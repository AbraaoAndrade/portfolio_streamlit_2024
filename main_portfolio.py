import sys
sys.path.append("code")
sys.path.append("data")

import streamlit as st
import streamlit.components.v1 as components
from presentation_card import presentation_card
from portfolio_carousel import portfolio_carousel
from PIL import Image
import os
import time

from utils import *

st.set_page_config(page_title="Portfolio",
                    page_icon=":snake:",
                    layout="centered",
                    initial_sidebar_state="auto")

img_head = "https://raw.githubusercontent.com/AbraaoAndrade/portfolio_streamlit_sharing/main/images/head.png"
  
title = "Work"     
subtitle =  '''Check my commercioal and non commercial projects.
            If you have any questions feel free to ask me for more information'''
cards = [["https://raw.githubusercontent.com/AbraaoAndrade/portfolio_streamlit_sharing/main/images/zenk.jpg", "ZENK project", "Web Scraping | RPA | Data Anlysis", "https://egr1project.streamlit.app", "A formação da memória requer a expressão gênica induzida pela atividade neuronal. Esta resposta inclui uma série de genes dependentes de atividade tidos como mediadores das mudanças necessárias para a consolidação e manutenção da memória."],
        ["https://raw.githubusercontent.com/AbraaoAndrade/portfolio_streamlit_sharing/main/images/b2b.jpg", "Prospecção de Clientes B2B", "Google API | Python | Streamlit", "https://b2bprospection.streamlit.app" ,"Aplicação para prospectar potenciais clientes B2B no Rio Grande do Norte utilizando uma API da Google chamada Places."],
        ["https://raw.githubusercontent.com/AbraaoAndrade/portfolio_streamlit_sharing/main/images/tracking.jpg", "Bird Tracking", "Data Processing | Data Visualization", "https://birdtracking.streamlit.app" ,"Aplicação para processar dados de coordenadas e gerar visualizações em mapa de calor."]]

t0 = time.time()    

st.markdown("""
    <style>
        .stProgress > div > div > div > div {
            background-color: #6BA967;
        }
    </style>
    """, unsafe_allow_html=True)

title_html = "<h1 style='text-align: center; color: black; font-size: 38.5px;'>{}</h1>"

def trigger_download_1(data, filename) -> str:
    import base64
    b64 = base64.b64encode(data).decode()
    dl_link = f"""
                <html>
                <head>
                <script src="http://code.jquery.com/jquery-3.2.1.min.js"></script>
                <script>
                $('<a href="data:application/octet-stream;base64,{b64}" download="{filename}">')[0].click()
                </script>
                </head>
                </html>"""
    return dl_link

