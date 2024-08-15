import streamlit as st
import pandas as pd
from pickle import load
import base64

# Cargar el modelo
model_path = "../models/model_randomforestclasiffier_42_sin_scal.sav"
with open(model_path, 'rb') as f:
    model = load(f)


# CSS para ajustar el ancho del contenedor y agregar una imagen de fondo
config_inic = f'''
<style>
.container {{
    max-width: 1000px;
    margin: auto;
    padding: 20px;
    border-radius: 10px;
           
}}
.title {{
    text-align: left;
    white-space: nowrap;
}}
.prediction {{
    color: white;
    font-weight: bold;
    font-size: 20px;
}}
      
</style>
'''
st.markdown(config_inic, unsafe_allow_html=True)

# Contenedor principal
with st.container():
    st.markdown("<h2 class='title'>Predicción Severidad de Accidentes Viales USA</h2>", unsafe_allow_html=True)
    st.write("<p style='color: white;'>Introducir Valores (Características Tomadas de DataSet Accidentes Viales 2020)</p>", unsafe_allow_html=True)

    st.markdown("<h5>Latitud. Min=24 / Max=50</h5>", unsafe_allow_html=True)
    lat = st.number_input(' ', format="%.6f",
            min_value=24.000000, max_value=50.000000, value=24.000000,step=0.000001,label_visibility="collapsed")
    
    st.markdown("<h5>Longitud. Min=-125 / Max=-68</h5>", unsafe_allow_html=True)
    lng = st.number_input(" ", format="%.6f", 
            min_value=-125.000000, max_value=-68.000000, value=-125.000000, step=0.000001,label_visibility="collapsed")
    
    st.markdown("<h5>Temperatura (F). Min=0 / Max=110</h5>", unsafe_allow_html=True)
    temp = st.number_input(" ", format="%.2f", 
            min_value=0.00, max_value=110.00, value=0.00, step=0.01,label_visibility="collapsed")
    
    st.markdown("<h5>Humedad (%). Min=0 / Max=100</h5>", unsafe_allow_html=True)
    hmd = st.number_input("Humedad (%). Min=0 / Max=100", format="%.2f", 
            min_value=0.00, max_value=100.00, value=0.00, step=0.01,label_visibility="collapsed")

    st.markdown("<h5>Semáforo Cercano (Traffic_Signal_n):</h5>", unsafe_allow_html=True)
    semaforo = st.radio("Selecciona una opción para Semáforo Cercano:", ["Sí", "No"],
                         key="semaforo", label_visibility="collapsed")
    sem = 1 if semaforo == "Sí" else 0

    st.markdown("<h5>Crepúsculo: Noche (Civil_Twilight_n):</h5>", unsafe_allow_html=True)
    crepusculo = st.radio("Selecciona una opción para Crepúsculo Noche:", ["Sí", "No"],
                         key="crepusculo", label_visibility="collapsed")
    crep = 1 if crepusculo == "Sí" else 0

    signif={'1':'Menor impacto en el tráfico. Retraso corto como resultado del accidente.',
            '2':'Impacto moderado en el tráfico.','3':'Impacto significativo en el tráfico.',
            '4':'Impacto considerable en el tráfico. Retraso largo como resultado del accidente.'}

    if st.button("Predecir"):
        data = pd.DataFrame([[float(lat), float(lng), int(sem), int(crep), float(temp), float(hmd)]], 
                            columns=['Start_Lat', 'Start_Lng', 'Traffic_Signal_n', 'Civil_Twilight_n',
                                     'Temperature(F)', 'Humidity(%)'])

        st.write("Datos de Entrada:", data)

        prediction = model.predict(data)[0]
        pred_class = f"{prediction:.0f}"

        st.write(f"<p class='prediction'>La Predicción de la Severidad es: {pred_class}</p>", unsafe_allow_html=True)
        st.write(f"<p class='prediction'>{signif[str(pred_class)]}</p>", unsafe_allow_html=True)