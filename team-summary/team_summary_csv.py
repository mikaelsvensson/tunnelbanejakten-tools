import csv

with open('170415113504_anmalan_formidable_entries.csv', 'rb') as report, open('teams.csv', 'wb') as teams:
    report.readline()

    reader = csv.reader(report, delimiter=',', quotechar='"')
    writer = csv.writer(teams)

    writer.writerow(['Lag', 'LagKort', 'Klass', 'AntalDeltagare', 'BiljettNr1', 'BiljettNr2', 'BiljettNr3'])
    for idx, entry in enumerate(reader):
        team_name = entry[0]
        count = entry[1]
        category = entry[2]

        values = [team_name.upper()[:30], team_name.upper()[:15], category, count, 'TSL%03d' % (idx * 3+1), 'TSL%03d' % (idx * 3 + 2), 'TSL%03d' % (idx * 3 + 3)]
        writer.writerow(values)
