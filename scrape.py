filename = input("enter the name of the file you wish to scrape:")

search = input("enter a string to search for:").lower()
while search == "":
    search = input("you must enter a string:").lower()

index = 0
results = []

import csv
with open(filename) as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        if index != 0:
            for item in row:
                if search in item:
                    results.append(item)
        else:
            index += 1

if len(results) == 0:
    print("no matches were found")
else:
    print(len(results), "matches were found")
    for item in results:
        print(item)