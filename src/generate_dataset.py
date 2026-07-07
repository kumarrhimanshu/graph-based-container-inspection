import csv
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "datasets"

# Load master datasets
with open(DATASET_DIR / "destinations.csv", newline="", encoding="utf-8") as f:
    destinations = list(csv.DictReader(f))

with open(DATASET_DIR / "goods.csv", newline="", encoding="utf-8") as f:
    goods = list(csv.DictReader(f))

with open(DATASET_DIR / "companies.csv", newline="", encoding="utf-8") as f:
    companies = list(csv.DictReader(f))

with open(DATASET_DIR / "containers.csv", newline="", encoding="utf-8") as f:
    containers = list(csv.DictReader(f))

# Output file
output_file = DATASET_DIR / "sample_containers.csv"

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow([
        "Container_ID",
        "Destination",
        "Goods",
        "Container_Length",
        "Actual_Weight",
        "Shipping_Company"
    ])

    for i in range(1, 1001):

        destination = random.choice(destinations)
        item = random.choice(goods)
        company = random.choice(companies)
        container = random.choice(containers)

        length = container["Length_ft"]
        standard_weight = int(container["Standard_Weight_kg"])

        actual_weight = standard_weight + random.randint(-400, 400)

        writer.writerow([
            f"C{i:06d}",
            destination["Destination"],
            item["Goods"],
            length,
            actual_weight,
            company["Company"]
        ])

print(f"Dataset generated successfully: {output_file}")
