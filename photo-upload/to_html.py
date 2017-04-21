import base64
import csv
import os

import re

OUTPUT_FOLDER = 'output'

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

csv.field_size_limit(2 * 1024 * 1024)

with open('170416071402_bilder_formidable_entries.csv', 'rb') as report, open('%s/index.html' % OUTPUT_FOLDER, 'wb') as output:
    report.readline()

    reader = csv.reader(report, delimiter=',', quotechar='"')
    for entry in reader:
        user, tag, imageData, timeStamp, lastUpdate, createdBy, updatedBy, draft, ip, id, key = entry
        print '%s uploaded %d bytes (starts with %s)' % (user, len(imageData), imageData[:100])
        mimeType = imageData[5:imageData.index(';')]
        extension = mimeType[mimeType.index('/') + 1:]
        filename = '%s/%s_%s_%s.%s' % (OUTPUT_FOLDER, user, re.sub(r'[^a-zA-Z0-9]', '', tag), id, extension)
        with open(filename, 'wb') as f:
            raw = base64.standard_b64decode(imageData[imageData.index(','):])
            f.write(raw)

        output.write('<img src="%s" alt="%s">' % (filename, tag))
