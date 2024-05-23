import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import foo
st.set_page_config(page_title="adjust mockup", page_icon=":sparkles:", layout="centered", initial_sidebar_state="auto", menu_items=None)

technologies=["Monokristallines PV-Modul","Polykristallines PV-Modul","CIGS PV-Modul","Stromnetz Deutschland","Luft-Wärme-Pumpe","Boden-Wärme-Pumpe", "Gasboiler"] #Kupfer-Indium-Gallium-Diselenid
co2em=[52, 44, 40, 498, 110, 98, 220] #Für Gridmix gibt EcoInvent 817g CO2e /kWh an. Ist schon höher als vom UBA berechnet. Was nehmen?
eurem=[7.6, 7.6, 4.5, 26.2, 7.0, 7.3, 11.2]
matem=[0.54, 0.55, 0.82, 2.12, 0.246 ,0.3, 0.123] #für Gridmix ist aus EcoInvent. hier erhält man aber auch für die PV Module Werte von 3.96 und 3.75

technologies_en=["Monokristallines PV-Modul","Polykristallines PV-Modul","CIGS PV-Modul","Stromnetz Deutschland"]
co2em_en=[52, 44, 40, 498]
eurem_en=[7.6, 7.6, 4.5, 26.2]
matem_en=[0.54, 0.55, 0.82, 2.12]
technologies_he=["Luft-Wärme-Pumpe","Boden-Wärme-Pumpe", "Gasboiler"]
co2em_he=[110, 98, 220]
eurem_he=[7.0, 7.3, 11.2]
matem_he=[0.246 ,0.3, 0.123]

def rescale(array):
     i=0
     x=max(array)
     y=min(array)
     tmp=array.copy()
     while i < len(array):
        tmp[i]=(array[i]-x)/(y-x)
        i+=1 
     return tmp

def singlescore(array1, array2, array3, array4):
    tmp1=rescale(array1)
    tmp2=rescale(array2)
    tmp3=rescale(array3)
    sinsc=[]
    sinsc_bar=array4
    i=0
    sum=foo.CO2+foo.material+foo.costs
    while i < len(array1):
        score=foo.CO2/sum*tmp1[i]+foo.costs/sum*tmp2[i]+foo.material/sum*tmp3[i]
        if(score==0):
            score=0         #fürs Vorzeichen und den Fun
        sinsc.append(score)
        sinsc_bar.append(tmp1[i]/3)
        sinsc_bar.append(tmp2[i]/3)
        sinsc_bar.append(tmp3[i]/3)
        i+=1
    return sinsc
    

st.subheader("Ergebnis:")
with st.spinner('Berechne optimale nachhaltige Technologie'):
        time.sleep(1)
if(foo.energydemand == 0):
    foo.energydemand = 55 #Quelle: https://www.gasag.de/magazin/energiesparen/stromverbrauch-unternehmen
    st.write("Es wurde kein Energiebedarf angegeben. Wir nehmen für Ihr Bürogebäude einen durschnittlichen Energiebedarf von", foo.energydemand, "kWh pro Quadratmeter und Jahr an." )
else:
    st.write("Sie haben einen Energiebedarf von", foo.heatdemand, "angegeben.")    
    #st.divider()
st.write("Sie haben zur Stromerzeugung folgende Technologien:", foo.technology_en)
if(foo.heatdemand == 0):
    foo.heatdemand = 72.1 #Quelle: https://webtool.building-typology.eu/#bm
    st.write("Es wurde kein Wärmebedarf angegeben. Wir nehmen für Ihr Gebäudealter einen durschnittlichen Wärmebedarf von", foo.heatdemand, "kWh pro Quadratmeter und Jahr an." )
else:
    st.write("Sie haben einen Wärmebedarf von", foo.heatdemand, "angegeben.")
    #st.divider()
st.write("Sie haben zur Wärmeerzeugung folgende Technologien:", foo.technology_he)
st.write("Sie haben folgende Gewichtung gewählt:")

labels = 'CO2-Emmissionen', 'Materialverbrauch', 'Finanzielle Kosten',
sum=foo.CO2+foo.material+foo.costs
sizes = [foo.CO2/sum, foo.material/sum, foo.costs/sum]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
startangle=90)
col1, col2, col3 = st.columns([1, 4, 1]) #gibt relative Größen an
with col2:
    st.pyplot(fig1)
st.subheader("Folgende Technologien haben wir anhand Ihrer Gewichtung für Sie ausgewählt:")
    #image=st.image(image="Polykristallin.jpg", width=100)

