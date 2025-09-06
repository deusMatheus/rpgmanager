import streamlit as st
from time import sleep
from classes.campaigns_manager import Campaigns_manager
from classes.players_manager import Players_manager

if 'new_campaign' not in st.session_state:
    st.session_state['new_campaign'] = False

if 'add_player' not in st.session_state:
    st.session_state['add_player'] = False

if 'add_select_player' not in st.session_state:
    st.session_state['add_selected_player'] = False

if 'add_character' not in st.session_state:
    st.session_state['add_character'] = False

if 'add_selected_character' not in st.session_state:
    st.session_state['add_selected_character'] = False

st.title('Campanhas')
campaigns = Campaigns_manager().list_campaigns()
titles = []
fullList = []
for campaign in campaigns:
    fullList.append(campaign['title'])
    if(st.session_state['user'] in campaign['players'] or st.session_state['user'] in campaign['dm']):
        titles.append(campaign['title'])

st.subheader('Lista completa de campanhas:')
listString = ''
for title in fullList:
    listString += title + ', '
st.write(listString[:-2])

if(st.session_state['type'] == 'dm' or st.session_state['type'] == 'player&dm'):
    create_campaign_button = st.button('Criar nova campanha')
else:
    create_campaign_button = False

if(create_campaign_button):
    st.session_state['new_campaign'] = True

if(st.session_state['new_campaign']):
    with st.form('register_new_campaign'):
        new_campaign_title = st.text_input('Título')
        new_campaign_description = st.text_area('Descrição')
        
        save_campaign_button = st.form_submit_button(label='Registrar campanha')

        if(save_campaign_button):
            if(not new_campaign_title or not new_campaign_description):
                st.warning('Há campos em branco! Revise antes de registrar a campanha!!')
            else:
                st.session_state['new_campaign'] = False
                Campaigns_manager().new_campaign(new_campaign_title, new_campaign_description)
                st.toast(f'Campanha {new_campaign_title} criada com sucesso!')
                st.toast('Aguarde...')
                sleep(2)
                st.switch_page('interface/campaigns_page.py')

st.subheader('Campanhas que você participa:')
if(titles):
    tabs = st.tabs(titles)

    for i in range (len(tabs)):
        for j in range(len(fullList)):
            if(titles[i]==fullList[j]):
                with tabs[i]:
                    st.write(f"Descrição: {campaigns[j]['description']}")
                    st.write(f"Link: {campaigns[j]['url']}")
                    st.write(f"DM: {campaigns[j]['dm']}")
                    st.write(f"Jogadores: {campaigns[j]['players']}")
                    st.write(f"Personagens: {campaigns[j]['characters']}")
                    st.write(f"Posts: {campaigns[j]['posts']}")
                    st.write(f"Itens mágicos: {campaigns[j]['magic_items']}")
                    st.write(f"Status: {campaigns[j]['status']}")
                    if(st.session_state['type'] == 'player' or st.session_state['type'] == 'player&dm'):
                        add_character = st.button('Adicionar personagem', key=f'add_char_to_{campaigns[j]['title']}')
                        if(add_character):
                            st.session_state['add_character'] = True
                        if(st.session_state['add_character']):
                            full_characters_list = Players_manager().list_characters()
                            characters_names_list = []
                            for character in full_characters_list:
                                characters_names_list.append(character[1])
                            selected_char_to_add = st.selectbox('Selecione um personagem', characters_names_list, key=F'char_to_{campaigns[j]['title']}')
                            if(selected_char_to_add in campaigns[j]['characters']):
                                st.warning('Este personagem já participa desta campanha!')
                            else:
                                add_selected_char = st.button(f'Adicionar {selected_char_to_add} à {campaigns[j]['title']}')
                                if(add_selected_char and not st.session_state['add_selected_character']):
                                    st.session_state['add_selected_character'] = True
                                if(st.session_state['add_selected_character']):
                                    st.session_state['add_character'] = False
                                    st.session_state['add_selected_character'] = False
                                    Campaigns_manager().add_character(selected_char_to_add, campaigns[j]['title'])
                                    st.toast(f'Personagem {selected_char_to_add} adicionado à {titles[i]} com sucesso!')
                                    st.toast('Aguarde...')
                                    sleep(2)
                                    st.switch_page('interface/campaigns_page.py')

                    if(campaigns[j]['dm'] == st.session_state['user']):
                        add_players = st.button('Adicionar jogador', key=titles[i])
                        if(add_players):
                            st.session_state['add_player'] = True
                        if(st.session_state['add_player']):
                            players_list = Players_manager().list_players()
                            selected_player_to_add = st.selectbox('Selecione um jogador', players_list, key='player_to_add')
                            if(selected_player_to_add in campaigns[j]['players']):
                                st.warning('Este jogador já participa desta campanha!')
                            if(selected_player_to_add in campaigns[j]['dm']):
                                st.warning('Este é o DM desta campanha!')
                            else:
                                add_selected_player = st.button('Adicionar jogador à campanha')
                                if(add_selected_player and not st.session_state['add_selected_player']):
                                    st.session_state['add_selected_player'] = True
                                if(st.session_state['add_selected_player']):
                                    Campaigns_manager().add_player(selected_player_to_add, titles[i])
                                    st.toast(f'Jogador {selected_player_to_add} adicionado à {titles[i]} com sucesso!')
                                    st.toast('Aguarde...')
                                    sleep(5)
                                    st.session_state['add_player'] = False
                                    st.session_state['add_selected_player'] = False
                                    st.switch_page('interface/campaigns_page.py')


else:
    st.write('Você não está participando de nenhuma campanha.')

