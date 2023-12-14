function submitForm() {
    // Obtén los valores del formulario
    const location = document.getElementById('location').value;
    const age = document.getElementById('age').value;
    const gender = document.getElementById('gender').value;
    const education = document.getElementById('education').value;

    // Realiza acciones con los datos (puedes enviarlos al servidor, realizar cálculos, etc.)
    console.log('Ubicación:', location);
    console.log('Edad:', age);
    console.log('Género:', gender);
    console.log('Nivel Educativo:', education);

    // Aquí puedes realizar más acciones según tus necesidades
}

document.addEventListener('DOMContentLoaded', function() {
    // Inicializa el idioma predeterminado al cargar la página
    const defaultLanguage = 'ca';
    changeLanguage(defaultLanguage);
});

async function changeLanguage(lang){
    try {
        // Carga las traducciones
        const traductions = await cargarTraductions(lang);
        console.log('Traductions:', traductions);

        // Itera sobre las claves del objeto de traducciones
        for (const key in traductions) {
            if (traductions.hasOwnProperty(key)) {
                // Asigna el contenido traducido a los elementos con el ID correspondiente
                const element = document.getElementById(key);
                if (element) {
                    element.textContent = traductions[key];
                }
            }
        }
    } catch (error) {
        console.error('Error al cargar las traducciones:', error);
    }
}

function cargarTraductions(lang) {
    return fetch(`/translations/${lang}.json`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`No se pudo cargar el archivo ${lang}.json. Código de estado: ${response.status}`);
            }
            return response.json();
        })
        .catch(error => {
            console.error(`Error al cargar las traducciones para ${lang}:`, error);
            return {}; // Devolver un objeto vacío en caso de error
        });
    }
