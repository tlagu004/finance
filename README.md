# 📈 Personal Finance Tracker

A real-time financial dashboard built with Python, Streamlit, and Plotly. This application allows users to track expenses, visualize spending habits, and manage budget goals through interactive charts.

---

## 🚀 App's purpose

A financial tracker to visualize and manage expenses. Users can upload a CSV of transactions, categorize them, and view summaries.

---

## 📀 Dataset used

The user provides their own dataset in the form of a CSV file. The expected CSV format is: `Date`, `Details`, `Amount`, `Debit/Credit`.

---

## 📖 User instructions

1.  **Run the app:** `streamlit run main.py`
2.  **Upload CSV:** Use the file uploader to select your transaction CSV.
3.  **Categorize:**
    *   Create new categories.
    *   Assign transactions to categories in the "Expenses (Debits)" tab.
    *   Changes are saved automatically.
4.  **View Summaries:**
    *   See a breakdown of expenses by category.
    *   View a pie chart of your spending.
    *   Check total income in the "Income (Credits)" tab.

---

## 🛠️ Tech Stack

-   **Language**: Python 3.10+
-   **Web Framework**: Streamlit
-   **Data Analysis**: Pandas, NumPy
-   **Plotting**: Plotly

---

## 💻 Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/tlagu004/finance.git
    cd finance
    ```

2.  **Set up the Environment:**
    Since this project is configured for Nix/Replit, use a virtual environment to manage dependencies:

    ```bash
    # Create a virtual environment
    python3 -m venv .venv

    # Activate the environment
    source .venv/bin/activate

    # Install dependencies
    pip install -r requirements.txt
    ```

3.  **Run the Application:**
    ```bash
    streamlit run main.py
    or
    streamlit run main.py --server.enableCORS false --server.enableXsrfProtection false
    ```

---

## 📝 License

This project is open-source and available under the MIT License.
