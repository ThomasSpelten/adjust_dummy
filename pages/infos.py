import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import foo
st.set_page_config(page_title="adjust mockup", page_icon=":sparkles:", layout="centered", initial_sidebar_state="auto", menu_items=None)

st.header("Weiterführende Infos und Quellen")

st.subheader("Steckbrief: Monokristallines PV-Modul")
col1, col2 = st.columns([4, 5]) #gibt relative Größen an
with col1:
    st.image("mono.png", width=250)
with col2:
    monosteck=pd.DataFrame(
         {"Kategorie": ["Installationskosten", "Laufende Kosten", "indirekte Treibhausgasemmissionen", "direkte Treibhausgasemissionen", "Ressourcenverbrauch", "Ökotoxizität", "Wasserverbrauch", "Ozonabbau", "Süßwassereutrophierung", "Meereseutrophierung", "Photochemische Ozonbildung", "abiotischer Ressourcenverbrauch - Mineralien", "abiotischer Ressourcenverbrauch - fossile Brennstoffe", "Humantoxität", "Landnutzung", "Feinstaubemmissionen" ],
         "Kosten/Auswirkungen": ["N/A", "N/A", "N/A","N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A",  ]}
    )
    st.dataframe(monosteck, hide_index=True)
st.divider()
st.subheader("Steckbrief: Polykristallines PV-Modul")
col1, col2 = st.columns([4, 5]) #gibt relative Größen an
with col1:
    st.image("poly.jpg", width=250)
with col2:
    monosteck=pd.DataFrame(
         {"Kategorie": ["Installationskosten", "Laufende Kosten", "indirekte Treibhausgasemmissionen", "direkte Treibhausgasemissionen", "Ressourcenverbrauch", "Ökotoxizität", "Wasserverbrauch", "Ozonabbau", "Süßwassereutrophierung", "Meereseutrophierung", "Photochemische Ozonbildung", "abiotischer Ressourcenverbrauch - Mineralien", "abiotischer Ressourcenverbrauch - fossile Brennstoffe", "Humantoxität", "Landnutzung", "Feinstaubemmissionen" ],
         "Kosten/Auswirkungen": ["N/A", "N/A", "N/A","N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A",  ]}
    )
    st.dataframe(monosteck, hide_index=True)
st.divider()
st.subheader("Steckbrief: Monokristallines PV-Modul")
col1, col2 = st.columns([4, 5]) #gibt relative Größen an
with col1:
    st.image("CIGS.jpg", width=250)
with col2:
    monosteck=pd.DataFrame(
         {"Kategorie": ["Installationskosten", "Laufende Kosten", "indirekte Treibhausgasemmissionen", "direkte Treibhausgasemissionen", "Ressourcenverbrauch", "Ökotoxizität", "Wasserverbrauch", "Ozonabbau", "Süßwassereutrophierung", "Meereseutrophierung", "Photochemische Ozonbildung", "abiotischer Ressourcenverbrauch - Mineralien", "abiotischer Ressourcenverbrauch - fossile Brennstoffe", "Humantoxität", "Landnutzung", "Feinstaubemmissionen" ],
         "Kosten/Auswirkungen": ["N/A", "N/A", "N/A","N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A",  ]}
    )
    st.dataframe(monosteck, hide_index=True)

if(st.button("Zurück zu den Ergebnissen")):
    st.switch_page("pages/results.py")