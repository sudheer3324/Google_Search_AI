import streamlit as st

from search_helper import search_web

st.set_page_config(
    page_title="AI Search Assistant",
    page_icon="🔎"
)

st.title("🔎 AI Search Assistant")

question = st.text_input(
    "Ask Anything"
)

if st.button("Search"):

    if question.strip() == "":

        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching Internet..."):

            answer, sources = search_web(question)

        st.header("Answer")

        st.write(answer)

        st.header("Sources")

        for url in sources:

            st.write(url)