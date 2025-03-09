import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="EliteBot", page_icon="🤖")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False


def authenticate(password):
    st.title("🔒 Enter Password")
    col1, col2 = st.columns([10, 1])
    with col1:
        code_input = st.text_input(
            "Enter Secret Code:", label_visibility="collapsed", type="password"
        )
    with col2:
        if st.button("🔓", type="primary"):
            if code_input == password:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.toast("Incorrect password!", icon="❌")


if not st.session_state.authenticated:
    authenticate(password=st.secrets.SECRET_CODE)

else:
    genai.configure(api_key=st.secrets.API_KEY)
    model = genai.GenerativeModel("gemini-2.0-flash")

    st.title(":red[🤖 EliteBot]")
    st.subheader("Welcome to the Gemini-powered AI Chatbot!")

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Display chat history
    for msg in st.session_state["messages"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if user_input := st.chat_input("Type your message..."):
        st.session_state["messages"].append({"role": "user", "content": user_input})

        with st.chat_message("user"):
            st.markdown(user_input)

        try:
            response = model.generate_content(user_input)
            bot_response = response.text
        except Exception:
            bot_response = "⚠️ Error: Unable to generate response."

        st.session_state["messages"].append(
            {"role": "assistant", "content": bot_response}
        )

        with st.chat_message("assistant"):
            st.markdown(bot_response)
