import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

# Load API key from environment
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("API key not found. Please check your .env file.")
    st.stop()

# Configure the API
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

# Template for the AI to generate multiple recipe names
recipe_names_prompt = """
You are an expert chef AI.

Given the cuisine type and available ingredients, generate five unique recipe names. Keep the descriptions brief and focused solely on the name of the dish.

Cuisine type: {cuisine}
Ingredients: {ingredients}
"""

# Template for the AI to provide detailed cooking instructions
detailed_recipe_prompt = """
You are an expert chef AI.

Provide detailed cooking instructions for the selected recipe. Include:

- Ingredients list
- Step-by-step instructions
- Cooking time and temperature
- Serving suggestions

Recipe name: {recipe_name}
"""

def generate_content(prompt):
    response = model.generate_content(prompt)
    return response.text

# Streamlit user interface
st.title("🍳 Cooking Recipe Selector")
st.write("Enter the type of cuisine and ingredients you have, and select a recipe from the options provided:")

# User inputs
cuisine = st.text_input("Type of cuisine (e.g., Italian, Indian):")
ingredients = st.text_input("Available ingredients (e.g., chicken, tomatoes, basil):")

if st.button("Get Recipe Options"):
    user_prompt = recipe_names_prompt.format(cuisine=cuisine, ingredients=ingredients)
    recipe_names = generate_content(user_prompt).split('\n')  # Assuming model outputs are separated by newlines
    st.session_state['recipe_names'] = recipe_names  # Save to session state
    st.session_state['selected_recipe'] = recipe_names[0]  # Default selection
    st.experimental_rerun()

recipe_name = st.selectbox("Choose a recipe to get detailed instructions:", st.session_state.get('recipe_names', []), index=0, key="selected_recipe")

if st.button("Show Detailed Instructions"):
    if 'selected_recipe' in st.session_state:
        detailed_instructions_prompt = detailed_recipe_prompt.format(recipe_name=st.session_state['selected_recipe'])
        detailed_instructions = generate_content(detailed_instructions_prompt)
        st.write("Here are the detailed cooking instructions:")
        st.write(detailed_instructions)
