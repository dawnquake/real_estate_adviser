# convert_excel_to_fixture.py

import pandas as pd
import simplejson as json
import os

def create_products_fixture(excel_file: str):

    # Read Excel file
    df = pd.read_csv(excel_file)

    # Prepare JSON fixture format
    fixture = []
    for index, row in df.iterrows():
        fixture.append({
            "model": "dashboards.Postcode",
            "pk": index + 1,
            "fields": row.to_dict()
        })

    # Save to file
    with open(os.path.join('preprocessing', 'london_postcodes_cleaned.json'), 'w') as f:
        json.dump(fixture, f, indent=4, ignore_nan=True)

create_products_fixture(os.path.join('preprocessing', 'london_postcodes_cleaned.csv'))