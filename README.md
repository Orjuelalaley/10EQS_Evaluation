
# Product Pricing Analysis Tool

## Overview
This tool helps small business owners analyze their product pricing against market trends and generate actionable insights.

---

## Prerequisites
1. **Python**:
   - Ensure Python 3.7 or higher is installed on your system.
   - You can download it from [Python Official Website](https://www.python.org/).

2. **Pip**:
   - Pip is required to install the dependencies.
   - Run the following command to ensure pip is installed:
     ```bash
     python -m ensurepip --upgrade
     ```

---

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local system:
```bash
git clone <repository_url>
cd <repository_directory>
```

### 2. Install Dependencies
Install the required Python libraries, including `tabulate`, using the following command:
```bash
pip install -r src/requirements.txt
```

If the `requirements.txt` file includes all dependencies, it will automatically install `tabulate` along with `pandas`, `requests`, and others.

---

## Usage

### Running the Tool
1. Ensure the `products.csv` file is available in the `data/` directory.
2. Run the analysis script with the following command:
   ```bash
   python src/analysis.py data/products.csv
   ```

### Outputs
- The analysis output will be saved to a Markdown file called `report.md` in the root directory.

---

## Additional Notes
- If you encounter any issues, ensure all dependencies are installed by running:
  ```bash
  pip install tabulate pandas requests
  ```
- For assistance with specific errors, refer to the tool's GitHub repository issues or contact the developer.

---

## Example API Used
- API: [Exchange Rate API](https://www.exchangerate-api.com/)
- Endpoint: `https://api.exchangerate-api.com/v4/latest/USD`

---

## Example Output

The tool will generate a report like this:
```markdown
# Report

## Insights

| Product Name                | Our Price | Market Price | Price Difference |
|-----------------------------|-----------|--------------|------------------|
| Organic Coffee Beans (1lb)  | 14.99     | 16.49        | -1.50            |
| Premium Green Tea (50 bags) | 8.99      | 9.89         | -0.90            |
| Masala Chai Mix (12oz)      | 9.99      | 10.99        | -1.00            |
```
