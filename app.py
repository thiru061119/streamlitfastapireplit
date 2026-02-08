import streamlit as st
import requests
API_URL = "https://your-fastapi-url"
st.title("User Form")

with st.form("user_form"):
    name = st.text_input("Enter name")
    age = st.number_input("Enter age", min_value=0, max_value=120)
    submit = st.form_submit_button("Save")

if submit:
    if name:
        res = requests.post(
            f"{API_URL}/users",
            params={"name": name, "age": age}
        )
        if res.status_code == 200:
            st.success("Saved to Supabase ✅")
        else:
            st.error("Backend error ❌")
    else:
      st.error("Name is required")
  if st.button("Load users"):
    data = requests.get(f"{API_URL}/users").json()
    st.table(data)
