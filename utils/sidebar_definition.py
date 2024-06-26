import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

   
def st_logo(main_title):
    st.set_page_config(page_title='AI SQL Linguist 👋',  page_icon="🚀",),
    st.title(main_title)        # not accepting default

    st.markdown("""
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://omnidevx.netlify.app/logo/aipro.png);
                background-size: 300px; /* Set the width and height of the image */
                background-repeat: no-repeat;
                padding-top: 80px;
                background-position: 15px 10px;
            }
        </style>
        """,
    unsafe_allow_html=True,
    )



def st_sidebar():
    with st.sidebar:
        # store_link = st.text_input("Enter Your Store URL:",   value="http://hypech.com/StoreSpark", disabled=True, key="store_link")
        openai_api_key = st.text_input("OpenAI API Key (gpt-4)", key="chatbot_api_key", type="password")
        st.write("[Get an OpenAI API key](https://platform.openai.com/account/api-keys)")
        add_vertical_space(2)
        st.write('Made with ❤️ by [aiProLeo]')
    return openai_api_key