st.subheader("Energieerzeugung:")
dummy_en=[]
sinsc_en=singlescore(co2em_en, eurem_en, matem_en, dummy_en)

df = pd.DataFrame(
         {"Technologie": technologies_en,
         "Art der Energie":  [ "Strom", "Strom", "Strom", "Strom"],
         "g CO2 e pro kWh": co2em_en,
         "ct pro kWh": eurem_en,
         "g Cu e pro kWh": matem_en,
         "Single Score": sinsc_en,
         'Bilder': [ 'https://pngimg.com/uploads/solar_panel/solar_panel_PNG149.png',
                    "https://pngimg.com/uploads/solar_panel/solar_panel_PNG118.png",
                     "https://upload.wikimedia.org/wikipedia/commons/9/9f/Cigsep.jpg", 
                     "https://www.umweltbundesamt.de/sites/default/files/medien/372/bilder/kraftwerksleistung_2024_0.png",
                     #"https://upload.wikimedia.org/wikipedia/commons/9/94/Outunit_of_heat_pump.jpg",
                     #"https://www.energie-fachberater.de/bilder/heizung-lueftung/heizung/waermepumpe/erwaermepumpe-sonde-bwp.jpg",
                     #"https://www.kesselheld.de/content/uploads/2016/12/gas-boiler.jpg"
                     ],
         }
)

df=df.sort_values(by="Single Score", ascending=False)
    #CIGS=Copper indium gallium selenide 
    #Quelle PV: https://www.sciencedirect.com/science/article/pii/S0959652618304530?via%3Dihub
    #Quelle Strommix: https://www.ndr.de/nachrichten/info/Strompreis-aktuell-So-viel-kosten-die-Kilowattstunden,strompreis182.html 
def path_to_image_html(path):
    return '<img src="' + path + '" width="60" >'
def convert_df(input_df):
     return input_df.to_html(escape=False, formatters=dict(Bilder=path_to_image_html), )

html_en = convert_df(df)
st.markdown(
    html_en,
    unsafe_allow_html=True
)
chart_data=pd.DataFrame([[dummy_en[0], dummy_en[1], dummy_en[2]], [dummy_en[3], dummy_en[4], dummy_en[5]], [dummy_en[6], dummy_en[7], dummy_en[8]], [dummy_en[9], dummy_en[10], dummy_en[11]]], columns=["CO2 Emissionen ", "Finanzielle Kosten", "Materialverbrauch"], )
st.subheader("Single Score aufgeschüsselt:")
st.write("Da der Single Score für die beste Technologie auch den höchsten Score vergibt, bedeutet hier ein kleiner Balken eine schlechte Performance.")
st.bar_chart(chart_data)
st.divider()
st.subheader("Wärmeerzeugung:")
dummy_he=[]
sinsc_he=singlescore(co2em_he, eurem_he, matem_he, dummy_he)

df_he = pd.DataFrame(
         {"Technologie": technologies_he,
         "Art der Energie":  ["Wärme", "Wärme", "Wärme"],
         "g CO2 e pro kWh": co2em_he,
         "ct pro kWh": eurem_he,
         "g Cu e pro kWh": matem_he,
         "Single Score": sinsc_he,
         'Bilder': ["https://upload.wikimedia.org/wikipedia/commons/9/94/Outunit_of_heat_pump.jpg",
                     "https://www.energie-fachberater.de/bilder/heizung-lueftung/heizung/waermepumpe/erwaermepumpe-sonde-bwp.jpg",
                     "https://www.kesselheld.de/content/uploads/2016/12/gas-boiler.jpg",
                    ],
         }
)

df_he=df_he.sort_values(by="Single Score", ascending=False)
    #CIGS=Copper indium gallium selenide 
    #Quelle PV: https://www.sciencedirect.com/science/article/pii/S0959652618304530?via%3Dihub
    #Quelle Strommix: https://www.ndr.de/nachrichten/info/Strompreis-aktuell-So-viel-kosten-die-Kilowattstunden,strompreis182.html 
def path_to_image_html(path):
    return '<img src="' + path + '" width="60" >'
def convert_df(input_df):
     return input_df.to_html(escape=False, formatters=dict(Bilder=path_to_image_html), index=False)

html_he = convert_df(df_he)
st.markdown(
    html_he,
    unsafe_allow_html=True
)


st.divider()
if(st.button("Weitere Informationen zu den einzelnen Technologien")):
    st.switch_page("pages/infos.py")
if(st.button("Zurück zum Start")):
    st.switch_page("start.py")