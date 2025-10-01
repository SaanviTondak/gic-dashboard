# GIC Financial Transactions Dashboard  

## Objective  
This project delivers an **interactive data visualization dashboard** built with **Python + Streamlit** to analyze and communicate insights from a financial transactions dataset.  
It is developed as part of the GIC Internal Audit Data Analytics internship project.  


## Requirements Coverage  
**1. Dataset**  
- Input: `financial_transactions.csv` (provided).  
- Data cleaning and preprocessing handled in `src/data.py` (date parsing, numeric conversion, duplicate removal).  

**2. Visualization**  
- **Charts implemented:**  
  - Daily transaction totals (line chart)  
  - Spending by category (bar chart)  
  - Transaction type distribution (pie chart)  
  - Payment method vs category (heatmap)  
  - Top merchants (bar chart)  
  - Outlier transactions over time (scatter plot)  
- **Interactive features:**  
  - File uploader (upload custom CSVs)  
  - Date range selector  
  - Tab navigation for workflow separation  
  - KPI cards (Total, Average, Transaction count, Outlier count)  
- **Advanced functionality:**  
  - Outlier detection via **IQR** and **Isolation Forest**  

**3. Organization**  
- Modular project structure for clarity and maintainability:  
  - `src/data.py` → Data loading & cleaning  
  - `src/plots.py` → Visualization functions  
  - `src/outliers.py` → Outlier detection methods  
  - `app.py` → Main Streamlit application  

**4. Dependencies**
- Python 3.9+
- Streamlit
- Pandas
- Plotly
- NumPy
- scikit-learn
(All dependencies are listed in requirements.txt.)


**5. Installation**  

1. **Get the project**  
   - If using GitHub:  
     ```bash
     git clone https://github.com/<your-username>/gic-dashboard.git
     cd gic-dashboard
     ```
   - If using a zip file:  
     - Unzip the project and `cd` into the folder.  

2. **Set up a virtual environment (recommended)**  
   - Mac/Linux:  
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Windows:  
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt

4. **Prepare data**  
Place your financial_transactions.csv in the project root (if not already in), or use the file uploader in the dashboard to load a custom CSV.

5. **Run dashboard**  
streamlit run app.py

6. **Interact with dashboard**  
Open the provided local URL in your browser.
Use the sidebar to upload files, select date ranges, and explore different tabs and visualizations.



**4.Project Structure**  
gic-dashboard/
│
├── app.py                  # Main Streamlit application
├── financial_transactions.csv
├── requirements.txt
├── README.md
└── src/
    ├── __init__.py
    ├── data.py             # Data loading & cleaning
    ├── plots.py            # Visualization functions
    ├── outliers.py         # Outlier detection methods

