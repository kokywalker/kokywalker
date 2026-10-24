import streamlit as st

# Configuración básica de la página
st.set_page_config(
    page_title="Mi Primera App en Streamlit",
    page_icon="🚀",
    layout="centered"
)

# Título principal
st.title("🚀 ¡Hola, Jorge!")
st.write("Esta es una aplicación de prueba desplegada en Streamlit Cloud.")

# Sección interactiva
st.divider()
st.subheader("Panel de Prueba")

nombre = st.text_input("¿Cómo te gustaría llamar a este proyecto?", "Proyecto Agroindustrial")

if st.button("Saludar"):
    st.success(f"¡Excelente! El proyecto **{nombre}** está funcionando correctamente.")

# Información adicional en la barra lateral
with st.sidebar:
    st.header("Acerca de")
    st.write("Aplicación de ejemplo configurada para correr en la nube de Streamlit.")