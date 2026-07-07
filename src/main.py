import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "datasets"

# Load master data
destinations = {}
with open(DATASET_DIR / "destinations.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        destinations[row["Destination"]] = float(row["Risk_Weight"])

goods = {}
with open(DATASET_DIR / "goods.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        goods[row["Goods"]] = float(row["Risk_Weight"])

companies = {}
with open(DATASET_DIR / "companies.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        companies[row["Company"]] = float(row["Risk_Weight"])

containers = {}
with open(DATASET_DIR / "containers.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        containers[row["Length_ft"]] = int(row["Standard_Weight_kg"])

# Priority factors
lambda1 = 0.4321
lambda2 = 0.3210
lambda3 = 0.1542
lambda4 = 0.0927

input_file = DATASET_DIR / "sample_containers.csv"
output_file = DATASET_DIR / "output.csv"

with open(input_file, newline="", encoding="utf-8") as infile, \
     open(output_file, "w", newline="", encoding="utf-8") as outfile:

    reader = csv.DictReader(infile)
    writer = csv.writer(outfile)

    writer.writerow([
        "Container_ID",
        "Destination",
        "Goods",
        "Container_Length",
        "Actual_Weight",
        "Shipping_Company",
        "Weight_Difference",
        "Risk_Score",
        "Decision"
    ])

    for row in reader:

        standard_weight = containers[row["Container_Length"]]
        actual_weight = int(row["Actual_Weight"])
        difference = abs(actual_weight - standard_weight)

        if difference <= 50:
            weight_factor = 0.01
        elif difference <= 100:
            weight_factor = 0.07
        elif difference <= 200:
            weight_factor = 0.40
        elif difference <= 300:
            weight_factor = 0.60
        else:
            weight_factor = 0.80

        R = (
            lambda1 * weight_factor
            + lambda2 * destinations[row["Destination"]]
            + lambda3 * goods[row["Goods"]]
            + lambda4 * companies[row["Shipping_Company"]]
        )

        decision = (
            "Store to ship"
            if R <= 0.30
            else "Proceed to further inspection"
        )

        writer.writerow([
            row["Container_ID"],
            row["Destination"],
            row["Goods"],
            row["Container_Length"],
            actual_weight,
            row["Shipping_Company"],
            difference,
            round(R, 3),
            decision
        ])

print(f"Analysis completed successfully: {output_file}")
