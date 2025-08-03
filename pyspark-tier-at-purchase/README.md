# Tier at Purchase — PySpark Analysis

This project analyzes **customer loyalty tier movements at the time of purchase** using PySpark. It helps identify how customer segments shift over time — including upgrades, downgrades, and first-time purchases — and the potential impact of expired rewards or benefits.

## 🔍 Key Features

- Extracts loyalty tier status **before and after each purchase**
- Flags expired loyalty assets and potential tier downgrades
- Identifies and categorizes customer behavior such as:
  - First Purchase
  - Upgrade
  - Downgrade
  - No Change
- Designed for use with distributed datasets (e.g., Spark/Delta tables)

## 📁 Project Structure

- `notebooks/`: Jupyter notebooks for interactive development
- `src/`: Optional reusable Python modules
- `docs/`: Extended documentation and notes (optional)

## 🛠️ Tech Stack

- **PySpark** for scalable data processing
- **Spark SQL** for structured queries
- **Jupyter / Databricks Notebooks** for interactive development
- **Matplotlib** / **ipywidgets** for optional visualization and interactivity

## ▶️ Quick Start

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/pyspark-tier-at-purchase.git
cd pyspark-tier-at-purchase
```

2. Open the notebook in your Spark-enabled environment (e.g., Databricks, AWS EMR, local PySpark)

3. Follow the logic in `notebooks/tier_at_purchase_analysis.ipynb` to generate your final DataFrame or view.

## 📈 Use Cases

- **Loyalty program analysis**: Track tier movement patterns over time
- **Customer segmentation**: Understand who upgrades or downgrades after key interactions
- **Churn risk modeling**: Identify early signs of disengagement via tier drops
- **Marketing impact**: Correlate campaigns with tier upgrades

---

## 📩 Contact

Built as part of an exploration into customer behavior analytics. Contributions and suggestions welcome!
