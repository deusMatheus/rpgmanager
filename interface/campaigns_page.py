import streamlit as st
from time import sleep
from classes.campaigns_manager import Campaigns_manager

if 'new_campaign' not in st.session_state:
    st.session_state['new_campaign'] = False

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

else:
    st.write('Você não está participando de nenhuma campanha.')

