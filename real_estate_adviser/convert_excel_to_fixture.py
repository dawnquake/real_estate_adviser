# convert_excel_to_fixture.py

import pandas as pd
import json
import os

def create_postcodes_fixture(excel_file: str):

    # Read Excel file
    df = pd.read_csv(excel_file)

    print(df)

    # Prepare JSON fixture format
    fixture = []
    for index, row in df.iterrows():
        fixture.append({
            "model": "dashboards.Postcode",
            "pk": index + 1,
            "fields": row.to_dict()
        })

    # Save to file
    with open('dashboards/fixtures/Postcodes.json', 'w') as f:
        json.dump(fixture, f, indent=4)


create_postcodes_fixture('preprocessing/cleaned_postcodes.csv')