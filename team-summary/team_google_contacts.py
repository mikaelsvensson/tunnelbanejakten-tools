import csv

import re


def sanitise(value):
    return re.sub('[^a-zA-Z0-9\s-]', '', value)


with open('170415113504_anmalan_formidable_entries.csv', 'rb') as report, open('google_contact_import.csv',
                                                                               'wb') as teams:
    report.readline()

    reader = csv.reader(report, delimiter=',', quotechar='"')
    writer = csv.writer(teams)

    writer.writerow(
        ['Name', 'Given Name', 'Additional Name', 'Family Name', 'Yomi Name', 'Given Name Yomi', 'Additional Name Yomi',
         'Family Name Yomi', 'Name Prefix', 'Name Suffix', 'Initials', 'Nickname', 'Short Name', 'Maiden Name',
         'Birthday', 'Gender', 'Location', 'Billing Information', 'Directory Server', 'Mileage', 'Occupation', 'Hobby',
         'Sensitivity', 'Priority', 'Subject', 'Notes', 'Group Membership', 'E-mail 1 - Type', 'E-mail 1 - Value',
         'Phone 1 - Type', 'Phone 1 - Value'])
    for idx, entry in enumerate(reader):
        team_name = sanitise(entry[0])
        contact_name = sanitise(entry[6])
        contact_phone = sanitise(entry[7])
        contact_email = entry[8]

        display_name = 'TSL17 %s (%s)' % (team_name, contact_name)
        values = [
            display_name, "", "", display_name, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
            "", "", "", "", " * My Contacts", " * INTERNET", contact_email, "Mobile", contact_phone
        ]
        writer.writerow(values)
