import csv
import json

with open('strings_festivals.json') as data_file:
    festival_data = json.load(data_file)

with open('test_festivals.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['FESTIVAL', 'LOCATION', 'PERSON'])

