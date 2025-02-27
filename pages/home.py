import streamlit as st
import base64


# Function to set a background image and change font color
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    background_style = f"""
        <style>
            .stApp {{
                background: url("data:image/jpg;base64,{encoded_string}") no-repeat center center fixed;
                background-size: cover;
                color: white; /* Changes font color to black */
            }}

            /* Ensures all text elements appear in black */
            h1, h2, h3, h4, h5, h6, p, span, div {{
                color: white !important;
            }}
        </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)


def app():
    # Set background image (Ensure the file exists in the same folder)
    set_background("pexels-pixabay-164501.jpg")

    st.title("🏠 Welcome to the Credit Card Churn Prediction App")

    st.markdown(
        """
        This app helps identify customers who might churn based on key financial indicators.  

        📌 **Scenario:**  
        A bank manager is increasingly concerned about customer churn in their credit card services.  
        Predicting potential churners allows proactive customer engagement, offering better services to retain them.  

        ### **🔹 Key Features:**
        - 📊 **Data-Driven Predictions** – Leverage machine learning to forecast churn.
        - ⚡ **Quick & Interactive Interface** – Seamless user experience.
        - 🔍 **Actionable Customer Insights** – Make informed business decisions.

        🔽 **Use the sidebar to navigate through the app and start predictions!**
        """
    )


