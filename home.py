import altair
import streamlit as st
from translations import translations
import analysis
import pandas as predicted_gender
import pandas as pd
import seaborn as sns
import os

import model

# Load data
df_1 = analysis.load_data('datasets/2023_pad_mdba_sexe_edat-1.csv')
df_2 = analysis.load_data('datasets/2023_pad_mdb_lloc-naix_edat-q_sexe.csv')
df_3 = analysis.load_data('datasets/2023_pad_mdbas_lloc-naix-ccaa_sexe.csv')
df_4 = analysis.load_data('datasets/2023_pad_mdb_lloc-naix-continent_edat-q_sexe.csv')
df_5 = analysis.load_data('datasets/2023_pad_mdb_niv-educa-esta_edat-q_sexe.csv')


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

st.write(translations.translate('text_inici'))
st.write("https://opendata-ajuntament.barcelona.cat/data/ca/organization/poblacio")

# Create tabs
tab1, tab2 = st.tabs([translations.translate('main'), translations.translate('data_analysis')])
st.markdown(
    """
    <style>
        .stSelectbox label {
            font-weight: bold;
            color: red;
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
        .stSlider label {
            font-weight: bold;
            color: red;
        }
    </style>
    """,
    unsafe_allow_html=True
)

with tab1:
    st.write(translations.translate('text_inici_tab_1'))
    st.subheader(translations.translate('introduce_data'))
    st.write(translations.translate('introduce_data_or'))
    # Sex selection
    sex_options = [
        (0, translations.translate('select')),
        (1, translations.translate('female')),
        (2, translations.translate('male'))]

    SEXE = st.selectbox(translations.translate('sex'), sex_options, format_func=lambda x: x[1])
    
    if(SEXE[0] != 0):
        (percentage_sex, number_sex) =  analysis.calculate_similarity_percentage_sex(df_1, SEXE)
        # Percentage and number of similar people in the dataset
        st.markdown(f"🚀 **{translations.translate('number_of_similar_people_sex')}** `{int(number_sex)}`")
        st.markdown(f"📊 **{translations.translate('percentage_of_similar_people_sex')}** `{percentage_sex:.3f}%`")


    # Age selection
    EDAT_1 = st.slider(translations.translate('age'), -1, 100, value = -1, step = 1)
    st.markdown(f"*{translations.translate('age_explication_1')}*")
    st.markdown(f"*{translations.translate('age_explication_2')}*")

    EDAT_Q = EDAT_1 // 5
    
    if(EDAT_1 != -1):
        (percentage_age, number_age) =  analysis.calculate_similarity_percentage_age(df_1, EDAT_1)
        # Percentage and number of similar people in the dataset
        st.markdown(f"🚀 **{translations.translate('number_of_similar_people_age')}** `{int(number_age)}`")
        st.markdown(f"📊 **{translations.translate('percentage_of_similar_people_age')}** `{percentage_age:.3f}%`")


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

    if(CODI_DISTRICTE_DEST[0] != 0):
        (percentage_district, number_district) =  analysis.calculate_similarity_percentage_district(df_1, CODI_DISTRICTE_DEST)
        # Percentage and number of similar people in the dataset
        st.markdown(f"🚀 **{translations.translate('number_of_similar_people_district')}** `{int(number_district)}`")
        st.markdown(f"📊 **{translations.translate('percentage_of_similar_people_district')}** `{percentage_district:.3f}%`")

    CODI_BARRI_DEST = (0,'')
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

    if(CODI_BARRI_DEST[0] != 0):
        (percentage_neighborhood, number_neighborhood) =  analysis.calculate_similarity_percentage_neighborhood(df_1, CODI_BARRI_DEST)
        # Percentage and number of similar people in the dataset
        st.markdown(f"🚀 **{translations.translate('number_of_similar_people_neighborhood')}** `{int(number_neighborhood)}`")
        st.markdown(f"📊 **{translations.translate('percentage_of_similar_people_neighborhood')}** `{percentage_neighborhood:.3f}%`")


    # Place of Birth selection
    place_birth_options = [
        (0, translations.translate('select')),
        (1, translations.translate('place_birth_1')),
        (2, translations.translate('place_birth_2')),
        (3, translations.translate('place_birth_3')),
        (4, translations.translate('place_birth_4')),
        (5, translations.translate('place_birth_5'))]
    LLOC_NAIX = st.selectbox(translations.translate('place_birth'), place_birth_options, format_func=lambda x: x[1])

    if(LLOC_NAIX[0] != 0):
        (percentage_placebirth, number_placebirth) =  analysis.calculate_similarity_percentage_placebirth(df_1, df_2, LLOC_NAIX)
        # Percentage and number of similar people in the dataset
        st.markdown(f"🚀 **{translations.translate('number_of_similar_people_placebirth')}** `{int(number_placebirth)}`")
        st.markdown(f"📊 **{translations.translate('percentage_of_similar_people_placebirth')}** `{percentage_placebirth:.3f}%`")

    place_birth_advanced_options = {
        3: [(0, translations.translate('select')), (1, 'Andalusia'), (2, 'Aragó'), (3, 'Principat d Astúries'), (4, 'Illes Balears'), (5, 'Canàries'), (6, 'Cantàbria'), (7, 'Castella i Lleò'), (8, 'Castella - la Manxa'), (9, 'Catalunya'), (10, 'Comunitat Valenciana'), (11, 'Extremadura'), (12, 'Galícia'), (13, 'Comunitat de Madrid'), (14, 'Regió de Murcia'), (15, 'Comunitat Foral de Navarra'), (16, 'País Basc'), (17, 'La Rioja'), (18, 'Ceuta'), (19, 'Melilla')],
        5: [(0, translations.translate('select')), (1, 'Àfrica'), (2, 'Amèrica'), (3, 'Àsia'), (4, 'Europa'), (5, 'Oceania')]}
    LLOC_NAIX_CCAA = (0,0)
    LLOC_NAIX_CONTINENT = (0,0)

    if LLOC_NAIX[0] == 1:
        LLOC_NAIX_CCAA = (9, 'Catalunya')
        LLOC_NAIX_CONTINENT = (4, 'Europa')
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

    if(LLOC_NAIX[0] == 3 and LLOC_NAIX_CCAA[0] != 0):
        (percentage_ccaa, number_ccaa) =  analysis.calculate_similarity_percentage_ccaa(df_1, df_3, LLOC_NAIX_CCAA)
        # Percentage and number of similar people in the dataset
        st.markdown(f"🚀 **{translations.translate('number_of_similar_people_ccaa')}** `{int(number_ccaa)}`")
        st.markdown(f"📊 **{translations.translate('percentage_of_similar_people_ccaa')}** `{percentage_ccaa:.3f}%`")

    if(LLOC_NAIX[0] == 5 and LLOC_NAIX_CONTINENT[0] != 0):
        (percentage_continent, number_continent) =  analysis.calculate_similarity_percentage_continent(df_1, df_4, LLOC_NAIX_CONTINENT)
        # Percentage and number of similar people in the dataset
        st.markdown(f"🚀 **{translations.translate('number_of_similar_people_continent')}** `{int(number_continent)}`")
        st.markdown(f"📊 **{translations.translate('percentage_of_similar_people_continent')}** `{percentage_continent:.3f}%`")


    # Education level selection
    education_options = [
        (0, translations.translate('select')),
        (1, translations.translate('education_1')),
        (2, translations.translate('education_2')),
        (3, translations.translate('education_3')),
        (4, translations.translate('education_4')),
        (5, translations.translate('education_5'))]
    NIV_EDUCA_esta = st.selectbox(translations.translate('education'), education_options, format_func=lambda x: x[1])
    st.markdown(f"*{translations.translate('education_explication')}*")

    if(NIV_EDUCA_esta[0] != 0):
        (percentage_education, number_education) =  analysis.calculate_similarity_percentage_education(df_1, df_5, NIV_EDUCA_esta)
        # Percentage and number of similar people in the dataset
        st.markdown(f"🚀 **{translations.translate('number_of_similar_people_education')}** `{int(number_education)}`")
        st.markdown(f"📊 **{translations.translate('percentage_of_similar_people_education')}** `{percentage_education:.3f}%`")


    # Total analysis
    st.subheader(translations.translate('analysis_results'))
    (percentage_total, number_total) =  analysis.calculate_similarity_percentage_total(df_1, df_2, df_3, df_4, df_5, SEXE, EDAT_1, EDAT_Q, CODI_DISTRICTE_DEST, CODI_BARRI_DEST, LLOC_NAIX, LLOC_NAIX_CCAA, LLOC_NAIX_CONTINENT, NIV_EDUCA_esta)
    st.markdown(f"🚀 **{translations.translate('number_of_similar_people_total')}** `{int(number_total)}`")
    st.markdown(f"📊 **{translations.translate('percentage_of_similar_people_total')}** `{percentage_total:.5f}%`")
    if number_total == 0:
        st.warning(translations.translate('analysis_results_1'))
    elif number_total == 1:
        st.success(translations.translate('analysis_results_2'))
    elif number_total <= 5:
        st.success(translations.translate('analysis_results_3'))
    elif number_total <= 10:
        st.info(translations.translate('analysis_results_4'))
    elif number_total <= 20:
        st.info(translations.translate('analysis_results_5'))
    elif number_total <= 50:
        st.warning(translations.translate('analysis_results_6'))
    else:
        st.warning(translations.translate('analysis_results_7'))

