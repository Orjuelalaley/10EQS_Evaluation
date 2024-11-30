import sys
from utils import load_csv, fetch_external_data, generate_insights, save_report


def main():
    if len(sys.argv) < 2:
        print("Usage : python src/analysis.py data/products.csv")
        sys.exit(1)

    # loading the csv file
    csv_file = sys.argv[1]
    try:
        products = load_csv(csv_file)
    except FileNotFoundError:
        print(f"Error : File Not Found at {csv_file}")
        sys.exit(1)

    try:
        external_data = fetch_external_data()
    except Exception as e:
        print(f"Error fetching external data : {e}")
        sys.exit(1)

    insights = generate_insights(products, external_data)

    try:
        save_report(insights, "report.md")
        print("Report saved to report.md")
    except Exception as e:
        print(f" Error saving report : {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
