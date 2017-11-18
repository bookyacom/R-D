import csv
import json

import sys

import globalvars


## TODO: CREATE ENVIROMENT WITH GLOBAL VARIABLES FOR DATAPAYLOAD AND ALL THE OTHERS


## Declaring variables, need to be put in enviroment file later
globalvars.init()

## Getting google API key from the user
text = input("Please enter key: ")
globalvars.test_key = (text)
querystring = {"key": ""}


## Putting given key in querystring for API
for key, value in querystring.items():
    # change the key for user input
    querystring[key] = globalvars.test_key
    print(querystring[key])

## Opening json containing the festivals and bios
with open('onlybio.json', 'r') as data_file:
    festival_data = json.load(data_file)

## Iterating over de keys, making sure bio is not empty
for key in festival_data.keys():
    key_value = festival_data[key]
    if key_value != [{}] and key_value[0] != {}:
        ## Check what is in the bio
        bio = key_value[0]['bio']
        ## Add the bio to the list
        globalvars.bio_list.append(bio)
        ## Parse key into string, print the festival and the bio in the csv file
        i = str(key)
        globalvars.festival_list.append(i)



# Length of lists
bio_list_len = len(globalvars.bio_list)
festival_list_len = len(globalvars.festival_list)

## Making sure lists are of same len
if bio_list_len != festival_list_len:
    print("ERROR: Bio and festivals not same len")
    sys.exit()



## asking which bio to be used
while True:
    bio_input = input("Which bio you want to check?(input = number): ")
    if not bio_input.isdigit() or not 0 < int(bio_input) < festival_list_len :
        print("Wrong input! Which bio you want to check?: ")
        continue
    else:
        print("Correct input!")
        break

globalvars.test_case = int(bio_input)



## TODO, CHECK HOW I WRITE COLLUMNS FOR EACH ELEMENT
#with open('test_festivals.csv', 'w') as csvfile:
    #writer = csv.DictWriter(csvfile, fieldnames=['fdfdsfd', 'sfdfsd'], extrasaction='ignore')
    #writer.writeheader()
   # for key in csv_dict.keys():
       #key_value = csv_dict[key]
       # writer.writerow(key_value)





## Change bio string for POST
bio_string = globalvars.bio_list[globalvars.test_case]


# Declaring payload for google API POST request, bio_string is parsed
data_payload = {
  "encodingType": "UTF8",
  "document": {
    "type": "PLAIN_TEXT",
    "content": bio_string
  }
}


























