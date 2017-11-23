import requests
import main
import globalvars
import os.path




url = "https://language.googleapis.com/v1/documents:analyzeEntities"


querystring = {"key": ""}


payload = "{\r\n  \"encodingType\": \"UTF8\",\r\n  \"document\": {\r\n    \"type\": \"PLAIN_TEXT\",\r\n    \"content\": \"placeholder\"\r\n  }\r\n}"

headers = {
    'cache-control': "no-cache",
    'postman-token': "c8d1159f-f3ef-6ff0-0916-bb72106f079b"
}

response = requests.request("POST", url, json=main.data_payload, headers=headers, params=main.querystring)

##print(response.text)

## Check if the festival is already checked
exists = os.path.isfile(globalvars.festival_name)


## Make sure festivals are not printed twice, and put in results directory
if exists == False:
    f = open(globalvars.festival_name, 'w')
    f.write(response.text)
    f.close()
else:
    print("File already exists!")
