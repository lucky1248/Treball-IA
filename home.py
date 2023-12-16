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
SEXE = st.selectbox(translations.translate('sex'), sex_options, format_func=lambda x: x[1])

# Age selection
EDAT_1 = st.slider(translations.translate('age'), 0, 100, value = 0, step = 1)
EDAT_Q = EDAT_1 // 5

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
CODI_DISTRICTE_DEST = st.selectbox(translations.translate('district'), district_options, format_func=lambda x: x[1])

neighborhood_options = {
    1: [(0, translations.translate('select')), (1, 'el Raval'), (2, 'el Barri Gòtic'), (3, 'la Barceloneta'), (4, 'Sant Pere, Santa Caterina i la Ribera')],
    2: [(0, translations.translate('select')), (5, 'el Fort Pienc'), (6, 'la Sagrada Familia'), (7, 'la Dreta de l Eixample'), (8, 'l Antiga Esquerra de l Eixample'), (9, 'la Nova Esquerra de l Eixample'), (10, 'Sant Antoni')],
    3: [(0, translations.translate('select')), (11, 'el Poble-sec'), (12, 'la Marina del Prat Vermell'), (13, 'la Marina de Port'), (14, 'la Font de la Guatlla'), (15, 'Hostafrancs'), (16, 'la Bordeta'), (17, 'Sants - Badal'), (18, 'Sants')],
    4: [(0, translations.translate('select')), (19, 'les Corts'), (20, 'la Maternitat i Sant Ramon'), (21, 'Pedralbes')],
    5: [(0, translations.translate('select')), (22, 'Vallvidrera, el Tibidabo i les Planes'), (23, 'Sarrià'), (24, 'les Tres Torres'), (25, 'Sant Gervasi - la Bonanova'), (26, 'Sant Gervasi - Galvany'), (27, 'el Putxet i el Farró')],
    6: [(0, translations.translate('select')), (28, 'Vallcarca i els Penitents'), (29, 'el Coll'), (30, 'la Salut'), (31, 'la Vila de Gràcia'), (32, 'el Camp d en Grassot i Gràcia Nova')],
    7: [(0, translations.translate('select')), (33, 'el Baix Guinardó'), (34, 'Can Baró'), (35, 'el Guinardó'), (36, 'la Font d en Fargues'), (37, 'el Carmel'), (38, 'la Teixonera'), (39, 'Sant Genís dels Agudells'), (40, 'Montbau'), (41, 'la Vall d Hebron'), (42, 'la Clota'), (43, 'Horta')],
    8: [(0, translations.translate('select')), (44, 'Vilapicina i la Torre Llobeta'), (45, 'Porta'), (46, 'el Turó de la Peira'), (47, 'Can Peguera'), (48, 'la Guineueta'), (50, 'les Roquetes'), (51, 'Verdun'), (52, 'la Prosperitat'), (53, 'la Trinitat Nova'), (54, 'Torre Baró'), (55, 'Ciutat Meridiana'), (56, 'Vallbona')],
    9: [(0, translations.translate('select')), (57, 'la Trinitat Vella'), (58, 'Baró de Viver'), (59, 'el Bon Pastor'), (60, 'Sant Andreu'), (61, 'la Sagrera'), (62, 'el Congrés i els Indians'), (63, 'Navas')],
    10: [(0, translations.translate('select')), (64, 'el Camp de l Arpa del Clot'), (65, 'el Clot'), (66, 'el Parc i la Llacuna del Poblenou'), (67, 'la Vila Olímpica del Poblenou'), (68, 'el Poblenou'), (69, 'Diagonal Mar i el Front Marítim del Poblenou'), (70, 'el Besòs i el Maresme'), (71, 'Provençals del Poblenou'), (72, 'Sant Martí de Provençals'), (73, 'la Verneda i la Pau')]}
if CODI_DISTRICTE_DEST[0] > 0:
    filtered_neighborhood_options = neighborhood_options[CODI_DISTRICTE_DEST[0]]
    CODI_BARRI_DEST = st.selectbox(translations.translate('neighborhood'), filtered_neighborhood_options, format_func=lambda x: x[1])

# Place of Birth selection
place_birth_options = [
    (0, translations.translate('select')),
    (1, translations.translate('place_birth_1')),
    (2, translations.translate('place_birth_2')),
    (3, translations.translate('place_birth_3')),
    (4, translations.translate('place_birth_4')),
    (5, translations.translate('place_birth_5'))]
LLOC_NAIX = st.selectbox(translations.translate('place_birth'), place_birth_options, format_func=lambda x: x[1])

place_birth_advanced_options = {
    3: [(0, translations.translate('select')), (1, 'Andalusia'), (2, 'Aragó'), (3, 'Principat d Astúries'), (4, 'Illes Balears'), (5, 'Canàries'), (6, 'Cantàbria'), (7, 'Castella i Lleò'), (8, 'Castella - la Manxa'), (9, 'Catalunya'), (10, 'Comunitat Valenciana'), (11, 'Extremadura'), (12, 'Galícia'), (13, 'Comunitat de Madrid'), (14, 'Regió de Murcia'), (15, 'Comunitat Foral de Navarra'), (16, 'País Basc'), (17, 'La Rioja'), (18, 'Ceuta'), (19, 'Melilla')],
    5: [(0, translations.translate('select')), (1, 'Àfrica'), (2, 'Amèrica'), (3, 'Àsia'), (4, 'Europa'), (5, 'Oceania')]}
if LLOC_NAIX[0] == 1:
    LLOC_NAIX_CCAA = (9, 'Catalunya')
    LLOC_NAIX_CONTINENT= (4, 'Europa')
elif LLOC_NAIX[0] == 2:
    LLOC_NAIX_CCAA = (9, 'Catalunya')
    LLOC_NAIX_CONTINENT = (4, 'Europa')
elif LLOC_NAIX[0] == 3:
    filtered_place_birth_advanced_options = place_birth_advanced_options[LLOC_NAIX[0]]
    LLOC_NAIX_CCAA = st.selectbox(translations.translate('lloc_naix_ccaa'), filtered_place_birth_advanced_options, format_func=lambda x: x[1])
    LLOC_NAIX_CONTINENT = (4, 'Europa')
elif LLOC_NAIX[0] == 4:
    LLOC_NAIX_CCAA = 0
    LLOC_NAIX_CONTINENT = (4, 'Europa')
elif LLOC_NAIX[0] == 5:
    LLOC_NAIX_CCAA = 0
    filtered_place_birth_advanced_options = place_birth_advanced_options[LLOC_NAIX[0]]
    LLOC_NAIX_CONTINENT = st.selectbox(translations.translate('lloc_naix_continent'), filtered_place_birth_advanced_options, format_func=lambda x: x[1])

# Education level selection
education_options = [
    (0, translations.translate('select')),
    (1, translations.translate('education_1')),
    (2, translations.translate('education_2')),
    (3, translations.translate('education_3')),
    (4, translations.translate('education_4')),
    (5, translations.translate('education_5'))]
NIV_EDUCA_esta = st.selectbox(translations.translate('education'), education_options, format_func=lambda x: x[1])
