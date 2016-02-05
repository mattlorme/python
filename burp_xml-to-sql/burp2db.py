#!/usr/bin/python2.7

import xml.etree.ElementTree as ET
import MySQLdb
from pprint import pprint as pp
import hashlib
import csv

# DB connect
db1 = MySQLdb.connect(host="localhost", user="root", passwd="Passw0rd", db="vuln_db")

cursor = db1.cursor()
dict_cursor = db1.cursor(MySQLdb.cursors.DictCursor)

# get scanner that provided data source
scanner = raw_input('From which scanner are you importing data: ')

def prod_options():
    print (30 * '-')
    print ('   Product options')
    print (30 * '-')
    print ('ADC                 = BNADC')
    print ('FDC                 = BNFDC')
    print ('WebFilter           = BNYF')
    print ('WebAppFirewall      = BNWF')
    print ('SpamFirewall        = BNSF')
    print ('Load_Balancer_(OG)  = BNLB')
    print ('Message_Archiver    = BNMA')
    print ('SSL-VPN             = BNVS')
    print ('Firewall            = BNF')
    print ('CudaSign            = BNSGN')
    print ('Cloud_Control       = BNPL')
    print ('NG_Firewall         = BNNGF')
    print ('BBS                 = BNBS')
    print ('SSL-VPN_NG          = BNNGS')
    print ('Phone               = BNPH')
    print ('Camera              = BNEYE')
    print (30 * '-')

prod_options()

# get product for use as table-name
product = raw_input("Which appliance (see list above): ")

# get version/firmware
firmware = raw_input('Firmware (X.X.X.XXX): ')

# things to add to create table
sql = "CREATE TABLE IF NOT EXISTS " + scanner  + """(
    id INT NOT NULL AUTO_INCREMENT,
    created timestamp default '0000-00-00 00:00:00',
    updated timestamp default now() on update now(),
    product VARCHAR(10) NOT NULL,
    firmware VARCHAR(15) NOT NULL,
    u_firmware VARCHAR(15) DEFAULT NULL,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(500) DEFAULT NULL,
    severity VARCHAR(50) DEFAULT NULL,
    confidence VARCHAR(50) NOT NULL,
    path VARCHAR(100) NOT NULL,
    host VARCHAR(70) NOT NULL,
    is_secure BOOLEAN NOT NULL,
    request VARCHAR(750),
    issueDetail VARCHAR(1000),
    hash VARCHAR(150) UNIQUE NOT NULL,
    PRIMARY KEY (id)
)"""

cursor.execute(sql)

fname = raw_input('Enter .xml file name (absolute path required): ')

print fname

# XML parse w/ ElementTree
def parseXML(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    #print(root)
    vulns = []
    for child in root:
        vuln = {}
        if child.tag == "issue":
            for step_child in child:
                vuln[step_child.tag] = step_child.text
                vuln['request'] = vuln.get('request', 'None')
                vuln['issueDetail'] = vuln.get('issueDetail', 'None')
                if step_child.tag == "requestresponse":
                    for g_child in step_child:
                        vuln[g_child.tag] = g_child.text
                        #check for issueDetail, if it's missing, add it with value=None
                        #vuln['issueDetail'] = vuln.get('issueDetail', 'None')
            vulns.append(vuln)
    return vulns

# Getting return from func. parseXML() above and putting values here for fkeys below
tags = parseXML(fname)

#Calc hash from NAME, PRODUCT, LOCATION, and bool IS_SECURE
def calc_hash(issue):
    index = ''.join([issue['name'], issue['product'], issue['location'], str(issue['is_secure'])])
    md5 = hashlib.md5()
    md5.update(index)
    return md5.hexdigest()

#add bool value for purpose of hash uniqueNess
def is_secure(issue):
    return 'https' in issue['host']

# Loop through tags adding req. keys if missing and calling is_secure() and calc_hash()
count = 0
for issue in tags:
    count += 1
    issue['product'] = product
    issue['created'] = None
    issue['updated'] = None
    issue['firmware'] = firmware
    issue['is_secure'] = is_secure(issue)
    issue['hash'] = calc_hash(issue)

# keys to collect from tags({}) for inclusion in sqli (SQL INSERT BELOW)
fkeys = ["created","updated","product","firmware","name","location","severity","confidence","path","host","request","issueDetail","is_secure","hash"]

# Build new list of dicts with fkeys and associated values from tags({})
fvalues = [{k:v[k] for k in (fkeys)} for v in tags]

sqli = "INSERT INTO " + scanner  + """( created, updated, product, firmware, name, location, severity, confidence, path, is_secure, host, request, issueDetail, hash ) VALUES ( %(created)s, %(updated)s, %(product)s, %(firmware)s, %(name)s, %(location)s, %(severity)s, %(confidence)s, %(path)s, %(is_secure)s, %(host)s, %(request)s, %(issueDetail)s, %(hash)s ) ON DUPLICATE KEY UPDATE u_firmware = %(firmware)s, updated = now()"""

count_rows = "SELECT * from " + scanner
cursor.execute(count_rows)
rows_before = int(str(cursor.rowcount))

cursor.executemany(sqli, fvalues)

count_rows = "SELECT * from " + scanner
cursor.execute(count_rows)
rows_after = int(str(cursor.rowcount))

pp('total from xml :' + str(count))
pp('total rows before insert :' + str(rows_before))
pp('total rows after insert :' + str(rows_after))
print "New issues from this scan " + (str(rows_after - rows_before))

get_new = "Select product,firmware,name,location,severity,confidence,host,issueDetail from %s where firmware = '%s'" % (scanner, firmware)
dict_cursor.execute(get_new)
out_new = dict_cursor.fetchall()
#print out_new

db1.commit()
db1.close()

with open( product + '_' + firmware + '_New.csv', 'w') as outfile:
    fp = csv.DictWriter(outfile, out_new[0].keys())
    fp.writeheader()
    fp.writerows(out_new)


