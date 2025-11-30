import streamlit as st

st.set_page_config(
    page_title="Menú de Dieta Interactivo",
    page_icon="✅",
    layout="wide"
)

st.title("✅ Plan de Dieta Interactivo")
st.markdown("---") 

st.info("Marca las casillas a medida que consumes tus comidas para llevar un seguimiento de tu día.")
st.markdown("---") 

menu = {
    "1 COMIDA - Desayuno": [
        "Base: 20 gr de copos de avena / 30 gr de harina de avena o dos rebanadas de pan de espelta.",
        "Acompañamiento: 150 gr de yogurt kéfir o griego + 20 gr de proteína + 25 gr de frutos rojos + 15 gr de semillas de lino."
    ],
    "2 COMIDA - Segunda Opción Salada": [
        "Proteína (Elige 1): 50 gr de jamón cocido / Una lata de atún al natural o melva / 65 gr de lomo embuchado.",
        "Carbohidrato (Elige 1): 2 panes de crack de espelta / 3 tortitas de arroz.",
        "Extra: Una pieza de fruta."
    ],
    "3 COMIDA - Almuerzo": [
        "Proteína Principal: 150 gr de pollo o pavo / 140 gr de carne roja (1 vez/semana) / 180 gr de pescado azul (2 veces/semana) / 20 gr de pescado blanco.",
        "Acompañamiento: 200 gr de verduras o una ensalada."
    ],
    "4 COMIDA - Merienda": [
        "Tan sencillo como una pieza de fruta."
    ],
    "ÚLTIMA COMIDA - Cena": [
        "Proteína: 150 gr de pescado / 160 gr de carne blanca / 200 gr de pulpo o sepia (si quieres) / 120 ml de claras de huevo más huevo (en tortilla te la puedes hacer).",
        "Acompañamiento: 200 gr de verdura la que tú quieras.",
        "Extra: 2 tortitas de arroz."
    ]
}

cols = st.columns(3) 

keys = list(menu.keys())
for i, key in enumerate(keys):
    col_index = i % 3 
    
    with cols[col_index]:
        with st.expander(f"**{key}**", expanded=True):
            for j, item in enumerate(menu[key]):
                checkbox_key = f"{key}_{j}"
                st.checkbox(item, key=checkbox_key)
                
            if key == "4 COMIDA - Merienda":
                 st.markdown("---")

if st.button("Reiniciar mi Progreso del Día"):
    for key in st.session_state.keys():
        if "_" in key: 
            st.session_state[key] = False
            
    st.rerun()


st.markdown("---")
st.success("¡Buen seguimiento! Tu plan nutricional ahora es interactivo.")
st.caption("Hecho con Streamlit y Python.")

st.caption("Hecho con Streamlit y Python.")


