import requests
import pandas as pd
import os

OUTPUT_PATH = "data/raw"

schemes = {
    "HDFC_Top_100_Direct": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for scheme_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    print(f"\nFetching NAV for {scheme_name}...")

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        meta = data.get("meta", {})
        nav_data = data.get("data", [])

        df = pd.DataFrame(nav_data)

        df["scheme_name"] = meta.get("scheme_name")
        df["fund_house"] = meta.get("fund_house")
        df["scheme_type"] = meta.get("scheme_type")
        df["scheme_category"] = meta.get("scheme_category")
        df["scheme_code"] = scheme_code

        output_file = os.path.join(
            OUTPUT_PATH,
            f"{scheme_name}_nav.csv"
        )

        df.to_csv(output_file, index=False)

        print(f"Saved: {output_file}")

        print(df.head())

    else:
        print("Failed to fetch data")