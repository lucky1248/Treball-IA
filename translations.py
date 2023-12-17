# translations.py

class Translations:
    def __init__(self):
        self.translations = {
            'Español': {
                'title': 'Datos de Barcelona',
                'main': 'Personas similares a ti',
                'data_analysis': 'Análisis de datos generales',           
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
                'analysis_results' : 'Con los datos seleccionados...',
                'analysis_results_1' : '🌟 ¡Increíble! Eres tan único que ni existes en nuestra base de datos. ¡Eres una rareza extraordinaria!',
                'analysis_results_2' : '🎉 ¡Enhorabuena! Estás más solo que un pingüino en el desierto.',
                'analysis_results_3' : '👥 No está mal, ¡has encontrado unos pocos clones!',
                'analysis_results_4' : '👍 Tienes más coincidencias que un juego de memoria. ¡Bien hecho!',
                'analysis_results_5' : '🔍 Estás en modo detective, ¡has encontrado un buen número de sospechosos!',
                'analysis_results_6' : '🧬 ¡Alerta de clonación masiva! Parece que tienes muchos gemelos perdidos.',
                'analysis_results_7' : '🚨 ¡Houston, tenemos un problema! ¡Demasiadas coincidencias, cuidado con el caos!',
                'based_on_profile' : 'Basado en tu perfil:',
                'percentage_of_similar_people' : 'Porcentaje de personas similares en el dataset:',
                'success_message' : '¡Tu perfil se ha analizado correctamente!',
                'not_specified' : 'No especificado',
                'select_district' : 'Selecciona un distrito',
                'district_gender' : 'Distribución de género por distrito',
                'percentage_of_similar_people_sex' : 'Porcentaje de personas con el mismo sexo que tu:',
                'number_of_similar_people_sex' : 'Número de personas con el mismo sexo que tu:',  
                'percentage_of_similar_people_age' : 'Porcentaje de personas con la misma edat que tu:',
                'number_of_similar_people_age' : 'Número de personas con la misma edat que tu:',                                
                'percentage_of_similar_people_district' : 'Porcentaje de personas que viven en el mismo distrito que tu:',
                'number_of_similar_people_district' : 'Número de personas que viven en el mismo distrito que tu:',
                'percentage_of_similar_people_neighborhood' : 'Porcentaje de personas que viven en el mismo barrio que tu:',
                'number_of_similar_people_neighborhood' : 'Número de personas que viven en el mismo barrio que tu:',            
                'percentage_of_similar_people_total' : 'Porcentaje de personas como tu:',
                'number_of_similar_people_total' : 'Número de personas como tu:', 
            },
            'Català': {
                'title': 'Dades de Barcelona',
                'main': 'Persones similars a tu',
                'data_analysis': 'Anàlisi de dades generals',           
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
                'analysis_results' : 'Amb les dades selecccionades...',
                'analysis_results_1' : '🌟 Increíble! Ets tan únic que ni existeixes a la nostra base de dades. Ets una raresa extraordinaria!',
                'analysis_results_2' : '🎉 Enhorabona! Estàs més sol que un pingüí en el desert.',
                'analysis_results_3' : '👥 No està malament, has trobat uns pocs clons!',
                'analysis_results_4' : '👍 Tens més coincidencies que un joc de memòria. Ben fet!',
                'analysis_results_5' : '🔍 Estàs en mode detectiu, has trobat un bon nombre de sospitosos!',
                'analysis_results_6' : '🧬 Alerta de clonació massiva! Sembla que tens molts bessons perduts.',
                'analysis_results_7' : '🚨 Houston, tenim un problema! Masses coincidencies, cuidado amb el caos!',                
                'based_on_profile' : 'Basat en el teu perfil:',
                'percentage_of_similar_people' : 'Percentatge de persones similars en el dataset:',
                'success_message' : 'El teu perfil s\'ha analitzat correctament!',
                'not_specified' : 'No especificat',
                'select_district' : 'Selecciona un districte',
                'district_gender' : 'Distribució de gènere per districte',
                'percentage_of_similar_people_sex' : 'Percentatge de persones amb el mateix sexe que tu:',
                'number_of_similar_people_sex' : 'Nombre de persones amb el mateix sexe que tu:',                
                'percentage_of_similar_people_age' : 'Percentatge de persones amb la mateixa edat que tu:',
                'number_of_similar_people_age' : 'Nombre de persones amb la mateixa edat que tu:',                                         
                'percentage_of_similar_people_district' : 'Percentatge de persones que viuen al mateix districte que tu:',
                'number_of_similar_people_district' : 'Nombre de persones que viuen al mateix districte que tu:',  
                'percentage_of_similar_people_neighborhood' : 'Percentatge de persones que viuen al mateix barri que tu:',
                'number_of_similar_people_neighborhood' : 'Nombre de persones que viuen al mateix barri que tu:', 
                'percentage_of_similar_people_total' : 'Percentatge de persones com tu:',
                'number_of_similar_people_total' : 'Nombre de persones com tu:', 
            }
        }
        self.idioma = 'Català'

    def set_idioma(self, new_idioma):
        self.idioma = new_idioma

    def translate(self, key):
        return self.translations[self.idioma][key]

translations = Translations()
