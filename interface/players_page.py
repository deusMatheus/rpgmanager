import streamlit as st
from time import sleep
from classes.players_manager import Players_manager

if 'new_char' not in st.session_state:
    st.session_state['new_char'] = False

st.title('Seus personagens')
characters = Players_manager().get_characters(st.session_state['username'])
names = []
if(len(characters)>1):
    for character in characters:
        names.append(character['name'])

elif(len(characters) == 1):
    names.append(characters[0]['name'])

create_character_button = st.button('Criar novo personagem')

if(create_character_button):
    st.session_state['new_char'] = True

if(st.session_state['new_char']):
    with st.form('register_new_character'):
        new_char_name = st.text_input('Nome')
        new_char_origin = st.text_input('Origem')
        new_char_class = st.text_input('Classe')
        new_char_archetype = st.text_input('Arquétipo')
        new_char_level = st.text_input('Nível')
        new_char_xp = st.text_input('Exp')
        new_char_gold = st.text_input('Gold')

        save_character_button = st.form_submit_button(label='Registrar')

        if(save_character_button):
            if(not new_char_name or not new_char_origin or not new_char_class or not new_char_archetype or not new_char_level or not new_char_xp or not new_char_gold):
                st.warning('Há campos em branco! Revise antes de registrar o personagem!!')
            else:
                st.session_state['new_char'] = False
                Players_manager().new_character(new_char_name, new_char_origin, new_char_class, new_char_archetype, new_char_level, new_char_xp, new_char_gold)
                st.toast(f'Personagem {new_char_name} criado com sucesso!')
                st.toast('Aguarde...')
                sleep(2)
                st.switch_page('interface/players_page.py')

if(names):
    tabs = st.tabs(names)

    if(len(tabs) >= 1):
        for i in range(len(tabs)):
            with tabs[i]:
#                st.write(f"Nome: {characters[i]['name']}")
                st.write(f"Classe: {characters[i]['class']}")
                st.write(f"Arquétipo: {characters[i]['archetype']}")
                st.write(f"Origem: {characters[i]['origin']}")
                st.write(f"Nível: {characters[i]['level']}")
                st.write(f"Exp: {characters[i]['exp']}")
                st.write(f"Gold: {characters[i]['gold']}")

else:
    st.write('Você não possui personagens cadastrados.')