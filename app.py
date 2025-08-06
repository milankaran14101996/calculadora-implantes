import streamlit as st

st.set_page_config(page_title="Calculadora de Tratamiento con Implantes", layout="centered")

st.title("🦷 Calculadora de Tratamiento con Implantes y Prótesis")
st.markdown("Completa los siguientes datos clínicos para obtener una sugerencia de tratamiento:")

# Entradas
altura = st.number_input("Altura ósea (mm)", min_value=0.0, step=0.1)
ancho = st.number_input("Ancho óseo (mm)", min_value=0.0, step=0.1)
tabla = st.selectbox("Estado de tabla vestibular", ["Intacta", "Reabsorbida", "Dehiscente"])
biotipo = st.selectbox("Biotipo gingival", ["Fino", "Grueso"])
antagonista = st.selectbox("Tipo de antagonista", ["Dientes naturales", "Prótesis"])
tipo_protesis = st.selectbox("Tipo de prótesis", ["Corona unitaria", "Puente fijo sobre implantes", "Sobredentadura removible", "Híbrida atornillada"])

if st.button("🔍 Sugerir tratamiento"):
    resultado = ""
    if altura < 8:
        resultado += "⚠️ Altura ósea insuficiente: considerar elevación de seno o implante corto.\n"
    else:
        resultado += "✅ Altura ósea adecuada.\n"
    if ancho < 6:
        resultado += "⚠️ Ancho óseo limitado: evaluar regeneración o implante estrecho.\n"
    else:
        resultado += "✅ Ancho óseo suficiente.\n"
    if tabla in ["Dehiscente", "Reabsorbida"]:
        resultado += "⚠️ Tabla vestibular comprometida: evaluar regeneración ósea.\n"
    else:
        resultado += "✅ Tabla vestibular favorable.\n"
    if biotipo == "Fino":
        resultado += "⚠️ Biotipo fino: considerar técnicas para conservar tejido.\n"
    else:
        resultado += "✅ Biotipo adecuado.\n"
    if antagonista == "Dientes naturales":
        resultado += "⚠️ Mayor carga funcional: considerar diseño de prótesis con refuerzo.\n"
    else:
        resultado += "✅ Cargas funcionales moderadas.\n"
    if tipo_protesis == "Híbrida atornillada":
        resultado += "💡 Requiere 15 mm de espacio interoclusal mínimo.\n"
    elif tipo_protesis == "Sobredentadura removible":
        resultado += "💡 Requiere 18-20 mm de espacio vertical.\n"

    st.subheader("📋 Sugerencia de Tratamiento:")
    st.success(resultado)
