import streamlit as st

st.set_page_config(page_title="Calculadora de Tratamiento con Implantes", layout="wide")
st.title("🦷 Calculadora de Tratamiento con Implantes Dentales")

# ------------------------
# 1️⃣ SELECCIÓN DE DIENTES FDI
# ------------------------
st.markdown("## 1️⃣ Selección de Dientes a Rehabilitar (FDI)")
dientes_fdi = [
    '11', '12', '13', '14', '15', '16', '17', '18',
    '21', '22', '23', '24', '25', '26', '27', '28',
    '31', '32', '33', '34', '35', '36', '37', '38',
    '41', '42', '43', '44', '45', '46', '47', '48'
]
seleccion_dientes = st.multiselect("Selecciona uno o más dientes a rehabilitar:", options=dientes_fdi)
if seleccion_dientes:
    st.success(f"Dientes seleccionados: {', '.join(seleccion_dientes)}")

# ------------------------
# 2️⃣ TIPO DE ANTAGONISTA
# ------------------------
st.markdown("## 2️⃣ Tipo de Antagonista")
antagonista = st.selectbox("Selecciona el tipo de antagonista", [
    "Diente Natural", "Corona sobre Implante", "Prótesis Fija", "Prótesis Removible", "Sin antagonista"
])
if st.button("📋 Ver Recomendaciones por Antagonista"):
    st.subheader("📌 Recomendaciones según tipo de antagonista:")
    recomendaciones = {
        "Diente Natural": "- ⚠️ Movimiento fisiológico\n- ✔️ Ajuste oclusal fino\n- 🔁 Carga diferida si torque <35 Ncm",
        "Corona sobre Implante": "- ⚠️ Sobrecontacto\n- ✔️ Contactos simultáneos\n- ❌ Evitar carga inmediata múltiple",
        "Prótesis Fija": "- ✔️ Estabilidad buena\n- 🔁 Carga inmediata si torque >35 Ncm",
        "Prótesis Removible": "- ⚠️ Contacto variable\n- ❌ Evitar carga inmediata si inestabilidad",
        "Sin antagonista": "- ⚠️ Extrusión posible\n- ✔️ Planear rehabilitación antagonista\n- ❌ Evitar carga inmediata"
    }
    st.markdown(recomendaciones[antagonista])

# ------------------------
# 3️⃣ ESPACIO INTERCLUSAL
# ------------------------
st.markdown("## 3️⃣ Espacio Interoclusal Disponible (mm)")
espacio_mm = st.number_input("Ingresa el espacio interoclusal disponible (mm):", min_value=0.0, max_value=30.0, step=0.1)

def seleccionar_protesis_espacio(espacio):
    if espacio < 4:
        return "❌ No se recomienda rehabilitación directa", ["Alargamiento coronario", "Reducir antagonista"]
    elif espacio < 6:
        return "✔ Corona unitaria atornillada", ["Evitar exceso de cerámica"]
    elif espacio < 8:
        return "✔ Corona o puente corto atornillado", []
    elif espacio < 12:
        return "✔ Puente fijo o prótesis parcial", []
    elif espacio <= 15:
        return "✔ Prótesis híbrida (All-on-4)", []
    else:
        return "✔ Prótesis híbrida con flancos", []

if st.button("📌 Evaluar Recomendación Protésica"):
    r, detalles = seleccionar_protesis_espacio(espacio_mm)
    st.subheader("Recomendación Protésica:")
    st.info(r)
    for item in detalles:
        st.markdown(f"- {item}")

# ------------------------
# 4️⃣ BIOTIPO GINGIVAL Y SONRISA
# ------------------------
st.markdown("## 4️⃣ Evaluación Estética: Biotipo y Exposición Gingival")
biotipo = st.selectbox("Biotipo gingival:", ["Biotipo delgado", "Biotipo intermedio", "Biotipo grueso"])
zona_estetica = st.selectbox("Nivel de sonrisa:", [
    "Alta exposición (más de 3 mm)", "Exposición moderada (1–3 mm)", "Baja exposición (menos de 1 mm)"
])
if st.button("🔍 Ver recomendaciones estéticas"):
    st.subheader("📌 Biotipo:")
    st.markdown({
        "Biotipo delgado": "- ⚠️ Riesgo de recesión\n- ✔️ Disilicato o zirconia estratificada",
        "Biotipo intermedio": "- ☑️ Equilibrado\n- ✔️ Carga inmediata si torque >35 Ncm",
        "Biotipo grueso": "- 💪 Estabilidad tisular\n- ✔️ Buena estética funcional"
    }[biotipo])
    st.subheader("📌 Sonrisa:")
    st.markdown({
        "Alta exposición (más de 3 mm)": "- 🎯 Alta demanda estética\n- ✔️ Materiales altamente estéticos",
        "Exposición moderada (1–3 mm)": "- ⚖️ Equilibrio estético\n- ✔️ Zirconia o híbridos",
        "Baja exposición (menos de 1 mm)": "- 👁️‍🗨️ Baja visibilidad\n- ✔️ Elección flexible"
    }[zona_estetica])

