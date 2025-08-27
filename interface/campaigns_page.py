import streamlit as st
from classes.campaigns_manager import Campaigns_manager

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

