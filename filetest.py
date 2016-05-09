vcard_tmpl =''' BEGIN:VCARD
VERSION:2.1
N:%s
FN:%s
ORG:Bubba Gump Shrimp Co.
TITLE:%s
PHOTO;GIF:http://www.example.com/dir_photos/my_photo.gif
TEL;WORK;VOICE:%s
TEL;HOME;VOICE:(404) 555-1212
ADR;WORK:;;100 Waters Edge;Baytown;LA;30314;United States of America
LABEL;WORK;ENCODING=QUOTED-PRINTABLE:100 Waters Edge=0D=0ABaytown, LA 30314=0D=0AUnited States of America
ADR;HOME:;;42 Plantation St.;Baytown;LA;30314;United States of America
LABEL;HOME;ENCODING=QUOTED-PRINTABLE:42 Plantation St.=0D=0ABaytown, LA 30314=0D=0AUnited States of America
EMAIL;%s;INTERNET:forrestgump@example.com
REV:20080424T195243Z
END:VCARD'''

import requests
import csv

def make_qrcode(text):
    'Return a QR code in PNG format using Google REST API'
    #url
    root_url = 'https://chart.googleapis.com/chart?'
    query = dict(cht='qr',chs='300x300',chl=text)
    return requests.get(root_url,query).content



with open('notes/raisin_team.csv') as f:
    for line in f:
        line = line.rstrip()
        fields = line.split(',')
        lname, fname, title, email, phone = fields

        vcard = vcard_tmpl % (lname, fname,title, email,phone)

        filename = '%s_%s.vcf' % (fname,lname)
        with open(filename, 'w') as vcard_file:
            vcard_file.write(vcard)

        image = make_qrcode(vcard)
        finename ='%s_%s.png' % (fname,lname)
        with open(filename,'wb') as f:
            f.write(image)


#print (vcard_tmpl % (lname, fname,title, email,phone))
#vcard = vcard_tmpl % (lname, fname,title, email,phone)


#with open('tmp.vcf', 'w') as vcard_file:
#    vcard_file.write(vcard)

