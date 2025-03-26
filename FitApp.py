import os
import time as t
from dotenv import find_dotenv, load_dotenv
from groq import Groq
import streamlit as st

# Load environment variables
load_dotenv(find_dotenv())

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


# Function to generate a personalized diet plan based on user inputs
def generate_milestone(task_description):
    prompt = f'''
    You are a fitness and wellness coach, and your task is to generate a personalized, strict vegetarian Indian diet based on the user's body data and health considerations. Consider factors like the user's height, weight, gender, and any allergies or medical problems to tailor the recommendations. Ensure that the diet is nutritious, balanced, and meets the user's health needs.

    Given the following user inputs:

    Height: (user's height)
    Weight: (user's weight)
    Gender: (user's gender)
    Allergies or Medical Problems: (any specific issues or allergies)
    Generate the following:


    '''

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a personal wellness and fitness coach. Your task is to generate a strict vegetarian Indian diet plan for a user based on their body details and health conditions. The plan should be tailored to the user’s height, weight, gender, allergies, and any other medical problems they might have."
                },
                {
                    "role": "user",
                    "content": f"{task_description}, {prompt} \n\n"
                }
            ],
            model="llama3-8b-8192",
            temperature=0.3,
            stream=False,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"


# Streamlit UI
st.title("Personalized Vegetarian Indian Diet Plan Generator")

# Input fields for user data
height = st.number_input("Enter your height (in cm)", min_value=0, max_value=300, step=1)
weight = st.number_input("Enter your weight (in kg)", min_value=0, max_value=200, step=1)
gender = st.selectbox("Select your gender", ["Male", "Female", "Other"])
allergies = st.text_area("Enter any allergies or medical problems (Optional)", "")

# Button to generate the diet plan
if st.button("Generate Diet Plan"):
    if height and weight and gender:
        task_description = f"Height: {height} cm, Weight: {weight} kg, Gender: {gender}, Allergies/Medical Problems: {allergies}"
        result = generate_milestone(task_description)
        st.subheader("Generated Diet Plan:")
        st.write(result)
    else:
        st.error("Please fill in all required fields.")
