import csv
import json

def main():
    # Read the JSON configuration file
    with open("config.json", "r") as f:
        config = json.load(f)

    country_code = config["country_code"]
    peril = config["peril"]
    loc_currency = config["LocCurrency"]
    data_file = config["data_file"]

    # Read the CSV file and extract the latitude, longitude and country_code data
    with open(data_file, "r") as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            if row["FIPS_10_"] == country_code:
                data.append({"Latitude": row["lat"], "Longitude": row["long"], "CountryCode": country_code})

    # Save the extracted data to a CSV file
    with open("location.csv", "w", newline="") as f:
        fieldnames = ["PortNumber", "Latitude", "Longitude", "CountryCode", "ConstructionCode", "OccupancyCode", "LocPerilsCovered", "AccNumber", "LocNumber", "LocCurrency", "OtherTIV", "GeogName1", "GeogScheme1"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        loc_number = 1
        for row in data:
            for construction_code in ['5100', '5150', '5200']:
                for occupancy_code in ['1100', '1150', '1250']:
                    row["ConstructionCode"] = construction_code
                    row["OccupancyCode"] = occupancy_code
                    row["LocPerilsCovered"] = peril
                    row["PortNumber"] = "Portfolio"
                    row["AccNumber"] = 1
                    row["LocNumber"] = loc_number
                    row["LocCurrency"] = loc_currency
                    row["OtherTIV"] = '0'
                    row["GeogName1"] = ''
                    row["GeogScheme1"] = ''
                    writer.writerow(row)
                    loc_number += 1

if __name__ == "__main__":
    main()

