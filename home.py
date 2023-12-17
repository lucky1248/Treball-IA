import altair
import streamlit as st
from translations import translations
import analysis
import pandas as pd
import geocoder
import seaborn as sns

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

# Create tabs
tab1, tab2 = st.tabs([translations.translate('main'), translations.translate('data_analysis')])

with tab1:

    # Sex selection
    sex_options = [
        (0, translations.translate('select')),
        (1, translations.translate('female')),
        (2, translations.translate('male'))]
    SEXE = st.selectbox(translations.translate('age'), sex_options, format_func=lambda x: x[1])
    
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
    (percentage_total, number_total) =  analysis.calculate_similarity_percentage_total(df_1, SEXE, EDAT_1, CODI_DISTRICTE_DEST, CODI_BARRI_DEST)
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


with tab2:
    # Custom styles for charts
    sns.set(style="whitegrid")

    # 1. Population Distribution by District and Neighborhood
    st.header("Population Distribution")
    col1, col2 = st.columns(2)
    with col1:
        selected_district = st.selectbox(translations.translate('select_district'), df_1['Nom_Districte'].unique())

    population_district = df_1[df_1['Nom_Districte'] == selected_district].groupby('Nom_Barri').size().reset_index(name='Population')
    bar_chart = altair.Chart(population_district).mark_bar().encode(
        x='Nom_Barri:N',
        y='Population:Q',
        color='Nom_Barri:N',
        tooltip=['Nom_Barri', 'Population']
    ).interactive()
    st.altair_chart(bar_chart, use_container_width=True)

    # 2. Gender Distribution Across Districts
    selected_district_gender = st.selectbox(translations.translate('district_gender'), df_1['Nom_Districte'].unique(), key='district_gender')
    gender_distribution = df_1[df_1['Nom_Districte'] == selected_district_gender].groupby('SEXE').size().reset_index(name='Count')
    gender_distribution['Gender'] = gender_distribution['SEXE'].map({1: 'Female', 2: 'Male'})
    st.bar_chart(gender_distribution.set_index('Gender')['Count'])

    # 3. Age Distribution in Neighborhoods
    st.subheader("Age Distribution in Neighborhoods")
    district_selected = st.selectbox('Select District', df_1['Nom_Districte'].unique(), key='district_age')
    neighborhood_selected = st.selectbox('Select Neighborhood', df_1[df_1['Nom_Districte'] == district_selected]['Nom_Barri'].unique(), key='neighborhood_age')
    age_distribution = df_1[(df_1['Nom_Districte'] == district_selected) & (df_1['Nom_Barri'] == neighborhood_selected)]['EDAT_1'].value_counts().sort_index()
    st.bar_chart(age_distribution)

    # 4. Comparison of Age Groups between Two Districts
    st.subheader("Comparison of Age Groups between Two Districts")
    district1 = st.selectbox('Select First District', df_1['Nom_Districte'].unique(), key='first_district')
    district2 = st.selectbox('Select Second District', df_1['Nom_Districte'].unique(), key='second_district')
    age_group_comparison = pd.DataFrame({
        district1: df_1[df_1['Nom_Districte'] == district1]['EDAT_1'].value_counts().sort_index(),
        district2: df_1[df_1['Nom_Districte'] == district2]['EDAT_1'].value_counts().sort_index()
    })
    st.bar_chart(age_group_comparison)

    # 5. Aggregated Data by Gender and Age Group
    st.subheader("Aggregated Data by Gender and Age Group")
    min_age, max_age = st.slider("Select Age Range", 0, 100, (0, 100), key='age_range')
    df_1['Gender'] = df_1['SEXE'].map({1: 'Female', 2: 'Male'})  # Map gender values
    age_gender_aggregation = df_1[(df_1['EDAT_1'] >= min_age) & (df_1['EDAT_1'] <= max_age)].groupby(['Gender', pd.cut(df_1['EDAT_1'], bins=[0, 18, 35, 60, 100], labels=['0-18', '19-35', '36-60', '60+'])]).size().unstack().fillna(0)
    st.table(age_gender_aggregation)

    # 6. Interactive Map of Population Density
    st.subheader("Interactive Map of Population Density")

    # Initialize a list to hold the map data
    map_data_list = []

    # Iterate through each district and neighborhood
    for district in df_1['Nom_Districte'].unique():
        for neighborhood in df_1[df_1['Nom_Districte'] == district]['Nom_Barri'].unique():
            # Geocode the neighborhood name to get coordinates
            g = geocoder.osm(neighborhood + ', ' + district)
            if g.ok:
                lat, lon = g.latlng
                population = df_1[(df_1['Nom_Districte'] == district) & (df_1['Nom_Barri'] == neighborhood)].shape[0]
                # Append data to the list
                map_data_list.append({'lat': lat, 'lon': lon, 'Population': population})

    # Convert the list to a DataFrame
    map_data = pd.DataFrame(map_data_list)

    # Display the map
    st.map(map_data)

    # 7. Statistical Summary of Each Neighborhood
    st.subheader("Statistical Summary of Each Neighborhood")
    district_stat = st.selectbox('Select District for Statistics', df_1['Nom_Districte'].unique(), key='district_stat')
    neighborhood_stat = st.selectbox('Select Neighborhood for Statistics', df_1[df_1['Nom_Districte'] == district_stat]['Nom_Barri'].unique(), key='neighborhood_stat')
    summary_stats = df_1[(df_1['Nom_Districte'] == district_stat) & (df_1['Nom_Barri'] == neighborhood_stat)]['EDAT_1'].describe()

    # Enhancing the display of statistical summary
    st.markdown("#### Summary Statistics")
    st.markdown(f"**Mean Age:** {summary_stats['mean']:.2f} years")
    st.markdown(f"**Median Age:** {summary_stats['50%']:.2f} years")
    st.markdown(f"**Standard Deviation:** {summary_stats['std']:.2f} years")
    st.markdown(f"**Minimum Age:** {summary_stats['min']:.0f} years")
    st.markdown(f"**Maximum Age:** {summary_stats['max']:.0f} years")
    st.markdown(f"**25th Percentile Age:** {summary_stats['25%']:.2f} years")
    st.markdown(f"**75th Percentile Age:** {summary_stats['75%']:.2f} years")
    st.markdown(f"**Count:** {summary_stats['count']:.0f} individuals")
