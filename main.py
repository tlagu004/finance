import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os

# Set page metadata for the Streamlit app, including title, icon, and layout.
st.set_page_config(page_title="Finance App", page_icon="💰", layout="wide")

# Define the filename for storing transaction categories.
category_file = "categories.json"

# Initialize session state for categories if it doesn't exist.
if "categories" not in st.session_state:
    st.session_state.categories = {
        "Uncategorized": []
    }

# Load transaction categories from the specified JSON file if it exists.
if os.path.exists(category_file):
    with open(category_file, "r") as f:
        st.session_state.categories = json.load(f)
# Function to save the current categories to the JSON file.
def save_categories():
    with open(category_file, "w") as f:
        json.dump(st.session_state.categories, f)

# Function to categorize transactions based on keywords in the 'Details' column.
def categorize_transactions(df):
    df["Category"] = "Uncategorized"
    for category, keywords in st.session_state.categories.items():
        if category == "Uncategorized" or not keywords:
            continue
        lowered_keywords = [keyword.lower().strip() for keyword in keywords]
        for idx, row in df.iterrows():
            details = row["Details"].lower().strip()
            if details in lowered_keywords:
                df.at[idx, "Category"] = category
    return df

# Function to add a new keyword to a specified category and save the updated categories.
def add_keyword_to_category(category, keyword):
    keyword = keyword.strip()
    if keyword and keyword not in st.session_state.categories[category]:
        st.session_state.categories[category].append(keyword)
        save_categories()
        return True
    return False

# Function to load transactions from a CSV file, process the data, and categorize it.
def load_transactions(file):
    try:
        df = pd.read_csv(file)
        df.columns = [col.strip() for col in df.columns]
        df["Amount"] = df["Amount"].str.replace(",", "").astype(float)
        df["Date"] = pd.to_datetime(df["Date"], format="%d %b %Y")
        return categorize_transactions(df)
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
        return None

# Main function to run the Streamlit application.
def main():
    st.title("Financial Tracker")
    uploaded_file = st.file_uploader("Upload transactions CSV File", type=["csv"])
    if uploaded_file is not None: 
        df = load_transactions(uploaded_file)

        if df is not None:
            debits_df = df[df["Debit/Credit"] == "Debit"].copy()
            credits_df = df[df["Debit/Credit"] == "Credit"].copy()

            st.session_state.debits_df = debits_df.copy()
            tab1, tab2 = st.tabs(["Expenses (Debits)", "Income (Credits)"])


            # This section allows users to view, categorize, and analyze their debit transactions.
            with tab1:
                # Adding new expense categories.
                new_category = st.text_input("New Category Name")
                add_button = st.button("Add Category")

                if add_button and new_category:
                    if new_category not in st.session_state.categories:
                        st.session_state.categories[new_category] = []
                        save_categories()
                        st.rerun()

                st.subheader("Your expenses")
                # Editable data table for assigning categories to transactions.
                edited_debits_df = st.data_editor(
                    st.session_state.debits_df[["Date", "Details", "Amount", "Category"]],
                    column_config={
                        "Date": st.column_config.DateColumn("Date", format="DD/MM/YYYY"),
                        "Amount": st.column_config.NumberColumn("Amount", format="%.2f AED"),
                        "Category": st.column_config.SelectboxColumn(
                            "Category",
                            options=list(st.session_state.categories.keys())
                        )
                    },
                    hide_index=True,
                    use_container_width=True,
                    key="debits_category_editor"
                )
                save_button = st.button("Apply Changes", type="primary")
                if save_button:
                    for idx, row in edited_debits_df.iterrows():
                        new_category = row["Category"]
                        if new_category == st.session_state.debits_df.at[idx, "Category"]: continue

                        details = row["Details"]
                        st.session_state.debits_df.at[idx, "Category"] = new_category
                        add_keyword_to_category(new_category, details)
                # Displaying an expense summary by category.
                st.subheader("Expense Summary")
                category_totals = st.session_state.debits_df.groupby("Category")["Amount"].sum().reset_index()
                category_totals = category_totals.sort_values("Amount", ascending=False)
                st.dataframe(category_totals,
                    column_config={
                     "Amount": st.column_config.NumberColumn("Amount", format="%.2f AED")   
                    },
                    use_container_width=True,
                    hide_index=True
                )
                # Visualizing expense distribution with a pie chart.
                fig = px.pie(
                    category_totals,
                    values="Amount",
                    names="Category",
                    title="Expenses by Category"
                )
                st.plotly_chart(fig, use_container_width=True)
            # This section displays Payments Summary with Table including date, details, and amount information.
            with tab2:
                st.subheader("Payments Summary")
                total_payments = credits_df["Amount"].sum()
                st.metric("Total Payments", f"{total_payments: ,.2f} AED")
                st.write( credits_df[["Date", "Details", "Amount"]])

# Run the main function to start the application.
main()