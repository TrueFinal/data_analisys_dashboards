import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from graph import df_agrupado, df

background = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://img.freepik.com/fotos-gratis/fundo-texturizado-abstrato_1258-30471.jpg");
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
    background-attachment: local;
}}
[data-testid="stHeader"] {{
    background: rgba(0,0,0,0)
}}
</style>
"""

st.set_page_config(
    layout='wide', 
    page_title='Dashboard Vendas Biodiesel - 2017 a 2024',
    page_icon='📊', 
    initial_sidebar_state='collapsed', 
    menu_items={'About': '# This is a project made for my Data *Analysis classes*'}
)

st.markdown(background, unsafe_allow_html=True)

def main():
    st.title("DASH - Acesso a Informações Internas Gráficas - Petrobrás")
    menu = ["Acesso Privilegiado"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Acesso Privilegiado":
        st.sidebar.subheader("Faça login para ter acesso privilegiado")
        username = st.sidebar.text_input("Nome de usuário")
        password = st.sidebar.text_input("Senha de acesso", type="password")
        if st.sidebar.button("Login"):
            if username == "Murillo" and password == "12345":
                opt = ["Vendas", "Tabela Dados Brutos", "Perfil"]
                task = st.selectbox(label='Dashboards', options=opt, key="task_selectbox")
                if task == "Vendas":
                    st.title("Gráficos de Vendas") 
                    st.header("Vendas totais de biodiesel - (2017 - 2024)")
                    fig = px.bar(df_agrupado, x='Ano', y='Vendas de Biodiesel', title="Vendas Biodiesel (Em Bilhões)")
                    st.plotly_chart(fig, use_container_width=True)
                elif task == "Tabela Dados Brutos":
                    st.title('Tabela com os Dados Completos')
                    st.header("Dados Brutos")
                    st.dataframe(df, use_container_width=True)
                elif task == "Perfil":
                    st.title("Perfil (Em construção!)")
            else:
                st.warning("Senha incorreta") 

if __name__ == "__main__":
    main()