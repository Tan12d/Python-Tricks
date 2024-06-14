from google.generativeai import GenerativeModel, configure

configure(api_key="AIzaSyA5Np0yhGKAXsfruPYqs2Ildow9cETk5Do")

model = GenerativeModel("gemini-1.5-pro")

r=model.generate_content("What is Streamlit")

print(r.text)