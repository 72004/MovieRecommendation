import streamlit as st
import pandas as pd

# Load the recommendation dataset
@st.cache_data
def load_data():
    return pd.read_csv('MovieRecommendations.csv')

df_result = load_data()

# Function to get movie recommendations
def get_recommendations(movie_name):
    list_result = df_result[df_result['title'] == movie_name]
    if not list_result.empty:
        return list_result.iloc[0, -4:].values
    else:
        return None

# Streamlit UI
st.title("🎬 Movie Recommender System")

# Movie selection
selected_movie = st.selectbox("Choose a movie:", df_result['title'].unique())

if st.button("Get Recommendations"):
    recommendations = get_recommendations(selected_movie)
    
    if recommendations is not None:
        st.success(f"Top movie recommendations for **{selected_movie}**:")
        for i, movie in enumerate(recommendations, 1):
            st.write(f"**{i}.** {movie}")
    else:
        st.error("Movie not found in the database.")

st.sidebar.write("💡 Select a movie to see similar recommendations.")
