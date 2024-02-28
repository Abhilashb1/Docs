import streamlit as st

# Function to generate response based on user input
def generate_response(question, prev_answer):
    if question.lower() == 'what is your name?':
        return "My name is ChatBot."
    elif question.lower() == 'how old are you?':
        return "I am just a program, so I don't have an age."
    elif question.lower() == 'what can you do?':
        if prev_answer.lower() == "chatbot":
            return "I can chat with you!"
        elif prev_answer.lower() == "program":
            return "I can help you with programming tasks."
        else:
            return "I can answer questions and assist you with tasks!"
    else:
        return "I'm sorry, I don't know the answer to that question."

# Streamlit app
def main():
    st.title("Interactive Q&A with ChatBot")

    # Ask the first question
    question1 = st.text_input("Question 1:", "What is your name?")

    # Generate response for the first question
    response1 = generate_response("What is your name?", question1)

    # Display response for the first question
    st.message("ChatBot:", response1)

    # Ask the second question based on the answer to the first question
    if question1.lower() == "chatbot" or question1.lower() == "program":
        question2 = st.text_input("Question 2:", "How old are you?")

        # Generate response for the second question
        response2 = generate_response("How old are you?", question2)

        # Display response for the second question
        st.message("ChatBot:", response2)

        # Display download button
        st.download_button("Download Data", "data.csv", label="Click here to download data")

    # Ask the third question
    question3 = st.text_input("Question 3:", "What can you do?")

    # Generate response for the third question
    response3 = generate_response("What can you do?", question3)

    # Display response for the third question
    st.message("ChatBot:", response3)

if __name__ == "__main__":
    main()
