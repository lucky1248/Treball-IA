import streamlit as st
from translations import translations


# Language buttons
col1, col2 = st.columns(2)
with col1:
    if st.button('Español'):
        translations.set_idioma('Español')
        st.rerun()
with col2:
    if st.button('Català'):
        translations.set_idioma('Català')
        st.rerun()

# Title
st.title(translations.translate('title'))

# Sex selection
sex_options = [
    (0, translations.translate('select')),
    (1, translations.translate('female')),
    (2, translations.translate('male'))]
sex = st.selectbox(translations.translate('sex'), sex_options, format_func=lambda x: x[1])

# Age selection
age = st.slider(translations.translate('age'), 0, 100, value = 0, step = 1)

# Location selection
district_options = [
    (0, translations.translate('select')),
    (1, 'Ciutat Vella'),
    (2, 'Eixample'),
    (3, 'Sants - Montjuïc'),
    (4, 'Les Corts'),
    (5, 'Sarrià - Sant Gervasi'),
    (6, 'Gràcia'),
    (7, 'Horta - Guinardó'),
    (8, 'Nou Barris'),
    (9, 'Sant Andreu'),
    (10, 'Sant Martí')]
district = st.selectbox(translations.translate('district'), district_options, format_func=lambda x: x[1])

district_options = {
    1: ['Barrio1_Distrito1', 'Barrio2_Distrito1', 'Barrio3_Distrito1'],
    2: ['Barrio1_D', 'Barritrito2', 'Barririto2'],
    # ... Agrega el mapeo de barrios para cada distrito
}

filtered_barrios_options = barrios_options[district[0]]
st.title(filtered_barrios_options)

def get_filtered_barrios_options(selected_district):
    return barrios_options.get(selected_district, [])

# Filtrar opciones de barrios según el distrito seleccionado
filtered_barrios_options = get_filtered_barrios_options(district)

selected_barrio = st.selectbox(translations.translate('neighborhood'), filtered_barrios_options)

# Puedes utilizar selected_district y selected_barrio como desees en tu aplicación
# Education level selection
education_options = [
    (0, translations.translate('select')),
    (1, 'education_1'),
    (2, 'education_2'),
    (3, 'education_3'),
    (4, 'education_4'),
    (5, 'education_5')]
education = st.selectbox(translations.translate('education'), education_options, format_func=lambda x: x[1])
