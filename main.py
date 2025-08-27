import streamlit as st

if 'login_status' not in st.session_state:
    st.session_state['login_status'] = False

if 'user' not in st.session_state:
    st.session_state['user'] = ''

if 'username' not in st.session_state:
    st.session_state['username'] = ''

if 'type' not in st.session_state:
    st.session_state['type'] = ''

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
#        st.write(st.session_state['type'])
#        print(st.session_state['type'])
        if(st.session_state['type'] == 'player'):
            pages = [st.Page('interface/main_page.py', title='Página principal'),
                     st.Page('interface/campaigns_page.py', title='Campanhas'),
                     st.Page('interface/players_page.py', title='Página do jogador')]

        elif(st.session_state['type'] == 'player&dm'):
            pages = [st.Page('interface/main_page.py', title='Página principal'),
                     st.Page('interface/campaigns_page.py', title='Campanhas'),
                     st.Page('interface/players_page.py', title='Página do jogador')]

        else:
            pages = [st.Page('interface/main_page.py', title='Página principal'),
                    st.Page('interface/campaigns_page.py', title='Campanhas')]

    pg = st.navigation(pages)
    pg.run()

if __name__ == '__main__':
    main()