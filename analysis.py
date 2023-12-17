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

def calculate_similarity_percentage(df, filtered_df):
    # Calculate the total number of people in the dataset and the number in the filtered dataset
    total_people = df['Valor'].sum()
    similar_people = filtered_df['Valor'].sum()
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

