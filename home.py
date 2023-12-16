import streamlit as st

# Title
st.title("Qui és com jo?")

# Sex selection
sex = st.selectbox("Sexe:", [('', 'Select'), (1, 'Dona'), (2, 'Home')], format_func=lambda x: x[1])

# Location input
location = st.text_input("Ubicació:")

# Age input
age = st.number_input("Edat:", min_value=0, max_value=150, step=1)

# Education level selection
education_options = [
    ('', 'Select'),
    (1, 'Sense estudis'),
    (2, 'Estudis primaris, certificat d\'escolaritat, EGB'),
    (3, 'Batxillerat elemental, graduat escolar, ESO, FPI'),
    (4, 'Batxillerat superior, BUP, COU, FPII, CFGM grau mitjà'),
    (5, 'Estudis universitaris, CFGS grau superior')
]
education = st.selectbox("Nivell Educatiu:", education_options, format_func=lambda x: x[1])

# Send button
if st.button('Enviar'):
    st.write("Dades enviades!")

# Language buttons
col1, col2 = st.columns(2)
with col1:
    if st.button('Español'):
        st.write("Idioma canviat a Espanyol")
with col2:
    if st.button('Català'):
        st.write("Idioma canviat a Català")
