import streamlit as st
from time import sleep
from classes.login_manager import Login_manager
from classes.users_manager import Users_manager
from classes.email_manager import Email

if 'register_status' not in st.session_state:
    st.session_state['register_status'] = 'not_registered'

if 'name_to_register' not in st.session_state:
    st.session_state['name_to_register'] = ''

if 'user_to_register' not in st.session_state:
    st.session_state['user_to_register'] = ''

if 'pass_to_register' not in st.session_state:
    st.session_state['pass_to_register'] = ''

if 'email_to_register' not in st.session_state:
    st.session_state['email_to_register'] = ''

if 'email_sent' not in st.session_state:
    st.session_state['email_sent'] = False

st.markdown(f"""
    <div style='margin-left: 1.15em; margin-top:1em;'>
        <h1>Cadastrar novo usuário</h1>
    </div>
""", unsafe_allow_html=True)

if(not st.session_state['login_status'] and st.session_state['register_status'] == 'not_registered'):
    newName = st.text_input('Nome')
    newUsername = st.text_input('Nome de usuário')
    if(Users_manager().check_username_availability(newUsername)):
        st.warning('Este nome de usuário não está disponível!')
    newEmail = st.text_input('E-mail')
    newPassword = st.text_input('Senha', type='password')
    confirmPassword = st.text_input('Confirme sua senha', type='password')
    if(newPassword != confirmPassword):
        st.warning('As senhas não conferem!')
    if(not Users_manager().check_username_availability(newUsername) and newPassword == confirmPassword and newUsername and newPassword and newName):
        submitButton = st.button('Cadastrar novo usuário')
        if(submitButton):
            st.session_state['register_status'] = 'register_started'
            if(not st.session_state['user_to_register']):
                st.session_state['name_to_register'] = newName
                st.session_state['user_to_register'] = newUsername
                st.session_state['pass_to_register'] = newPassword
                st.session_state['email_to_register'] = newEmail
            st.switch_page('interface/register.py')

#    if(submitButton and not Login_manager().checkUser(username, password)):
#        st.write('Usuário ou senha incorretos.')
#        submitButton = False
#
#    elif(submitButton and Login_manager().checkUser(username, password)):
#        st.session_state['login_status'] = True
#        st.session_state['username'] = username
#        st.session_state['user'] = Users_manager().get_user_name(username)
#        st.session_state['type'] = Users_manager().get_type(username)
#        st.rerun()

elif(not st.session_state['login_status'] and st.session_state['register_status'] == 'register_started'):
    if not st.session_state['email_sent']:
        Users_manager().register_new_user(st.session_state['name_to_register'],st.session_state['user_to_register'],st.session_state['email_to_register'])
        st.session_state['email_sent'] = True

    st.write(f'Um e-mail foi enviado para {st.session_state['email_to_register']}. Verifique sua caixa de entrada e insira abaixo o código informado!')
    informedOTP = st.text_input('Insira o código recebido por email')
    if informedOTP != '':
        try:
            informedOTP = int(informedOTP)
        except ValueError:
            st.warning('Você precisa digitar um número!')

    if(st.session_state['register_status'] == 'register_started'):
        finish_register = st.button('Finalizar cadastro')
        if(finish_register):
            st.session_state['register_status'] = 'register_checking'

    if(st.session_state['register_status'] == 'register_checking'):
        if(Users_manager().check_otp(st.session_state['name_to_register'],st.session_state['user_to_register'],st.session_state['pass_to_register'],st.session_state['email_to_register'],informedOTP)):
            st.session_state['register_status'] = 'register_finished'
            st.switch_page('interface/register.py')
        else:
            st.toast('O código informado é inválido.')
            st.session_state['register_status'] = 'register_started'

elif(not st.session_state['login_status'] and st.session_state['register_status'] == 'register_finished'):
    st.toast('Seu cadastro foi concluído com sucesso.')
    st.toast('Aguarde, você será redirecionado para a página de login.')
    sleep(5)
    st.switch_page('interface/login_page.py')

else:
    st.write('Retorne à página inicial.')
    st.switch_page('interface/login_page.py')
