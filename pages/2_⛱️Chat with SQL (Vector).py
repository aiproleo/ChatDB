from app.utils import streamlit_components,streamlit_docs

streamlit_components.streamlit_ui('🦣 PostgreSQL')
streamlit_docs.postgre_intro()
# -----------------------------------------------------------------------------------------------------------
from app import (
    chat_ui_vector,
    db_handler,
    llm_vector_handler
)


if __name__ == "__main__":
    
    db_handler = db_handler.DatabaseHandler()   # init: session_state add uri, with save() get unique_id.
    llm_vector_handler = llm_vector_handler.LLMVectorHandler()      # Initialize the language model handler with the OpenAI API key
    
    app = chat_ui_vector.ChatUI(db_handler, llm_vector_handler, 'vector')   # Create an instance of the Streamlit UI and pass the handlers to it
    app.run()   # Run the Streamlit application
