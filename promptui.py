import streamlit as st

# Set up Streamlit configuration
st.set_page_config(
    page_title="Client Project",
    page_icon=":bar_chart:",
    layout="wide"
)

# Define CSS styles
main_bg = "background-color: #f0f5f9;"
sidebar_bg = "background-color: #192b3b;"

# Apply CSS styles
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

    body {{
        font-family: 'Roboto', sans-serif;
    }}

    .reportview-container {{
        {main_bg}
    }}

    .sidebar .sidebar-content {{
        {sidebar_bg}
    }}

    .css-1p3jvgu, .css-dq8hqf, .css-1n2y7ln {{
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin-bottom: 10px;
        padding: 10px;
    }}

    .css-1p3jvgu {{
        background-color: #f0f5f9;
        color: #000000;
    }}

    .css-dq8hqf {{
        background-color: #ffddc1;
        color: #192b3b;
    }}

    .css-1n2y7ln {{
        background-color: #192b3b;
        color: #ffffff;
    }}

    .stButton button:first-child {{
        border-radius: 10px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Persona Input Section
st.sidebar.header("Persona Input")
Persona = st.sidebar.text_area("Persona")

# Submit and Clear Buttons
col1, col2 = st.sidebar.columns(2)
with col1:
    if st.button("Submit"):
        # Placeholder for the submit button logic
        pass
with col2:
    if st.button("Clear"):
        Persona = ""

# Prompt Output Section
st.sidebar.header("Prompt Output")
prompt = st.sidebar.text_area("Prompt")

# OpenAI Response Section
st.header("OpenAI Response")
response = st.empty()

# Dataset Upload Section
st.header("Dataset Upload")
uploaded_file = st.file_uploader("Upload Dataset", type=["csv", "txt"])

# Display the generated response
if st.button("Generate Response"):
    # Placeholder for the response generation logic
    generated_response = "This is a sample response."
    response.markdown(f"> {generated_response}")
