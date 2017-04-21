import csv

with open('170415113504_anmalan_formidable_entries.csv', 'rb') as report:
    report.readline()

    reader = csv.reader(report, delimiter=',', quotechar='"')
    for idx, entry in enumerate(reader):
        print entry[0]
