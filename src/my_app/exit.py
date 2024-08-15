import streamlit as st

#st.title("Salir de la Aplicación")

#if st.button("Confirmar Salida"):
st.markdown("""
        <meta http-equiv="refresh" content="0; url=https://www.4geeks.com">
        <div style="text-align: center; margin-top: 50px;">
            <h2>Redirigiendo a 4Geeks...</h2>
            <p>Si no eres redirigido automáticamente, haz clic <a href="https://www.4geeks.com">aquí</a>.</p>
        </div>
    """, unsafe_allow_html=True)