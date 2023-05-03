import streamlit as st

st.set_page_config(page_title = "Song Recommender")

st.title("Welcome. :wave:")
st.sidebar.success("Select a page above.")

"""Hello there!  This app is a music recommendation service that takes into account your taste, mood, and emotion. As a user, you get to 
choose two different modes, one is through a chatbot and the other is through facial emotion detection. Enjoy!"""

"""Please leave us a feedback so that we can improve your experience."""

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Give your feedback", st.session_state["my_input"])
submit = st.button("Submit")

if submit:
    st.session_state["my_input"] = my_input
    st.write("Thank you for your feedback! Excited for your next visit!")