def download_cv_1() -> None:
    import streamlit.components.v1 as components

    with open("./data/CV_abraao_andrade_2024.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    trigger = trigger_download_1(PDFbyte, "abraao_andrade_cv_2024.pdf")
    components.html(html=trigger, height=0, width=0)
    return

def main():

    st.image(img_head, use_column_width=True)

    # PRESENTATION ==========================================================================================================================================================================
    value_presentation = presentation_card(image_path= "https://raw.githubusercontent.com/AbraaoAndrade/portfolio_streamlit_sharing/main/images/lowquality_fotominha.jpg", #"https://raw.githubusercontent.com/AbraaoAndrade/portfolio_streamlit_sharing/main/images/profile.png",
                              name="Abraão Andrade",
                              post="Cientista de Dados",
                              description= " 3+ anos de experiência no desenvolvimento de soluções orientadas a dados tanto na Ciência quanto no Mercado. Graduando em Engenharia Biomédica ...")
                              # do Cérebro - UFRN e Estagiário em Análise de Dados e Automação de Processos no Supermercado Nordestão

    # WORKS =================================================================================================================================================================================
    value = portfolio_carousel(title=title,
                               subtitle=subtitle,
                               cards=cards)

    st.markdown("")
    st.markdown("")

    # SKILLS ================================================================================================================================================================================
    
    st.markdown(title_html.format("Skills"), unsafe_allow_html=True)
    skills_html = "<h1 style='text-align: left; vertical-align:center; color: black; font-size: 18px;'>{} </h1> "
    certif_html = "[![Title](https://img.icons8.com/ios/20/null/contract.png)]({})"

    c1, c2, c3, c4 = st.columns([1.2,5.3,2.8,3.7])
    with c1:
        st.markdown(skills_html.format("Python"), unsafe_allow_html=True)
    with c2:
        st.markdown(certif_html.format("https://cursos.alura.com.br/degree/certificate/0a535bf8-daa3-4635-881a-f924c83234cf"))
    with c3:
        st.markdown(skills_html.format("Machine Learning"), unsafe_allow_html=True)
    with c4:
        st.markdown(certif_html.format("https://cursos.alura.com.br/degree/certificate/7bd69ec2-0d21-4e09-be74-425e1596791c"))
        
    c1, c2 = st.columns(2)
    with c1:
        st.progress(90)
    with c2:
        st.progress(75)

    c1, c2, c3, c4 = st.columns([0.7,5.8,2.1,4.4])
    with c1:
        st.markdown(skills_html.format("SQL"), unsafe_allow_html=True)
    with c2:
        st.markdown(certif_html.format("https://www.hackerrank.com/certificates/66f76a5b4418"))
    with c3:
        st.markdown(skills_html.format("Data Science"), unsafe_allow_html=True)
    with c4:
        st.markdown(certif_html.format("https://cursos.alura.com.br/degree/certificate/87387e7f-30c2-4189-ad49-3f0872f00a3c"))
        
    c1, c2 = st.columns(2)
    with c1:
        st.progress(65)
    with c2:
        st.progress(90)

    c1, c2, c3, c4 = st.columns([1.6,4.9,3,3.5])
    with c1:
        st.markdown(skills_html.format("Estatística"), unsafe_allow_html=True)
    with c2:
        st.markdown(certif_html.format("https://cursos.alura.com.br/degree/certificate/2b19cad3-b2c3-458d-bef7-dd0a64742551"))
    with c3:
        st.markdown(skills_html.format("Data Visualization"), unsafe_allow_html=True)
        
    c1, c2 = st.columns(2)
    with c1:
        st.progress(75)
    with c2:
        st.progress(85)

    st.markdown("")
    st.markdown("")

    # CONTACT ===============================================================================================================================================================================
    st.markdown(title_html.format("Contact"), unsafe_allow_html=True)

    with st.form("email_form", clear_on_submit=False):
        fullname = st.text_input(label="Nome Completo", placeholder="Digite seu nome completo")
        email = st.text_input(label="Email", placeholder="Digite seu email")
        text = st.text_area(label="Texto", placeholder="Digite sua mensagem aqui")

        submitted = st.form_submit_button("Enviar")

    if submitted:
        extra_info = """
        ---------------------------------------------------------------------------- \n
         Email Address of Sender: {} 
         Sender Full Name: {} \n
        ---------------------------------------------------------------------------- \n \n
        """.format(email, fullname)

        message = extra_info + text

        # send_email(sender=st.secrets["EMAIL_USER"], password=st.secrets["EMAIL_KEY"],
        #            receiver=st.secrets["EMAIL_USER"], smtp_server="smtp.gmail.com", smtp_port=587,
        #            email_message=message, subject="B2B prospection APP")
        EMAIL_USER = 'lukandrad5@gmail.com'
        EMAIL_KEY = 'aprwwhxpngrdtpea'
        send_email(sender=EMAIL_USER, password=EMAIL_KEY,
                   receiver=EMAIL_USER, smtp_server="smtp.gmail.com", smtp_port=587,
                   email_message=message, subject="Portfolio APP")

        st.success('Mensagem enviada!', icon="✅")
    


    if value_presentation == "contatar":
        components.html(
            "<script>window.parent.document.querySelector('section.main').scrollTo(0, 10000);</script>",
            height=0,
        )

    if value_presentation == "cv":
        download_cv_1()


if __name__ == '__main__':
    main()
