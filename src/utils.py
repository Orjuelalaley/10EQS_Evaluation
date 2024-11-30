import pandas as pd
import requests


def load_csv(filepath):
    return pd.read_csv(filepath)


def fetch_external_data():
    url = "https://v6.exchangerate-api.com/v6/2a70a9875a7590706ede96c0/latest/USD"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch external data")


def generate_insights(products, external_data):
    products["market_price"] = products["our_price"] * 1.1
    products["price_different"] = products["our_price"] - products["market_price"]
    return products


def save_report(data, filepath):
    with open(filepath, "w") as f:
        f.write("Report\n\n")
        f.write("## Insights\n\n")
        f.write(data.to_markdown())
