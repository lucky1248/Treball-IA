import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filepath):
    df = pd.read_csv(filepath)
    df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')
    df['Valor'] = df['Valor'].fillna(0)    
    return df

def filter_data(df, sex, age, district, neighborhood, education):
    # Apply filters based on user selection
    filtered_df = df.copy()

    if sex[0] > 0:
        filtered_df = filtered_df[filtered_df['SEXE'] == sex[0]]
    if age > 0:
        filtered_df = filtered_df[filtered_df['EDAT_1'] == age]
    
    # Add more filters
    return filtered_df

def plot_age_distribution(filtered_df):
    plt.figure(figsize=(10, 6))
    sns.histplot(filtered_df['EDAT_1'], bins=30, kde=True)
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Count')
    return plt
"""
def calculate_similarity_percentage(df, user_sex, user_age, user_district, user_neighborhood):
    # Filter based on user inputs
    filtered_df = df[
        (df['SEXE'] == user_sex[0]) &
        (df['EDAT_1'] == user_age) &
        (df['Codi_Districte'] == user_district[0]) &
        (df['Codi_Barri'] == user_neighborhood[0])
    ]

    # Calculate the total number of people in the dataset and the number in the filtered dataset
    total_people = df.shape[0]
    similar_people = filtered_df.shape[0]

    # Calculate the percentage
    if total_people > 0:
        percentage = (similar_people / total_people) * 100
    else:
        percentage = 0

    return percentage
"""

def filter_data_sex(df, user_sex):
    return df[(df['SEXE'] == user_sex)]    

def filter_data_age(df, user_age):
    return df[(df['EDAT_1'] == user_age)]    

def filter_data_district(df, user_district):
    return df[(df['Codi_Districte'] == user_district)] 

def filter_data_neighborhood(df, user_neighborhood):
    return df[(df['Codi_Barri'] == user_neighborhood)] 

def filter_data_placebirth(df, user_placebirth):
    return df[(df['LLOC_NAIX'] == user_placebirth)]    

def filter_data_ccaa(df, user_ccaa):
    return df[(df['LLOC_NAIX_CCAA'] == user_ccaa)]    

def filter_data_continent(df, user_continent):
    return df[(df['LLOC_NAIX_CONTINENT'] == user_continent)] 

def filter_data_education(df, user_education):
    return df[(df['NIV_EDUCA_esta'] == user_education)] 

def calculate_similarity_percentage(df, filtered_df, extra = 0):
    # Calculate the total number of people in the dataset and the number in the filtered dataset
    total_people = df['Valor'].sum()
    similar_people = filtered_df['Valor'].sum()
    similar_people += extra
    # Calculate the percentage
    if total_people > 0:
        percentage = (similar_people / total_people) * 100
    else:
        percentage = 0
    return (percentage, similar_people)

def calculate_similarity_percentage_sex(df, user_sex):
    filtered_df = filter_data_sex(df, user_sex[0])
    return calculate_similarity_percentage(df, filtered_df)

def calculate_similarity_percentage_age(df, user_age):
    filtered_df = filter_data_age(df, user_age)
    return calculate_similarity_percentage(df, filtered_df)

def calculate_similarity_percentage_district(df, user_district):
    filtered_df = filter_data_district(df, user_district[0])
    return calculate_similarity_percentage(df, filtered_df)

def calculate_similarity_percentage_neighborhood(df, user_neighborhood):
    filtered_df = filter_data_neighborhood(df, user_neighborhood[0])
    return calculate_similarity_percentage(df, filtered_df)

def calculate_similarity_percentage_placebirth(df_1, df_2, user_placebirth):
    filtered_df_2 = filter_data_placebirth(df_2, user_placebirth[0])
    return calculate_similarity_percentage(df_1, filtered_df_2)

def calculate_similarity_percentage_ccaa(df_1, df_2, user_ccaa):
    filtered_df_2 = filter_data_ccaa(df_2, user_ccaa[0])
    return calculate_similarity_percentage(df_1, filtered_df_2)

def calculate_similarity_percentage_continent(df_1, df_2, user_continent):
    filtered_df_2 = filter_data_continent(df_2, user_continent[0])
    return calculate_similarity_percentage(df_1, filtered_df_2)

def calculate_similarity_percentage_education(df_1, df_2, user_education):
    filtered_df_2 = filter_data_education(df_2, user_education[0])
    if(user_education[0] == 1):
        return calculate_similarity_percentage(df_1, filtered_df_2, 227298)
    else:
        return calculate_similarity_percentage(df_1, filtered_df_2)

def calculate_similarity_percentage_total(df_1, user_sex, user_age, user_district, user_neighborhood):
    filtered_df1 = df_1
    if(user_sex[0] != 0):
        filtered_df1 = filter_data_sex(filtered_df1, user_sex[0])
    if(user_age != -1):
        filtered_df1 = filter_data_age(filtered_df1, user_age)
    if(user_district[0] != 0):
        filtered_df1 = filter_data_district(filtered_df1, user_district[0])
    if(user_neighborhood[0] != 0):
        filtered_df1 = filter_data_neighborhood(filtered_df1, user_neighborhood[0])
    return calculate_similarity_percentage(df_1, filtered_df1)


