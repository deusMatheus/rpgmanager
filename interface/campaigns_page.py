import streamlit as st
from classes.campaigns_manager import Campaigns_manager

st.title('Campanhas')
campaigns = Campaigns_manager().list_campaigns()
titles = []
for campaign in campaigns:
    titles.append(campaign['title'])

tabs = st.tabs(titles)

for i in range (len(tabs)):
    with tabs[i]:
        st.write(f"Descrição: {campaigns[i]['description']}")
        st.write(f"Link: {campaigns[i]['url']}")
        st.write(f"DM: {campaigns[i]['dm']}")
        st.write(f"Jogadores: {campaigns[i]['players']}")
        st.write(f"Personagens: {campaigns[i]['characters']}")
        st.write(f"Posts: {campaigns[i]['posts']}")
        st.write(f"Itens mágicos: {campaigns[i]['magic_items']}")
        st.write(f"Status: {campaigns[i]['status']}")