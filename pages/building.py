import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import foo

st.set_page_config(page_title="adjust mockup", page_icon=":sparkles:", layout="centered", initial_sidebar_state="auto", menu_items=None)


st.markdown("""             
<style>
    button.step-up {display: none;}
    button.step-down {display: none;}
    div[data-baseweb] {border-radius: 4px;}
</style>""",
unsafe_allow_html=True) #disable buttons on number input

st.subheader( "Geben Sie nun Gebäudeparameter und den Energie- und Wärmebedarf des Gebäudes an")
age=st.number_input(
   label="Wann wurde das Gebäude gebaut?",
    value=1910,
    min_value=0,
    format="%d"
    )
st.write("Wo befindet sich das Gebäude?")
map_data={
    'latitude': [51.53926979151661],
    'longitude': [7.219745218719016]}
data = pd.DataFrame(map_data)
st.map(map_data, zoom=16, size=6)

st.number_input("Welche Fläche hat das Gebäude? (in Quadratmetern)", min_value=0, format="%d")

st.selectbox("Welche Energieeffizienzklasse hat das Gebäude?", ("A+", "A", "B", "C", "D", "E", "F", "G", "H"),index=None,  placeholder="Wählen Sie eine Energieeffizienzklasse aus")


    
type = st.selectbox(
    "Welchen Gebäudetyp hat das Gebäude?",
    ("Bürogebäude", "Einfamilienhaus", "Mehrfamilienhaus"), index=None, placeholder="Wählen Sie einen Gebäudetyp aus")
st.selectbox("Welche Art von Dach liegt vor?", ("Flachdach","Pultdach", "Satteldach", "Walmdach"), index=None, placeholder="Wählen Sie einen Dachtyp aus")

foo.energydemand=st.number_input(
    label="Wie viel Energiebedarf hat das Gebäude? (in kWh pro Quadratmeter pro Jahr). ",
    help="Falls Sie diesen nicht kennen, wird ein Durchschnittswert aus Ihrem Gebäudetyp errechnet",
    #value=72.1,
    min_value=0.0,
    format="%f"
    )
foo.technology_en=["Keine"]
number=0
technologies_en=["Keine", "Multikristallines PV-Modul", "Polykristallines PV-Modul","CIGS PV-Modul" ]
Technologie1=st.selectbox("Welche Technologien haben Sie zur Stromerzeugung?", technologies_en, placeholder="Wählen Sie eine Technologie aus")
while(Technologie1!="Keine"):
    number=number+1
    col1, col2 = st.columns([1, 1]) #gibt relative Größen an
    with col2:
        st.number_input("Wie alt ist diese Technologie? (in Jahren)" , key=4*number, format="%d", min_value=0)
        st.number_input("Wie viel Dachfläche belegt diese Technologie? (in Quadratmetern)" , key=10000*number, format="%d", min_value=0)
        generated=st.number_input("Wie viel kWh generiert Ihre Technologie ungefähr pro Jahr?", key=4*number+1, format="%d", min_value=0)
    generated=Technologie1 + " mit einer Erzeugung von " + str(generated) + " kWh pro Jahr."
    foo.technology_en.append(generated)
    technologies_en.remove(Technologie1)
    Technologie1="Keine"
    Technologie1=st.selectbox("Welche weitere Technologien haben Sie zur Stromerzeugung?", technologies_en, key=-2*number, placeholder="Wählen Sie eine Technologie aus")
if(number!=0):
    foo.technology_en.remove("Keine")
foo.heatdemand=st.number_input(
    label="Wie viel Wärmebedarf hat Ihr Gebäude? (in kWh pro Quadratmeter pro Jahr). ",
    help="Falls Sie diesen nicht kennen, wird ein Durchschnittswert aus Ihrem Gebäudealter errechnet",
    #value=72.1,
    min_value=0.0,
    format="%f"
    )
foo.technology_he=["Keine"]
number=0
technologies_he=["Keine", "Luft-Wärme-Pumpe", "Boden-Wärme-Pumpe"]
Technologie2=st.selectbox("Welche Technologien haben Sie zur Wärmeerzeugung?", technologies_he, placeholder="Wählen Sie eine Technologie aus")
while(Technologie2!="Keine"):
    number=number+1
    col1, col2 = st.columns([1, 1]) #gibt relative Größen an
    with col2:
        st.number_input("Wie alt ist Ihre Technologie? (in Jahren)" , key=4*number+2, format="%d", min_value=0)
        generated=st.number_input("Wie viel kWh generiert Ihre Technologie ungefähr pro Jahr?", key=4*number+3, format="%d", min_value=0)
    generated=Technologie2 + " mit einer Erzeugung von " + str(generated) + " kWh pro Jahr."
    foo.technology_he.append(generated)
    technologies_he.remove(Technologie2)
    Technologie2="Keine"
    Technologie2=st.selectbox("Welche weitere Technologien haben Sie zur Stromerzeugung?", technologies_he, key=-2*number+1, placeholder="Wählen Sie eine Technologie aus")
if(number!=0):
    foo.technology_he.remove("Keine")

col1, col2, col3 = st.columns([2, 2, 1]) #gibt relative Größen an
with col1:
    if(st.button("Ein weiteres Gebäude hinzufügen")):
        st.switch_page("pages/building.py")
with col3:
    if(st.button("Berechnen ", help="Lassen Sie sich die optimalen Technologien für Ihr Gebäude anzeigen")):
        st.switch_page("pages/results.py")