import requests
import main



url = "https://language.googleapis.com/v1/documents:analyzeEntities"

<<<<<<< HEAD
querystring = {"key": ""}

=======
querystring = {"key":""}
>>>>>>> b332be37b7586a51cff5cb7b5b83c283e3b1ba7e

payload = "{\r\n  \"encodingType\": \"UTF8\",\r\n  \"document\": {\r\n    \"type\": \"PLAIN_TEXT\",\r\n    \"content\": \"placehodler\"\r\n  }\r\n}"

print(payload)

<<<<<<< HEAD
payload = "{\r\n  \"encodingType\": \"UTF8\",\r\n  \"document\": {\r\n    \"type\": \"PLAIN_TEXT\",\r\n    \"content\": \"placehodler\"\r\n  }\r\n}"

=======
>>>>>>> b332be37b7586a51cff5cb7b5b83c283e3b1ba7e
headers = {
    'cache-control': "no-cache",
    'postman-token': "c8d1159f-f3ef-6ff0-0916-bb72106f079b"
}

response = requests.request("POST", url, json=main.data_payload, headers=headers, params=main.querystring)

print(response.text)

<<<<<<< HEAD
=======


response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
>>>>>>> b332be37b7586a51cff5cb7b5b83c283e3b1ba7e

##f = open('137.json', 'w')
##f.write(response.text)
##f.close()
