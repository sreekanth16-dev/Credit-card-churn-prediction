import streamlit as st



import home, prediction,about

# st.set_page_config(
#     page_title="Pondering",
# )

st.markdown(
    """
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src=f"https://www.googletagmanager.com/gtag/js?id={os.getenv('analytics_tag')}"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', os.getenv('analytics_tag'));
        </script>
        
    """, unsafe_allow_html=True)
st.markdown("""
    <style>
        /* Customize the sidebar background and text */
        .sidebar .sidebar-content {
            background-color: #2E3B55;  /* Dark Blue Background */
            color: #FFFFFF;  /* White Text */
            font-family: 'Arial', sans-serif;
            padding-top: 30px;  /* Add padding to the top */
        }

        /* Sidebar title */
        .sidebar .sidebar-title {
            font-size: 20px;
            font-weight: bold;
            color: #FFD700;  /* Gold color for title */
            margin-bottom: 20px;
        }

        /* Make the sidebar radio buttons larger */
        .st-radio label {
            font-size: 18px;
            font-weight: bold;
            color: #FFFFFF;  /* White Text */
        }

        .st-radio label:hover {
            color: #FFD700;  /* Gold text when hovered */
        }

        /* Hover effect on sidebar radio buttons */
        .stRadio .st-bc {
            background-color: #1E2A3B;  /* Darker blue when hovered */
        }

        /* Customize the sidebar's hover effect on selected option */
        .stRadio .st-bc:hover {
            background-color: #FFD700;  /* Gold background when hovered */
            color: #2E3B55;  /* Dark blue text when hovered */
        }
    </style>
""", unsafe_allow_html=True)




class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        st.sidebar.title("Navigation")
        app = st.sidebar.radio("Go to", ("Home", "Prediction", "About"))
        # app = st.sidebar(


        if app == "Home":
            home.app()
        if app == "Prediction":
            prediction.app()
        if app == "About":
            about.app()


    run()

