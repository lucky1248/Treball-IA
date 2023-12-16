# translations.py

class Translations:
    def __init__(self):
        self.translations = {
            'Español': {
                'title': '¿Quién es cómo yo?',           
                'select': 'Selecciona',
                'sex' : 'Sexo:',
                'female': 'Mujer',
                'male': 'Hombre',
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
                'place_birth_5' : 'Resto del mundo'   
            },
            'Català': {
                'title': 'Qui és com jo?',           
                'select': 'Selecciona',
                'sex' : 'Sexe:',
                'female': 'Dona',
                'male': 'Home',
                'age' : 'Edad:',
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
                'place_birth_5' : 'Resta del món'                
            }
        }
        self.idioma = 'Català'

    def set_idioma(self, new_idioma):
        self.idioma = new_idioma

    def translate(self, key):
        return self.translations[self.idioma][key]

translations = Translations()
