import streamlit as st
import requests

st.title("Book Recommendation")

query = st.text_input("Enter your search")
topk = st.slider("Number of recommendations", 1, 10, 3)
 
if st.button("Search"):
    response = requests.post(
        "http://127.0.0.1:8000/query",
        json={
            "text": query,
            "topk": topk
        }
    )

    if response.status_code == 200:
        data = response.json()
        st.write(f"## Recommendations for '{query}':")
        for rec in data["recommendations"]:
            st.write(f"{rec['Title']} by {rec['Author']} - Rating: {rec['Rating']}")
    else:
        st.error("Error: " + response.text)

