''' An old, true and sordid tale of python
   featuring raisins, checkboards, pushy relatives,
   business cards, and getting much rest.'''

import csv
import requests

vcard_tmpl = '''\
BEGIN:VCARD
VERSION:2.1
N:%s;%s
FN:%s %s
ORG:Raisins R Us, Inc.
TITLE:%s
TEL;WORK;VOICE:%s
ADR;WORK:;;100 Flat Grape;Fresno;CA;95555;United States of America
EMAIL;PREF;INTERNET:%s
REV:20080424T195243Z
END:VCARD
'''

def make_vcard(fname, lname, title, phone, email):
    'Return an electronic busincess card in the VCard 2.0 file format'
    return vcard_tmpl % (lname, fname, fname, lname, title, phone, email)


def make_qrcode(text):
    'Return a QR code in PNG format using the Google Chart REST API'
    # https://developers.google.com/chart/infographics/docs/qr_codes
    root_url = 'https://chart.googleapis.com/chart?'
    query = dict(cht='qr', chs='300x300', chl=text)
    return requests.get(root_url, query).content


if __name__ == '__main__':   
    with open('notes/raisin_team_update.csv') as f:
        for row in csv.reader(f):
            lname, fname, title, email, phone = row

            vcard = make_vcard(fname, lname, title, phone, email)

            filename = '%s_%s.vcf' % (fname, lname)
            with open(filename, 'w') as vcard_file:
                vcard_file.write(vcard)

            image = make_qrcode(vcard)
            filename = '%s_%s.png' % (fname, lname)
            with open(filename, 'wb') as f:
                f.write(image)


