# 📈 Personal Finance Tracker

A real-time financial dashboard built with Python, Streamlit, and Plotly. This application allows users to track expenses, visualize spending habits, and manage budget goals through interactive charts.

---

## 🚀 Features

-   **Interactive Visualizations**: Dynamic pie charts and bar graphs using Plotly.
-   **Data Management**: Easy data manipulation powered by Pandas.
-   **Clean UI**: Simple, intuitive dashboard interface via Streamlit.
-   **Expense Tracking**: Categorize and monitor your monthly spending.

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
