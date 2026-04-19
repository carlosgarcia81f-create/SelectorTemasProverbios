import streamlit as st
import pandas as pd

# 1. Carga de datos (ajustado a tu hoja 'Datos')
@st.cache_data
def cargar_datos():
    # Cambia el nombre del archivo si es necesario
    df = pd.read_excel("proverbios.xlsx", sheet_name="Datos")
    return df

df = cargar_datos()

st.title("📖 Explorador de Proverbios")

# --- INTERFAZ DE USUARIO ---
# 2. Selector de Categoría (Como tu segmentador de Excel)
categorias = sorted(df['Categoria'].unique())
cat_seleccionada = st.selectbox("Selecciona una Categoría:", categorias)

# Filtrar los datos por la categoría elegida
df_filtrado = df[df['Categoria'] == cat_seleccionada]

st.divider()
st.subheader(f"Temas disponibles en: {cat_seleccionada}")

# 3. Lógica de "Tabla Dinámica" con Expanders
# Agrupamos por Tema para iterar sobre ellos
temas = sorted(df_filtrado['Tema'].unique())

for tema in temas:
    # Creamos un desplegable por cada tema
    with st.expander(f"🔹 {tema}"):
        # Filtramos versículos solo de este tema
        versiculos = df_filtrado[df_filtrado['Tema'] == tema]
        
        for index, row in versiculos.iterrows():
            # Mostramos la cita en negrita y el texto abajo
            st.markdown(f"**{row['Cita']}**")
            st.write(row['Texto'])
            st.markdown("---") # Una línea sutil de separación entre versículos


# 1. Leer el archivo
df = pd.read_excel("Proverbios_agrupados.xlsx",sheet_name="Datos")

#2. Ver las primeras filas para confirmar nombres de columnas
print("---Columnas detectadas---")
print(df.columns)

#3. Simular la elección de un joven
#Supongamos que se le asignó la categoría 'Sabiduría'
miCategoria = "Sabiduría"
temasMiCategoria= df[df['Categoría']==miCategoria]['Tema'].unique()
for tema in temas:
    # Creamos un desplegable por cada tema
    with st.expander(f"🔹 {tema}"):
        # Filtramos versículos solo de este tema
        versiculos = df_filtrado[df_filtrado['Tema'] == tema]
        
        for index, row in versiculos.iterrows():
            # Mostramos la cita en negrita y el texto abajo
            st.markdown(f"**{row['Cita']}**")
            st.write(row['Texto'])
            st.markdown("---") # Una línea sutil de separación entre versículos
