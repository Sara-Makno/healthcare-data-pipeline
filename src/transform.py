import csv

from extract import extract

def transform(encounters):

    transformed_encounters = []
    rejected_encounters = []

    for encounter in encounters:

        try:
            cleaned_encounter = encounter.copy()
            cleaned_encounter["charge_amount"] = float(encounter["charge_amount"])
            cleaned_encounter["length_of_stay"] = int(encounter["length_of_stay"])

            transformed_encounters.append(cleaned_encounter)
        except ValueError as error:
            rejected_encounters.append({
                "encounter_id": encounter["encounter_id"],
                "reason": str(error),
                "original_record": encounter
            })    

    return transformed_encounters, rejected_encounters

def save_rejected(rejected_encounters):

    with open("data/rejected/rejected_encounters.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "encounter_id",
            "reason",
            "original_charge_amount"
        ])

        for rejected in rejected_encounters:

            writer.writerow([
                rejected["encounter_id"],
                rejected["reason"],
                rejected["original_record"]["charge_amount"]
            ])


if __name__ == "__main__":

    encounters = extract()

    transformed_encounters, rejected_encounters = transform(encounters)

    save_rejected(rejected_encounters)

    print("Incoming encounters:", len(encounters))
    print("Valid encounters:", len(transformed_encounters))
    print("Rejected encounters:", len(rejected_encounters))