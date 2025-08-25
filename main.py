import streamlit as st

if 'login_status' not in st.session_state:
    st.session_state['login_status'] = False

if 'user' not in st.session_state:
    st.session_state['user'] = ''

def main():

    if(not st.session_state['login_status']):
        pages = [st.Page('interface/login_page.py',title='Login')]

    if(st.session_state['login_status']):
        st.markdown(f"""
            <div style='margin-left: 1.05em;'>
                <h1>RPG Manager</h1>
                <p>Bem-vindo: {st.session_state['user']}</p>
            </div>
        """, unsafe_allow_html=True)
        pages = [st.Page('interface/main_page.py', title='Página principal'),
                 st.Page('interface/campaigns_page.py', title='Campanhas')]

    pg = st.navigation(pages)
    pg.run()

if __name__ == '__main__':
    main()