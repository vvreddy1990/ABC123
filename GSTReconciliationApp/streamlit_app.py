import sys
import os
import streamlit as st

# Ensure the current directory is in sys.path for module imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    import app
    # If app.py uses __name__ == "__main__" for initialization, call it explicitly
    if hasattr(app, 'initialize_session_state'):
        app.initialize_session_state()
except Exception as e:
    st.error(f"An error occurred while running the app: {e}")
    import traceback
    st.exception(e)
