# coding=utf-8
import csv

import re

import datetime

import sys


def sanitise(value):
    return re.sub('[^a-zA-Z0-9\s+-]', '', value)

def get_welcome_message(entry):
    team_name = entry[0]
    contact_name = entry[6].split()[0]
    return 'Hej %s. Vi hoppas ni i %s är taggade inför Tunnelbanejakten imorgon! Incheckning 8:30-9:00. Visa upp detta SMS vid incheckningen för att bekräfta att telefonnumret stämmer. Mvh. Kundtjänst' % (contact_name, team_name)


generators = {
    'welcome': get_welcome_message
}


message_generator = generators[sys.argv[1]]

with open('170415113504_anmalan_formidable_entries.csv', 'rb') as report, open('sms_%s.csv' % datetime.datetime.now().strftime('%Y%m%d_%H%M%S'),
                                                                               'wb') as teams:
    report.readline()

    reader = csv.reader(report, delimiter=',', quotechar='"')
    writer = csv.writer(teams)

    writer.writerow(['TEAM_NAME', 'PHONE', 'MESSAGE'])
    for idx, entry in enumerate(reader):
        team_name = entry[0]
        contact_phone = sanitise(entry[7])

        message = message_generator(entry)

        values = [team_name, contact_phone, message]
        writer.writerow(values)
