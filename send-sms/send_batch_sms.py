# coding=utf-8
import csv
import datetime
import time
import os

import requests
import sys

messages_file = sys.argv[2]
IFTTT_EVENT_KEY = sys.argv[1]
IFTTT_EVENT_NAME = 'send_sms'


def trigger_ifttt_event(phone_number, message, log_writer):
    r = requests.post(
        'https://maker.ifttt.com/trigger/%s/with/key/%s' % (IFTTT_EVENT_NAME, IFTTT_EVENT_KEY),
        data={
            'value1': phone_number,
            'value2': message
        })
    log_writer.writerow([message, phone_number, r.status_code])
    print 'IFTTT Response Code to sending message "%s" to "%s": %s' % (message, phone_number, r.status_code)


if not os.path.isfile(messages_file):
    print 'Could not file %s.' % messages_file
    sys.exit(1)

with open(messages_file, 'rb') as messages, open('send_batch_sms_%s.log' % datetime.datetime.now().strftime('%Y%m%d_%H%M%S'), 'wb') as log:
    messages.readline()

    reader = csv.reader(messages, delimiter=',', quotechar='"')
    writer = csv.writer(log)

    for entry in reader:
        (team_name, contact_phone, message) = entry

        trigger_ifttt_event(contact_phone, message, writer)

        time.sleep(1)

os.rename(messages_file, '%s.done.csv' % messages_file)
