import streamlit as st

# Create a state dictionary to store user responses
state = st.session_state

def ask_questions():
  """Asks four questions and stores responses in the state dictionary."""

  # Question 1
  question1 = "What is your name?"
  if "name" not in state:
    state["name"] = st.text_input(question1)

  # Question 2
  question2 = "What is your favorite color?"
  if "favorite_color" not in state:
    state["favorite_color"] = st.selectbox(question2, ["Red", "Green", "Blue", "Other"])

  # Question 3 (multiple choice)
  question3 = "Which programming languages do you know?"
  if "languages" not in state:
    options = ["Python", "Java", "JavaScript", "C++", "None"]
    state["languages"] = st.multiselect(question3, options)

  # Question 4 (open-ended)
  question4 = "Tell me about your favorite hobby."
  if "hobby" not in state:
    state["hobby"] = st.text_area(question4)

# Display the questions dynamically
ask_questions()

# Display the collected responses
st.write("**Your name:**", state.get("name", ""))
st.write("**Favorite color:**", state.get("favorite_color", ""))
st.write("**Programming languages known:**", state.get("languages", []))
st.write("**Favorite hobby:**", state.get("hobby", ""))
