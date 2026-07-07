## Workflow


Master Datasets
│
├── destinations.csv
├── goods.csv
├── companies.csv
├── containers.csv
│
├── generate_dataset.py
│
▼
sample_containers.csv
│
▼
main.py
│
▼
output.csv

The framework operates in two stages:

1. **Dataset Generation**
   - Generates synthetic shipping container records from master datasets.

2. **Risk Assessment**
   - Reads each container record.
   - Computes the GTA risk score.
   - Produces an inspection recommendation.
   - Exports the results to `output.csv`.
