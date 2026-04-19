import streamlit as st
import pandas as pd

# 1. Configuración de página para móviles
st.set_page_config(page_title="Proverbios Jóvenes", page_icon="📖")

@st.cache_data
def cargar_datos():
    # USA EL NOMBRE EXACTO DEL ARCHIVO QUE SUBISTE A GITHUB
    # Si tu archivo se llama 'Proverbios_agrupados.xlsx', cámbialo aquí abajo:
    df = pd.read_excel("Proverbios_agrupados.xlsx", sheet_name="Datos")
    
    # Limpieza básica: quitar espacios en blanco en los nombres de columnas
    df.columns = df.columns.str.strip()
    return df

try:
    df = cargar_datos()

    st.title("📖 Explorador de Proverbios")
    st.info("Descubre la sabiduría bíblica para los retos de hoy.")

    # 2. Selector de Categoría
    # Usamos 'Categoría' (con acento) si así está en tu Excel
    col_cat = 'Categoria' if 'Categoria' in df.columns else 'Categoría'
    
    categorias = sorted(df[col_cat].unique())
    cat_seleccionada = st.selectbox("1. Selecciona tu Categoría:", categorias)

    # Filtrar datos
    df_filtrado = df[df[col_cat] == cat_seleccionada]

    st.divider()
    st.subheader(f"Temas en: {cat_seleccionada}")

    # 3. Listado de Temas con Expanders y Tarjetas
    temas = sorted(df_filtrado['Tema'].unique())

    for tema in temas:
        versiculos = df_filtrado[df_filtrado['Tema'] == tema]
        
        # El título del expander muestra cuántos proverbios hay
        with st.expander(f"🔹 {tema} ({len(versiculos)})"):
            for index, row in versiculos.iterrows():
                # Formato de tarjeta con borde para cada proverbio
                with st.container(border=True):
                    st.caption(f"Cita: {row['Cita']}")
                    st.write(f"**{row['Texto']}**")

except Exception as e:
    st.error(f"Error al cargar la aplicación: {e}")
    st.warning("Revisa que el nombre del archivo Excel en GitHub coincida con el código.")
