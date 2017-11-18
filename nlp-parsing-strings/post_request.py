import requests
import main



url = "https://language.googleapis.com/v1/documents:analyzeEntities"

querystring = {"key": ""}



payload = "{\r\n  \"encodingType\": \"UTF8\",\r\n  \"document\": {\r\n    \"type\": \"PLAIN_TEXT\",\r\n    \"content\": \"placehodler\"\r\n  }\r\n}"

headers = {
    'cache-control': "no-cache",
    'postman-token': "c8d1159f-f3ef-6ff0-0916-bb72106f079b"
}

response = requests.request("POST", url, json=main.data_payload, headers=headers, params=main.querystring)

print(response.text)


##f = open('137.json', 'w')
##f.write(response.text)
##f.close()
