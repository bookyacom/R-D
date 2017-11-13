import csv
import json
import payload_api


## Opening json containing the festivals and bios
with open('onlybio.json', 'r') as data_file:
    festival_data = json.load(data_file)



with open('test_festivals.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for key in festival_data.keys():
        key_value = festival_data[key]
        if key_value != [{}]:
            print(key_value)
            i = str(key)
            writer.writerow([i])



data_payload = {
    "encodingType": "UTF8",
    "document": {
    "type": "PLAIN_TEXT",
    "content": "placehodler"
  }
}


















