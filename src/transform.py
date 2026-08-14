from extract import extract

def transform(encounters):
    for encounter in encounters:
        encounter["charge_amount"] = float(encounter["charge_amount"])
        encounter["length_of_stay"] = int(encounter["length_of_stay"])
        
    return encounters

if __name__ == "__main__":

    encounters = extract()

    transformed_encounters = transform(encounters)

    print("Number of transformed encounters:", len(transformed_encounters))
    print("First transformed encounter:", transformed_encounters[0])

    print( "Length of stay type:", type(transformed_encounters[0]["length_of_stay"]))

    print(
        "Charge amount type:",
        type(transformed_encounters[0]["charge_amount"])
    )