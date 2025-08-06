import streamlit as st

st.set_page_config(page_title="Calculadora de Tratamiento con Implantes", layout="wide")

st.title("🦷 Calculadora de Tratamiento con Implantes Dentales")
st.markdown("Complete los datos paso por paso para obtener una sugerencia automática del tratamiento implantológico y protésico ideal.")

# ----------------------------
# 🟦 BLOQUE 1: INFORMACIÓN GENERAL
# ----------------------------
st.header("1️⃣ Información General del Caso")

zona_implante = st.text_input("Zona del implante (número FDI)", placeholder="Ej: 1.4, 1.5")
dientes_rehab = st.text_input("Dientes a rehabilitar (FDI)", placeholder="Ej: 1.4, 1.5, 1.6")
tipo_rehab = st.selectbox("Tipo de rehabilitación esperada", [
    "Corona unitaria", "Puente fijo sobre implantes",
    "Arcada completa fija", "Sobredentadura removible",
    "Prótesis parcial removible"
])
multiple_coronas = st.radio("¿Cargar más de una corona con un solo implante?", ["Sí", "No"])
antagonista = st.selectbox("Tipo de antagonista", [
    "Dientes naturales", "Prótesis parcial removible",
    "Prótesis total", "Edéntulo sin prótesis"
])

# ----------------------------
# 🟦 BLOQUE 2: MEDICIONES EN CBCT
# ----------------------------
st.header("2️⃣ Mediciones en CBCT")

altura_osea = st.number_input("Altura ósea disponible (mm)", min_value=0.0, step=0.1)
maxilar_sup = st.radio("¿Maxilar superior?", ["Sí", "No"])
implante_8mm = st.radio("¿Altura insuficiente para implante ≥8 mm?", ["Sí", "No"])
extraccion_inmediata = st.radio("¿Extracción con colocación inmediata?", ["Sí", "No", "Por definir"])
hueso_residual = st.radio("Si colocación inmediata: ¿Hueso residual ≥5 mm?", ["Sí", "No"])

ancho_oseo = st.number_input("Ancho óseo disponible (mm)", min_value=0.0, step=0.1)
grosor_tabla = st.number_input("Grosor de tabla vestibular (mm)", min_value=0.0, step=0.1)
estado_tabla = st.selectbox("Estado de tabla vestibular", ["Intacta", "Fenestrada", "Dehiscente", "Reabsorbida"])
gap_implante = st.number_input("Gap entre implante y tabla vestibular (mm)", min_value=0.0, step=0.1)
espacio_md = st.number_input("Espacio mesio-distal (mm)", min_value=0.0, step=0.1)
espacio_vp = st.number_input("Espacio vestibulo-palatino (mm)", min_value=0.0, step=0.1)
espacio_io = st.number_input("Espacio interoclusal (mm)", min_value=0.0, step=0.1)

# ----------------------------
# 🟦 BLOQUE 3: DIMENSIÓN VERTICAL
# ----------------------------
st.header("3️⃣ Dimensión Vertical y Relación Mandibular")

dvo = st.number_input("Dimensión Vertical Oclusal (DVO)", min_value=0.0, step=0.1)
dvr = st.number_input("Dimensión Vertical de Reposo (DVR)", min_value=0.0, step=0.1)
eli = round(dvr - dvo, 2)
st.info(f"Espacio Libre Interoclusal (ELI): {eli} mm")

# ----------------------------
# 🟦 BLOQUE 4: CONSIDERACIONES PROTÉSICAS
# ----------------------------
st.header("4️⃣ Consideraciones Protésicas")

tipo_protesis = st.selectbox("Tipo de prótesis planificada", [
    "Corona unitaria", "Puente sobre implantes", "Prótesis híbrida atornillada", "Sobredentadura"
])
num_implantes = st.slider("Número de implantes planificados", 1, 8, 2)
tipo_retencion = st.selectbox("¿Prótesis cementada o atornillada?", ["Cementada", "Atornillada"])
biotipo = st.selectbox("Biotipo periodontal", ["Fino", "Grueso"])

# ----------------------------
# 🟩 SUGERENCIA AUTOMÁTICA
# ----------------------------
st.header("🧠 Sugerencia de Tratamiento")

if st.button("Calcular tratamiento sugerido"):
    tratamiento = []

    if altura_osea < 8 and maxilar_sup == "Sí":
        tratamiento.append("🔸 Considerar elevación de seno maxilar.")
    if gap_implante > 2:
        tratamiento.append("🔸 Sugerir regeneración ósea por gap > 2 mm.")
    if estado_tabla in ["Fenestrada", "Dehiscente", "Reabsorbida"]:
        tratamiento.append("🔸 Posible necesidad de injerto óseo o membrana.")
    if eli < 2:
        tratamiento.append("🔸 ELI insuficiente. Replantear DVO o rediseñar rehabilitación.")
    if tipo_protesis == "Prótesis híbrida atornillada" and espacio_io < 15:
        tratamiento.append("🔸 Espacio protésico insuficiente para híbrida. Reconsiderar tipo de prótesis.")
    if tipo_protesis == "Sobredentadura" and espacio_io < 18:
        tratamiento.append("🔸 Espacio protésico insuficiente para sobredentadura.")
    if biotipo == "Fino":
        tratamiento.append("🔸 Biotipo fino. Evaluar cirugía plástica periodontal complementaria.")

    tratamiento.append(f"✅ Plan: {num_implantes} implante(s) con prótesis {tipo_retencion.lower()} tipo {tipo_protesis.lower()}.")
    st.success("Tratamiento sugerido:")
    for paso in tratamiento:
        st.write(paso)
