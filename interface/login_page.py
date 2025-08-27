import streamlit as st
from classes.login_manager import Login_manager
from classes.users_manager import Users_manager

placeholder = st.empty()

with placeholder.form('login', clear_on_submit=True, border=False):
    
    if(not st.session_state['login_status']):
        st.markdown(f"""
            <div style='margin-left: 1.15em; margin-top:1em;'>
                <h1>Login page</h1>
            </div>
        """, unsafe_allow_html=True)

        username = st.text_input('Nome de usuário')
        password = st.text_input('Senha', type='password')
        submitButton = st.form_submit_button('Acessar')

        if(submitButton and not Login_manager().checkUser(username, password)):
            st.write('Usuário ou senha incorretos.')
            submitButton = False

        elif(submitButton and Login_manager().checkUser(username, password)):
            st.session_state['login_status'] = True
            st.session_state['username'] = username
            st.session_state['user'] = Users_manager().get_user_name(username)
            st.session_state['type'] = Users_manager().get_type(username)
            st.rerun()

    else:
        st.write('Retorne à página inicial.')
        st.switch_page('interface/main_page.py')