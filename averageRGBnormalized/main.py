import json

# Open and read json file
with open('anklepants.json') as data_file:
    data = json.load(data_file)


## Setting up variables
count = 0
sum = 0
red = 0
blue = 0
green = 0


## For number of dominant colors
for i in range(0, 10):
    # Take the sum of the percentages
    sum += (data["responses"][0]["imagePropertiesAnnotation"]["dominantColors"]["colors"][count]["score"])
    # Red color
    red += (data["responses"][0]["imagePropertiesAnnotation"]["dominantColors"]["colors"][count]["score"])*(data["responses"][0]["imagePropertiesAnnotation"]["dominantColors"]["colors"][count]["color"]["red"])
    # Blue color
    blue += (data["responses"][0]["imagePropertiesAnnotation"]["dominantColors"]["colors"][count]["score"]) * (
    data["responses"][0]["imagePropertiesAnnotation"]["dominantColors"]["colors"][count]["color"]["blue"])
    # Green color
    green += (data["responses"][0]["imagePropertiesAnnotation"]["dominantColors"]["colors"][count]["score"]) * (
    data["responses"][0]["imagePropertiesAnnotation"]["dominantColors"]["colors"][count]["color"]["green"])
    count+= 1

print ("summing the total of scores...")
print (sum)
print ("normalized red color:", (red/sum))
print ("normalized green color:", green/sum)
print ("normalized blue color:", blue/sum)




