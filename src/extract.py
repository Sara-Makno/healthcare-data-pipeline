import csv


def extract():
    file = open("data/raw/encounters.csv", "r")

    reader = csv.DictReader(file)

    encounters = []

    for row in reader:
        encounters.append(row)

    file.close()

    return encounters


encounters = extract()

if __name__ == "__main__":
    encounters = extract()

    print("Number of encounters:", len(encounters))
    print("First encounter:", encounters[0])
    print("Encounter collection type:", type(encounters))
    print("Single encounter type:", type(encounters[0]))
    print("Charge amount type:", type(encounters[0]["charge_amount"]))