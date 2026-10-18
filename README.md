# Adidas Interactive Sales Dashboard

## 📌 Overview

This project is an **Interactive Adidas Sales Dashboard** built using Python, Streamlit, Pandas, and Plotly.

The dashboard analyzes Adidas retail sales data and presents key business metrics through interactive visualizations. It helps users explore sales performance across retailers, states, and time periods, making it easier to identify trends and understand business performance.

This project demonstrates practical skills in **Data Analysis, Data Visualization, Exploratory Data Analysis (EDA), and Interactive Dashboard Development**.

## 🎯 Project Objectives

- Analyze Adidas retail sales performance.
- Understand sales distribution across different retailers and states.
- Track total sales and units sold.
- Explore monthly sales trends.
- Create interactive visualizations to support data-driven decision-making.

## 📂 Project Structure

```text
Adidas-Sales-Dashboard/
│
├── app.py                  # Streamlit dashboard application
├── Adidas.xlsx             # Adidas retail sales dataset
├── adidas-logo.jpg         # Dashboard logo
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

*Note: Include only the files that are present in your GitHub repository. Create `requirements.txt` if you have not already done so.*

## 📊 Dataset

The project uses an Excel dataset containing Adidas retail sales information.

The dataset includes fields such as:

- **Retailer:** Retail company selling Adidas products.
- **Invoice Date:** Date of the sales transaction.
- **State:** Location associated with the sale.
- **Total Sales:** Revenue generated from sales.
- **Units Sold:** Number of units sold.
- **Product and sales details:** Additional attributes available in the dataset.

These fields help analyze sales performance across different business dimensions.

## 🛠️ Technologies Used

- **Python** – Data analysis and application development.
- **Pandas** – Data manipulation, aggregation, and cleaning.
- **Streamlit** – Interactive dashboard development.
- **Plotly Express** – Interactive charts and visualizations.
- **Plotly Graph Objects** – Customized charts.
- **OpenPyXL** – Reading Excel files through Pandas.
- **Pillow (PIL)** – Handling dashboard images.

## 🔍 Methodology

### 1. Data Loading

- Imported the Adidas Excel dataset using Pandas.
- Loaded the dataset into a DataFrame for analysis.
- Prepared the data for aggregation and visualization.

### 2. Data Preparation

- Worked with sales and invoice date columns.
- Grouped sales data by relevant business categories.
- Aggregated total sales and units sold.
- Created a Month-Year field to analyze sales over time.

### 3. Exploratory Data Analysis (EDA)

- Examined sales performance across retailers.
- Analyzed sales distribution across states.
- Explored total sales and units sold.
- Investigated monthly sales patterns.

### 4. Interactive Dashboard Development

- Built the dashboard using Streamlit.
- Used Plotly to create interactive visualizations.
- Added retailer-wise sales analysis.
- Organized the dashboard layout for readability.
- Incorporated Adidas branding and custom styling.

## 📈 Key Dashboard Features

- **Retailer-Wise Sales Analysis:** Compare sales performance across retailers.
- **State-Wise Sales Analysis:** Explore sales distribution across different states.
- **Sales Performance:** Analyze total sales and units sold.
- **Monthly Sales Trends:** Examine sales performance over time.
- **Interactive Visualizations:** Explore data through interactive charts.
- **Custom Dashboard Design:** Present business information in a structured, user-friendly layout.

## 💡 Business Value

This dashboard can help business stakeholders:

- Identify retailers contributing to sales performance.
- Understand geographical sales distribution.
- Monitor sales trends over time.
- Compare sales performance across business categories.
- Support data-driven sales and business planning.

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Adidas-Sales-Dashboard
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Install Python Dependencies

Make sure Python is installed on your system.

Install the required libraries:

```bash
pip install streamlit pandas openpyxl pillow plotly
```

### 3. Run the Dashboard

Open the terminal in your project folder and execute:

```bash
streamlit run app.py
```

Streamlit will open the dashboard in your web browser.

## 📸 Dashboard Preview


<img width="1327" height="572" alt="Monthly Sales and Retailer wise Sales" src="https://github.com/user-attachments/assets/fab1f442-e455-42b0-a448-5cbc44644012" />

<img width="1286" height="448" alt="Total Sales and Units sold by State" src="https://github.com/user-attachments/assets/3f3bc2c0-150c-45fa-ad84-354fc351bb2b" />

<img width="1242" height="493" alt="Tree map for total Sales for Region and city" src="https://github.com/user-attachments/assets/f068e111-acb0-4f77-9ba9-3514743134f7" />






## 📚 Skills Demonstrated

- Data Analysis with Python
- Data Manipulation using Pandas
- Exploratory Data Analysis
- Interactive Data Visualization
- Business KPI Analysis
- Dashboard Development using Streamlit
- Working with Excel Datasets
- Data Storytelling and Business Insights

## 👩‍💻 Author

**Syeda Saniya Anjum**

Aspiring Data Analyst | Python | SQL | Excel | Data Visualization

- LinkedIn: https://www.linkedin.com/in/syeda-saniya-anjum-9985a51a9
- GitHub: https://github.com/syedasaniyaanjum12-sudo

## ⭐ Acknowledgment

This project was developed as a practical learning project to strengthen my data analysis and dashboard development skills using Python and interactive visualization tools.

If you find this project useful, feel free to explore the repository and share your feedback!