# ------------------------
# 6️⃣ PLANIFICACIÓN QUIRÚRGICA COMPLETA
# ------------------------
st.markdown("## 6️⃣ Planificación Quirúrgica: Cantidad, Diámetro y Longitud del Implante")

# Tipo de rehabilitación basado en espacio
if espacio_mm < 4:
    tipo_rehab = "No indicado"
elif espacio_mm < 6:
    tipo_rehab = "Corona unitaria"
elif espacio_mm < 8:
    tipo_rehab = "Puente corto"
elif espacio_mm < 12:
    tipo_rehab = "Puente largo"
elif espacio_mm <= 15:
    tipo_rehab = "Prótesis híbrida"
else:
    tipo_rehab = "Prótesis híbrida extendida"

longitud_tramo = st.slider("📏 Longitud del tramo edéntulo (mm):", 5, 60, 20)
carga_por_antagonista = {
    "Diente Natural": 1.2,
    "Corona sobre Implante": 1.0,
    "Prótesis Fija": 0.9,
    "Prótesis Removible": 1.4,
    "Sin antagonista": 0.8
}
carga = carga_por_antagonista.get(antagonista, 1.0)

def sugerir_implantes(tipo, longitud_mm, carga, biotipo):
    if tipo in ["Corona unitaria", "No indicado"]:
        return 1
    elif tipo == "Puente corto":
        return 2 if longitud_mm <= 15 else 3
    elif tipo == "Puente largo":
        base = longitud_mm / 10
        ajuste = 0.5 if carga > 1.2 else -0.5 if carga < 1.0 else 0
        ajuste += 0.5 if biotipo == "Biotipo delgado" else 0
        return int(round(base + ajuste))
    elif tipo in ["Prótesis híbrida", "Prótesis híbrida extendida"]:
        return 4 if longitud_mm <= 30 else 6
    else:
        return 2

implantes_sugeridos = sugerir_implantes(tipo_rehab, longitud_tramo, carga, biotipo)
st.success(f"🔢 Implantes sugeridos: {implantes_sugeridos} para {longitud_tramo} mm de tramo edéntulo.")
st.caption(f"Rehabilitación: {tipo_rehab} | Antagonista: {antagonista} | Biotipo: {biotipo}")

# DIÁMETRO DEL IMPLANTE
st.markdown("### 🧱 Selección del Diámetro del Implante")
ancho_vest = st.number_input("Ancho óseo VESTIBULAR (mm):", min_value=0.0, step=0.1)
ancho_centro = st.number_input("Ancho óseo CENTRAL (mm):", min_value=0.0, step=0.1)
ancho_lingual = st.number_input("Ancho óseo LINGUAL / PALATINO (mm):", min_value=0.0, step=0.1)

ancho_promedio = (ancho_vest + ancho_centro + ancho_lingual) / 3 if (ancho_vest + ancho_centro + ancho_lingual) > 0 else 0
if ancho_promedio:
    if ancho_promedio < 5:
        st.warning("⚠️ Ancho óseo insuficiente. Puede requerir injerto o implante estrecho (≤3.5 mm).")
    elif ancho_promedio <= 7:
        st.info("✔️ Implante sugerido: diámetro estándar (3.5 a 4.3 mm)")
    else:
        st.success("💪 Implante sugerido: diámetro ancho (4.5 mm o más)")

# LONGITUD DEL IMPLANTE
st.markdown("### 📏 Selección de la Longitud del Implante")
altura_osea = st.number_input("Altura ósea disponible (mm):", min_value=0.0, step=0.1)
colocacion = st.selectbox("Nivel de colocación del implante", ["A nivel de cresta (0 mm)", "Subcrestal (2 mm)", "Supracrestal (-1 mm)"])
if colocacion == "Subcrestal (2 mm)":
    margen_seguridad = 2
elif colocacion == "Supracrestal (-1 mm)":
    margen_seguridad = -1
else:
    margen_seguridad = 0

longitud_recomendada = altura_osea - margen_seguridad - 2  # 2 mm de seguridad apical
if longitud_recomendada > 0:
    st.success(f"📐 Longitud de implante sugerida: {round(longitud_recomendada, 1)} mm")
else:
    st.error("❌ Altura ósea insuficiente. Considerar técnicas avanzadas (elevación seno, injertos, etc.)")
