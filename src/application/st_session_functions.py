"""
Module that holds all helper functions related to the streamlit session state
includes :
    - initialization of session state
    - variable storing in session state before switching pages + page switching
"""

import pandas as pd
import streamlit as st


def initialize_session_state() -> None:
    """
    Initialize all necessary keys in the Streamlit session state if they are not already present.
    Allows for better readability in the app file
    """
    default_values = {
        'recipe_id': '',
        'title': '',
        'ingredients': '',
        'instructions': '',
        'link': '',
        'total_recipes': None,
        'search_df': None,
        'research_summary': None,
        'filters': None,
        'recipe_type': None,
        'rating': None,
        'vote': None,
        'author': None,
        'c_time': None,
        'prep_time': None,
        'servings': None,
        'tot_time': None,
        'description': None,
        'keywords': None,
        'img_link': None,
        'rec_link': None,
        'calories': None,
        'protein': None,
        'fat': None,
        'sat_fat': None,
        'chol': None,
        'sodium': None,
        'carbo': None,
        'fiber': None,
        'sugar': None,
    }

    for key, value in default_values.items():
        if key not in st.session_state:
            st.session_state[key] = value


def handle_recipe_click(page: pd.DataFrame, index: int) -> None:
    """
    Update Streamlit session state variables with recipe details -for use across pages- from the
    given DataFrame row and navigates to the recipe page.

    Parameters:
    ----------
    page : pd.DataFrame
        DataFrame containing recipe data, where each row represents a recipe, with information
        such as title, ingredients, cooking time, etc.
    index : int
        The index of the selected recipe row in the DataFrame

    Session State Variables Updated:
    -------------------------------
    - `recipe_id`: str - Recipe id
    - `title`: str - Recipe title
    - `ingredients`: str - Ingredients list
    - `instructions`: str - Preparation instructions
    - `link`: str - Source link for the recipe
    - `rating`: float - Aggregated rating of the recipe
    - `vote`: int - Number of reviews/votes
    - `author`: str - Name of the recipe's author
    - `c_time`: str - Cooking time
    - `prep_time`: str - Preparation time
    - `servings`: int - Number of servings the recipe yields
    - `tot_time`: str - Total time required for the recipe
    - `description`: str - Description of the recipe
    - `keywords`: str - Relevant keywords or tags for the recipe
    - `img_link`: str - URL to the recipe's image
    - `calories`: float - Calorie content per serving
    - `protein`: float - Protein content per serving
    - `fat`: float - Total fat content per serving
    - `sat_fat`: float - Saturated fat content per serving
    - `chol`: float - Cholesterol content per serving
    - `sodium`: float - Sodium content per serving
    - `carbo`: float - Carbohydrate content per serving
    - `fiber`: float - Fiber content per serving
    - `sugar`: float - Sugar content per serving

    Returns:
    --------
    None
    """
    st.session_state.recipe_id = page.iloc[index]['recipe_id']
    st.session_state.title = page.iloc[index]['title']
    st.session_state.ingredients = page.iloc[index]['ingredients']
    st.session_state.instructions = page.iloc[index]['directions']
    st.session_state.link = "https://" + page.iloc[index]['link']
    # st.session_state.correspondance_rate = page.iloc[index]['%']
    st.session_state.rating = page.iloc[index]['AggregatedRating']
    st.session_state.vote = page.iloc[index]['ReviewCount']
    st.session_state.author = page.iloc[index]['AuthorName']
    st.session_state.c_time = page.iloc[index]['CookTime']
    st.session_state.prep_time = page.iloc[index]['PrepTime']
    st.session_state.servings = page.iloc[index]['RecipeServings']
    st.session_state.tot_time = page.iloc[index]['TotalTime']
    st.session_state.description = page.iloc[index]['Description']
    st.session_state.keywords = page.iloc[index]['Keywords']
    st.session_state.img_link = page.iloc[index]['Images']
    # st.session_state.rec_link = page.iloc[index]['Images']
    st.session_state.calories = page.iloc[index]['Calories']
    st.session_state.protein = page.iloc[index]['ProteinContent']
    st.session_state.fat = page.iloc[index]['FatContent']
    st.session_state.sat_fat = page.iloc[index]['SaturatedFatContent']
    st.session_state.chol = page.iloc[index]['CholesterolContent']
    st.session_state.sodium = page.iloc[index]['SodiumContent']
    st.session_state.carbo = page.iloc[index]['CarbohydrateContent']
    st.session_state.fiber = page.iloc[index]['FiberContent']
    st.session_state.sugar = page.iloc[index]['SugarContent']
    with st.spinner():
        st.switch_page("./pages/recipe_page.py")
