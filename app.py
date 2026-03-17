import streamlit as st
from google import genai
from auth import login_user, register_user

# 1. SETUP - Use the 2026 stable model name
# 'gemini-3-flash-preview' or 'gemini-2.5-flash' are your best bets
MODEL_ID = "gemini-3-flash-preview"

st.set_page_config(page_title="AI Interview Pro 2026", layout="centered")

# Authentication check
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.username = None

if "page" not in st.session_state:
    st.session_state.page = "login"

# Login page
if not st.session_state.authenticated:
    if st.session_state.page == "login":
        st.title("🔐 Login")
        with st.form("login_form"):
            username = st.text_input("Username", placeholder="Enter your username")
            password = st.text_input("Password", type="password", placeholder="Enter your password")
            submitted = st.form_submit_button("Login")
            
            if submitted:
                if username and password:
                    success, message = login_user(username, password)
                    if success:
                        st.session_state.authenticated = True
                        st.session_state.username = username
                        st.success("✅ Login successful!")
                        st.rerun()
                    else:
                        st.error(message)
                else:
                    st.error("Please fill in all fields")
        
        st.divider()
        if st.button("📝 Create Account", use_container_width=True):
            st.session_state.page = "register"
            st.rerun()
    
    elif st.session_state.page == "register":
        st.title("📝 Create Account")
        with st.form("register_form"):
            username = st.text_input("Username", placeholder="Choose a username")
            email = st.text_input("Email", placeholder="Enter your email")
            password = st.text_input("Password", type="password", placeholder="Create a password (min 6 chars)")
            password_confirm = st.text_input("Confirm Password", type="password", placeholder="Confirm your password")
            submitted = st.form_submit_button("Register")
            
            if submitted:
                if not all([username, email, password, password_confirm]):
                    st.error("Please fill in all fields")
                elif password != password_confirm:
                    st.error("Passwords do not match")
                else:
                    success, message = register_user(username, password, email)
                    if success:
                        st.success("✅ Account created! Redirecting to login...")
                        st.session_state.page = "login"
                        st.rerun()
                    else:
                        st.error(message)
        
        st.divider()
        if st.button("🔐 Back to Login", use_container_width=True):
            st.session_state.page = "login"
            st.rerun()
    
    st.stop()

st.title("🤖 AI Interview Practice System")

# 2. API KEY - Paste your key here
API_KEY = "AIzaSyDDM53Wo7JqE1UsprB6zXe4i9aeF-hp9ik"

# Initialize the new Client
client = genai.Client(api_key=API_KEY)

# Session state to keep the conversation going
if "question" not in st.session_state:
    st.session_state.question = ""

# Sidebar for Job Role and User Info
with st.sidebar:
    st.write(f"👤 Logged in as: **{st.session_state.username}**")
    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.authenticated = False
        st.session_state.username = None
        st.rerun()
    st.divider()

role = st.sidebar.text_input("Target Job Role:", placeholder="e.g. Java Developer")

if st.sidebar.button("Generate New Question"):
    if role:
        with st.spinner("Generating..."):
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=f"Act as a technical interviewer. Ask one challenging question for a {role} role."
            )
            st.session_state.question = response.text
    else:
        st.sidebar.warning("Enter a role first!")

# Main UI
if st.session_state.question:
    st.info(f"**Question:**\n{st.session_state.question}")
    
    user_answer = st.text_area("Your Answer:", height=150)
    
    if st.button("Submit for AI Feedback"):
        with st.spinner("Analyzing..."):
            feedback_prompt = f"""
            Question: {st.session_state.question}
            User Answer: {user_answer}
            Evaluate this answer for a {role} position. Provide a score/10 and improvement tips.
            """
            feedback = client.models.generate_content(model=MODEL_ID, contents=feedback_prompt)
            st.success("Analysis Complete!")
            st.markdown(feedback.text)
else:
    st.write("👈 Use the sidebar to generate your first interview question!")