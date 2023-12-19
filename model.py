import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

def save_gender_models_and_encoders(gender_models, district_encoder, neighborhood_encoder):
    with open('gender_models.pkl', 'wb') as f:
        pickle.dump(gender_models, f)
    
    with open('gender_district_encoder.pkl', 'wb') as f:
        pickle.dump(district_encoder, f)

    with open('gender_neighborhood_encoder.pkl', 'wb') as f:
        pickle.dump(neighborhood_encoder, f)

def load_gender_models_and_encoders():
    with open('gender_models.pkl', 'rb') as f:
        gender_models = pickle.load(f)

    with open('gender_district_encoder.pkl', 'rb') as f:
        district_encoder = pickle.load(f)

    with open('gender_neighborhood_encoder.pkl', 'rb') as f:
        neighborhood_encoder = pickle.load(f)

    return gender_models, district_encoder, neighborhood_encoder

def save_lifespan_models_and_encoders(lifespan_models, district_encoder, neighborhood_encoder):
    with open('lifespan_models.pkl', 'wb') as f:
        pickle.dump(lifespan_models, f)
    
    with open('lifespan_district_encoder.pkl', 'wb') as f:
        pickle.dump(district_encoder, f)

    with open('lifespan_neighborhood_encoder.pkl', 'wb') as f:
        pickle.dump(neighborhood_encoder, f)

def load_lifespan_models_and_encoders():
    with open('lifespan_models.pkl', 'rb') as f:
        lifespan_models = pickle.load(f)

    with open('lifespan_district_encoder.pkl', 'rb') as f:
        district_encoder = pickle.load(f)

    with open('lifespan_neighborhood_encoder.pkl', 'rb') as f:
        neighborhood_encoder = pickle.load(f)

    return lifespan_models, district_encoder, neighborhood_encoder

# Function to load and preprocess data, and train the model
def load_gender_model():
    # Load datasets
    df_main = pd.read_csv('datasets/2023_pad_mdb_niv-educa-esta_edat-q_sexe.csv')
    df_additional = pd.read_csv('datasets/2023_pad_mdb_lloc-naix_edat-q_sexe.csv')

    # Merging datasets on common columns
    df_merged = pd.merge(df_main, df_additional, on=['Nom_Districte', 'Nom_Barri', 'EDAT_Q', 'SEXE'], how='inner')

    # Feature Engineering
    district_encoder = LabelEncoder()
    neighborhood_encoder = LabelEncoder()
    df_merged['Nom_Districte_Encoded'] = district_encoder.fit_transform(df_merged['Nom_Districte'])
    df_merged['Nom_Barri_Encoded'] = neighborhood_encoder.fit_transform(df_merged['Nom_Barri'])

    # Selecting relevant columns
    X = df_merged[['Nom_Districte_Encoded', 'Nom_Barri_Encoded', 'EDAT_Q', 'NIV_EDUCA_esta']]
    y = df_merged['SEXE']

    return X, y, df_merged, district_encoder, neighborhood_encoder

# Function to train the model
def train_gender_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print('Model Accuracy:', accuracy)

    return model

def load_lifespan_model():
    # Load datasets
    df_main = pd.read_csv('datasets/2023_pad_mdb_niv-educa-esta_edat-q_sexe.csv')
    df_additional = pd.read_csv('datasets/2023_pad_mdb_lloc-naix_edat-q_sexe.csv')

    # Merging datasets on common columns
    df_merged = pd.merge(df_main, df_additional, on=['Nom_Districte', 'Nom_Barri', 'EDAT_Q', 'SEXE'], how='inner')

    # Feature Engineering
    district_encoder = LabelEncoder()
    neighborhood_encoder = LabelEncoder()
    df_merged['Nom_Districte_Encoded'] = district_encoder.fit_transform(df_merged['Nom_Districte'])
    df_merged['Nom_Barri_Encoded'] = neighborhood_encoder.fit_transform(df_merged['Nom_Barri'])

    # Selecting relevant columns
    X = df_merged[['Nom_Districte_Encoded', 'Nom_Barri_Encoded', 'NIV_EDUCA_esta', 'SEXE']]
    
    return X, df_merged, district_encoder, neighborhood_encoder

def train_lifespan_models(X, df_merged):
    max_age_group = df_merged['EDAT_Q'].max()
    models = {}

    for age_group in range(1, max_age_group + 1):
        y = (df_merged['EDAT_Q'] == age_group).astype(int)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Age Group {age_group}: Model Accuracy: {accuracy}")
        models[age_group] = model
    
    return models

def predict_lifespan(models, input_features):
    highest_probability = 0
    predicted_quinquennial_group = 1  # Default to the first group

    for age_group, model in models.items():
        probabilities = model.predict_proba([input_features])[0]

        # Handle the case where predict_proba returns only one column
        if len(probabilities) == 1:
            probability = 1 - probabilities[0]
        else:
            probability = probabilities[1]

        # Track the age group with the highest probability
        if probability > highest_probability:
            highest_probability = probability
            predicted_quinquennial_group = age_group

    # Ensure the predicted group is within valid range
    predicted_quinquennial_group = max(1, min(predicted_quinquennial_group, max(models.keys())))

    # Convert the predicted quinquennial group to a normal age range
    predicted_age_group_min = (predicted_quinquennial_group - 1) * 5
    predicted_age_group_max = predicted_age_group_min + 4

    return predicted_age_group_min, predicted_age_group_max
