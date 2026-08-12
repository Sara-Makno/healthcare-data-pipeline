import csv
file = open("data/raw/encounters.csv", "r")
reader = csv.DictReader(file)
for row in reader:
    print(row)
file.close()
    