# translations.py

class Translations:
    def __init__(self):
        self.translations = {
            'Español': {
                'title': '¿Quién es cómo yo?',
                'main': 'Personas similares a ti',
                'data_analysis': 'Análisis de datos',           
                'select': 'Selecciona',
                'sex' : 'Sexo:',
                'female': 'Mujer',
                'Female': 'Mujer',
                'male': 'Hombre',
                'Male': 'Hombre',
                'age' : 'Edad:',
                'district' : 'Distrito:',
                'neighborhood' : 'Barrio:',
                'education' : 'Nivel Educativo:',
                'education_1' : 'Sin estudios',
                'education_2' : 'Estudios primarios, certificado de escolaridad, EGB',
                'education_3' : 'Bachillerato elemental, graduado escolar, ESO, FPI',
                'education_4' :'Bachillerato superior, BUP, COU, FPII, CFGM grado medio',
                'education_5' :'Estudios universitarios, CFGS grado superior',
                'place_birth' : 'Lugar de Nacimiento:',
                'place_birth_1' : 'Barcelona ciudad',
                'place_birth_2' : 'Resto de Cataluña',
                'place_birth_3' : 'Resto d España',
                'place_birth_4' : 'Resto de la Unión Europea',
                'place_birth_5' : 'Resto del mundo',    
                'lloc_naix_ccaa' : 'Comunidad Autónoma de Nacimiento:',
                'lloc_naix_continent' : 'Continente de Nacimiento:',
                'analyze' : 'Analizar',
                'analysis_results' : 'Resultados del Análisis',
                'based_on_profile' : 'Basado en tu perfil:',
                'percentage_of_similar_people' : 'Porcentaje de personas similares en el dataset:',
                'success_message' : '¡Tu perfil se ha analizado correctamente!',
                'not_specified' : 'No especificado',
                'select_district' : 'Selecciona un distrito',
                'district_gender' : 'Distribución de género por distrito',
            },
            'Català': {
                'title': 'Qui és com jo?',
                'main': 'Persones similars a tu',
                'data_analysis': 'Anàlisi de dades',           
                'select': 'Selecciona',
                'sex' : 'Sexe:',
                'female': 'Dona',
                'Female': 'Dona',
                'male': 'Home',
                'Male': 'Home',
                'age' : 'Edat:',
                'district' : 'Districte:',
                'neighborhood' : 'Barri:',
                'education' : 'Nivell Educatiu:',
                'education_1' : 'Sense estudis',
                'education_2' : 'Estudis primaris, certificat d\'escolaritat, EGB',
                'education_3' : 'Batxillerat elemental, graduat escolar, ESO, FPI',
                'education_4' :'Batxillerat superior, BUP, COU, FPII, CFGM grau mitjà',
                'education_5' :'Estudis universitaris, CFGS grau superior',
                'place_birth' : 'Lloc de Naixement:',
                'place_birth_1' : 'Barcelona ciutat',
                'place_birth_2' : 'Resta de Catalunya',
                'place_birth_3' : 'Resta d Espanya',
                'place_birth_4' : 'Resta de la Unió Europea',
                'place_birth_5' : 'Resta del món',    
                'lloc_naix_ccaa' : 'Comunitat Autònoma de Naixement:',
                'lloc_naix_continent' : 'Continent de Naixement:',
                'analyze' : 'Analitzar',
                'analysis_results' : 'Resultats de l\'anàlisi',
                'based_on_profile' : 'Basat en el teu perfil:',
                'percentage_of_similar_people' : 'Percentatge de persones similars en el dataset:',
                'success_message' : 'El teu perfil s\'ha analitzat correctament!',
                'not_specified' : 'No especificat',
                'select_district' : 'Selecciona un districte',
                'district_gender' : 'Distribució de gènere per districte'          
            }
        }
        self.idioma = 'Català'

    def set_idioma(self, new_idioma):
        self.idioma = new_idioma

    def translate(self, key):
        return self.translations[self.idioma][key]

translations = Translations()
