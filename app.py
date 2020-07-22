import streamlit as st
import pages.home
import pages.setup_cleaning
import pages.salary_predictor
import pages.visualizations
import shared.components

PAGES = {
    'Home' : pages.home,
    'Setup & Cleaning' : pages.setup_cleaning,
    'Data Visualizations' : pages.visualizations,
    'Salary Predictor' : pages.salary_predictor
}

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        shared.components.write_page(page)

    st.sidebar.title("About")
    st.sidebar.info("""
        This app is maintained by Daman Heer. You can learn more about me at
        [damehero.github.io](https://damehero.github.io).
""")


if __name__ == "__main__":
    main()