### Data analysis ###
with tab2:
    # Predict gender
    if os.path.exists('gender_models.pkl') and os.path.exists('gender_district_encoder.pkl') and os.path.exists('gender_neighborhood_encoder.pkl'):
        gender_model, district_encoder, neighborhood_encoder = model.load_gender_models_and_encoders()

        df_merged = pd.read_csv('datasets/merged_gender_data.csv')
    else:
        X, y, df_merged, district_encoder, neighborhood_encoder = model.load_gender_model()

        # Save df_merged for later use
        df_merged.to_csv('datasets/merged_gender_data.csv', index=False)

        gender_model = model.train_gender_model(X, y)
        model.save_gender_models_and_encoders(gender_model, district_encoder, neighborhood_encoder)
    st.header(translations.translate('prediction_gender'))

    # District selection
    district_options = district_encoder.classes_
    selected_district = st.selectbox(translations.translate('district'), district_options)

    # Neighborhood selection based on district
    filtered_neighborhoods = df_merged[df_merged['Nom_Districte'] == selected_district]['Nom_Barri'].unique()
    selected_neighborhood = st.selectbox(translations.translate('neighborhood'), filtered_neighborhoods)

    # Age selection
    age = st.number_input(translations.translate('age'), min_value=0, max_value=100, value=25)
    age_group = age // 5  # Mapping age to quinquennial group

    # Education level selection
    education_options = [
        (0, translations.translate('select')),
        (1, translations.translate('education_1')),
        (2, translations.translate('education_2')),
        (3, translations.translate('education_3')),
        (4, translations.translate('education_4')),
        (5, translations.translate('education_5'))]
    # Education level selection for gender prediction
    selected_education_gender = st.selectbox(translations.translate('education'), education_options, format_func=lambda x: x[1], key="education_select_gender")

    # Encoding user inputs
    encoded_district = district_encoder.transform([selected_district])[0]
    encoded_neighborhood = neighborhood_encoder.transform([selected_neighborhood])[0]
    selected_education_int = int(selected_education_gender[0])

    if st.button(translations.translate('predict')):
        prediction = gender_model.predict([[encoded_district, encoded_neighborhood, age_group, selected_education_int]])
        predicted_gender = translations.translate('male') if prediction[0] == 1 else translations.translate('female')
        st.success(f'{translations.translate("predicted_gender")} {predicted_gender}')


    # Predict lifespan
    if os.path.exists('lifespan_models.pkl') and os.path.exists('lifespan_district_encoder.pkl') and os.path.exists('lifespan_neighborhood_encoder.pkl'):
        models, district_encoder, neighborhood_encoder = model.load_lifespan_models_and_encoders()
    else:
        X, df_merged, district_encoder, neighborhood_encoder = model.load_lifespan_model()
        models = model.train_lifespan_models(X, df_merged)
        model.save_lifespan_models_and_encoders(models, district_encoder, neighborhood_encoder)
    st.header(translations.translate('life_expectancy_prediction'))

    # Gender selection
    gender_options = {
        'Male': 2,
        'Female': 1
    }
    selected_gender = st.selectbox("Gènere", list(gender_options.keys()))
    encoded_gender = gender_options[selected_gender]

    # District selection
    district_options = district_encoder.classes_
    selected_district = st.selectbox("Districte", district_options)

    # Neighborhood selection based on district
    filtered_neighborhoods = df_merged[df_merged['Nom_Districte'] == selected_district]['Nom_Barri'].unique()
    selected_neighborhood = st.selectbox("Barri", filtered_neighborhoods)

    # Age selection
    age = st.number_input("Edat", min_value=0, max_value=100, value=25)
    age_group = age // 5  # Mapping age to quinquennial group

    # Education level selection
    education_options = [
        (0, translations.translate('select')),
        (1, translations.translate('education_1')),
        (2, translations.translate('education_2')),
        (3, translations.translate('education_3')),
        (4, translations.translate('education_4')),
        (5, translations.translate('education_5'))]
    selected_education_lifespan = st.selectbox(translations.translate('education'), education_options, format_func=lambda x: x[1], key="education_select_lifespan")

    # Encoding user inputs
    encoded_district = district_encoder.transform([selected_district])[0]
    encoded_neighborhood = neighborhood_encoder.transform([selected_neighborhood])[0]
    selected_education_int = int(selected_education_lifespan[0])

    if st.button(translations.translate('predict'), key="predict_lifespan"):
        input_features = [encoded_district, encoded_neighborhood, selected_education_int, encoded_gender]
        predicted_age_group_min, predicted_age_group_max = model.predict_lifespan(models, input_features)
        st.success(f'{translations.translate("predicted_age")} {predicted_age_group_min}-{predicted_age_group_max} {translations.translate("years")}')


    # Custom styles for charts
    sns.set(style="whitegrid")

    # 1. Population Distribution by District and Neighborhood
    st.header(translations.translate('population_distribution'))
    col1, col2 = st.columns(2)
    with col1:
        selected_district = st.selectbox(translations.translate('select_district'), df_1['Nom_Districte'].unique())

    population_district = df_1[df_1['Nom_Districte'] == selected_district].groupby('Nom_Barri').size().reset_index(name='Population')
    bar_chart = altair.Chart(population_district).mark_bar().encode(
        x=altair.X('Nom_Barri:N', title=translations.translate('neighborhood_name')),
        y=altair.Y('Population:Q', title=translations.translate('population')),
        color='Nom_Barri:N',
        tooltip=[altair.Tooltip('Nom_Barri:N', title=translations.translate('neighborhood_name')), 
                altair.Tooltip('Population:Q', title=translations.translate('population'))]
    ).interactive()

    st.altair_chart(bar_chart, use_container_width=True)

    # 3. Statistical Summary of Each Neighborhood
    st.subheader(translations.translate('statistical_summary_for_each_neighborhood'))
    district_stat = st.selectbox(translations.translate('select_district'), df_1['Nom_Districte'].unique(), key='district_stat')
    neighborhood_stat = st.selectbox(translations.translate('select_neighborhood'), df_1[df_1['Nom_Districte'] == district_stat]['Nom_Barri'].unique(), key='neighborhood_stat')
    summary_stats = df_1[(df_1['Nom_Districte'] == district_stat) & (df_1['Nom_Barri'] == neighborhood_stat)]['EDAT_1'].describe()

    st.markdown(f"""
        <style>
        .stats-card {{
            background-color: #f8f9fa;
            border-left: 5px solid #2a9d8f;
            padding: 15px;
            margin: 5px 0;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }}
        .stats-card h4 {{
            color: #495057;
            font-size: 1.2em; /* Smaller font size for the title */
            margin-bottom: 10px;
        }}
        .stats-card p {{
            color: #495057;
            font-size: 1em; /* Smaller font size for the content */
            margin: 3px 0; /* Less space between lines */
        }}
        .stats-card p strong {{
            display: block;
            color: #212529;
            font-size: 1.1em; /* Slightly larger font size for the key terms */
            margin-bottom: 3px; /* Less space below key terms */
        }}
        </style>
        <div class="stats-card">
            <h4>{translations.translate('summary_statistics')}</h4>
            <p><strong>{translations.translate('mean_age')}:</strong> {summary_stats['mean']:.2f} {translations.translate('years')}</p>
            <p><strong>{translations.translate('median_age')}:</strong> {summary_stats['50%']:.2f} {translations.translate('years')}</p>
            <p><strong>{translations.translate('standard_deviation')}:</strong> {summary_stats['std']:.2f} {translations.translate('years')}</p>
            <p><strong>{translations.translate('minimum_age')}:</strong> {summary_stats['min']:.0f} {translations.translate('years')}</p>
            <p><strong>{translations.translate('maximum_age')}:</strong> {summary_stats['max']:.0f} {translations.translate('years')}</p>
            <p><strong>{translations.translate('percentile_25')}:</strong> {summary_stats['25%']:.2f} {translations.translate('years')}</p>
            <p><strong>{translations.translate('percentile_75')}:</strong> {summary_stats['75%']:.2f} {translations.translate('years')}</p>
            <p><strong>{translations.translate('count')}:</strong> {summary_stats['count']:.0f} {translations.translate('individuals')}</p>
        </div>
        """, unsafe_allow_html=True)
