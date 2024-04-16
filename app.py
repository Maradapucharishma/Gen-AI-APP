from openai import OpenAI
import streamlit as st

# Read the API key and setup an OpenAI client
with open(r"C:\\Users\\CHARISHMA\\Documents\\Internship\\Backend\\Genai_App\\practice_API_key.txt") as f:
    openai_api_key = f.read()

st.markdown("<h1 style='color:teal;'>GenAI App - AI Code Reviewer</h1>", unsafe_allow_html=True)
st.subheader("📝AI Code Reviewer")

client = OpenAI(api_key=openai_api_key)

# Take user's input
prompt = st.text_area("Enter your code here....", height=100)

# If button is clicked, generate responses
if st.button("Get Review"):
    st.markdown("<h2 style='color:black;'>Review:</h2>", unsafe_allow_html=True)

    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful AI Assistant. Given a Python code snippet, you will review it for potential bugs and suggest fixes."},
            {"role": "user", "content": prompt}
        ]
    )

    # Display corrected code
    corrected_code = response.choices[0].message.content
    st.markdown("<h3 style='color:green;font-size:20px;'>Explanation:</h3>", unsafe_allow_html=True)
    st.write(response.choices[0].message.content)
    