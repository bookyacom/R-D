import requests

url = "https://language.googleapis.com/v1/documents:analyzeEntities"

querystring = {"key":""}

payload = "{\r\n  \"encodingType\": \"UTF8\",\r\n  \"document\": {\r\n    \"type\": \"PLAIN_TEXT\",\r\n    \"content\": \"placehodler\"\r\n  }\r\n}"

print(payload)

headers = {
    'cache-control': "no-cache",
    'postman-token': "c8d1159f-f3ef-6ff0-0916-bb72106f079b"
    }



response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)