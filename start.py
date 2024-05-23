import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import time
import foo
st.set_page_config(page_title="adjust mockup", page_icon=":sparkles:", layout="centered", initial_sidebar_state="auto", menu_items=None)





st.header("Herzlich willkommen zum Probetool _adjust_", divider="red")
st.subheader("Geben Sie zunächst Ihre persönliche Gewichtung der Einflussfaktoren an")
foo.CO2 = st.slider('Wie wichtig sind Ihnen CO2 Emmissionen?', min_value=0, max_value=10, step=1, value=10)
foo.material= st.slider('Wie wichtig ist Ihnen der Materialverbrauch?', min_value=0, max_value=10, step=1, value=10)
foo.costs = st.slider('Wie wichtig sind Ihnen die finanziellen Kosten?', min_value=0, max_value=10, step=1, value=10)

st.write("Beginnen Sie nun mit der Eingabe Ihres ersten Gebäudes")
if st.button("Loslegen!"):
    st.switch_page("pages/building.py")



    





