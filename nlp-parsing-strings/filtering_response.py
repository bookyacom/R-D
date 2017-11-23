## This file filters the results from a .txt file
import globalvars


## Prompt user which festival to check
query = globalvars.festival_name

## make sure input is valid

list = ['LOCATION', 'PERSON', 'OTHER', 'EVENT']

## Check the string in the lines and printing out the correct one.
def check_line(entity):
    txt = open(query, "r")
    line_list = []
    i = 0
    for line in txt:
        line_list.append(line.rstrip("\n"))
        if entity in line_list[i]:
            print(line_list[i - 1])
        i += 1


## Using all the entities
for i in range(len(list)):
    print(list[i])
    entity = list[i]
    check_line(entity)


## Print the date if found
if globalvars.dates is not "":
    print("possible date extracted: ")
    print(globalvars.dates)


## TODO: PUT RESULTS IN CSV



