import csv

import re


def sanitise(value):
    return re.sub('[^a-zA-Z0-9\s-]', '', value)


with open('170415113504_anmalan_formidable_entries.csv', 'rb') as report, open('google_contact_import.csv',
                                                                               'wb') as teams:
    report.readline()

    reader = csv.reader(report, delimiter=',', quotechar='"')
    writer = csv.writer(teams)

    writer.writerow(['Name', 'Phone 1 - Type', 'Phone 1 - Value', 'E-mail 1 - Type', 'E-mail 1 - Value'])
    for idx, entry in enumerate(reader):
        team_name = sanitise(entry[0])
        contact_name = sanitise(entry[6])
        contact_phone = sanitise(entry[7])
        contact_email = entry[8]

        values = ['TSL17 %s (%s)' % (team_name, contact_name), 'Mobile', contact_phone, 'Home', contact_email]
        writer.writerow(values)
