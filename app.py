import streamlit as st
from search_helper import search_web

st.set_page_config(
    page_title="AI Search Assistant",
    page_icon="🔎",
    layout="wide"
)

st.title("🔎 AI Search Assistant")

question = st.text_input("Ask Anything")

if st.button("Search"):

    if not question.strip():
        st.warning("Please enter a question.")

    else:
        with st.spinner("Searching the Internet..."):

            answer, sources = search_web(question)

        st.subheader("Answer")
        st.write(answer)

        if sources:
            st.subheader("Sources")

            for source in sources:
                st.write(source)
