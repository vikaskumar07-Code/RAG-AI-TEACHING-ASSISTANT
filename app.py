import streamlit as st
from process_incoming import ask_question

st.set_page_config(page_title="ML Teaching Assistant", page_icon="🤖", layout="wide")

# ---------- DARK THEME ----------
st.markdown("""
<style>
body {background-color:#e1e6f4;color:black}
.block-container {max-width:900px;margin:auto}

.user-msg {background:#ebf0fd;padding:12px 16px;border-radius:12px;margin:8px 0;margin-left:120px}
.ai-msg {background:#c7d5f9;padding:12px 16px;border-radius:12px;margin:8px 0;margin-right:120px}

.title-center {text-align:center;font-size:42px;font-weight:700;margin-bottom:20px}

.chat-input {position:fixed;bottom:20px;left:50%;transform:translateX(-50%);width:900px}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-center">🤖 ML Teaching Assistant</div>', unsafe_allow_html=True)

if "chat" not in st.session_state:
    st.session_state.chat = []

# ---------- CHAT HISTORY ----------
for role, msg in st.session_state.chat:
    if role == "user":
        st.markdown(f'<div class="user-msg">{msg}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="ai-msg">{msg}</div>', unsafe_allow_html=True)

# ---------- INPUT BOX CENTER ----------
with st.container():
    user_input = st.chat_input("Ask your ML question...")

if user_input:
    st.session_state.chat.append(("user", user_input))
    answer = ask_question(user_input)
    st.session_state.chat.append(("ai", answer))
    st.rerun()
