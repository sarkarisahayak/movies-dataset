import altair as alt
import pandas as pd
import streamlit as st

# Show the page title and description.
st.set_page_config(page_title="Movies dataset", page_icon="🎬")
st.title("🎬 Movies dataset")
st.write(
    """
    This app visualizes data from [The Movie Database (TMDB)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).
    It shows which movie genre performed best at the box office over the years. Just 
    click on the widgets below to explore!
    """
)


# Load the data from a CSV. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_data():
    df = pd.read_csv("data/movies_genres_summary.csv")
    df2=pd.read_csv("data/can.csv")
    return df


df = load_data()

# Show a multiselect widget with the genres using `st.multiselect`.
options = st.multiselect(
    "enter names",["Anuradha Tai Chavan", "Suhas Shirsath", "Vijay Autade", "Bhagwan Bapu Ghadamode", "Kalyaan Kale", 
                  "Vilas Autade", "Vishwas Autade", "Jagannath Kale", "Sandeep Borse", "Varun Pathrikar", 
                  "Rajendra Thombre", "Kishor Balande", "Ramesh Pawar"],)



