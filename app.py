import streamlit as st # type: ignore
import random

# Constants
PROMPT = "Enter your name:"
JOKES = [
    "Why don’t skeletons fight each other? They don’t have the guts!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What did one ocean say to the other ocean? Nothing, they just waved!",
    "Why do cows have hooves instead of feet? Because they lactose!",
    "Why don’t programmers like nature? It has too many bugs.",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "What’s a computer’s favorite snack? Microchips!",
    "Why was the JavaScript developer sad? Because he didn’t ‘null’ his problems.",
    "Why do Python programmers prefer snake_case? Because CamelCase has too many humps!",
    "What do you call a fake noodle? An Impasta!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "What do you call cheese that isn’t yours? Nacho cheese!",
    "Why don’t some couples go to the gym? Because some relationships don’t work out!",
    "Why did the math book look sad? Because it had too many problems.",
    "What do you call a boomerang that doesn’t come back? A stick!",
    "How does a penguin build its house? Igloos it together!",
    "Why did the coffee file a police report? It got mugged!",
    "What do you call an alligator in a vest? An investigator!",
    "Why don’t eggs tell jokes? Because they might crack up!",
    "Why do we never tell secrets on a farm? Because the potatoes have eyes and the corn has ears!"
]
SORRY = "Sorry, I only tell jokes."

# Streamlit UI
st.title("😂 Joke Bot 🤖")
st.subheader("Enter your name and I'll tell you a joke!")

# User Input
user_input = st.text_input(PROMPT)
if user_input:
    st.write(f"Hello {user_input}!")
    st.write("What you want to do?")
# Show Joke & Exit Buttons after user input
if user_input:
    col1, col2 = st.columns(2)  # Creating two buttons side by side
    
    with col1:
        joke_btn = st.button("Tell me a Joke 😂")
    
    with col2:
        exit_btn = st.button("Exit 🚪")

    # Handle Button Clicks
    if joke_btn:
        joke = random.choice(JOKES)  # Get random joke
        st.success(joke)  # Show joke
    
    if exit_btn:
        st.warning(f"Goodbye! 👋 {user_input}")  # Show exit message
        st.stop()  # Stop the app