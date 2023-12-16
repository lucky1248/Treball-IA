import Data from './Data';
let dataInstance;

document.addEventListener('DOMContentLoaded', function() {
    // Inicializa el idioma predeterminado al cargar la página y el dataInstance
    dataInstance = new Data();
    const defaultLanguage = 'ca';
    changeLanguage(defaultLanguage);
});

async function changeLanguage(lang){
    try {
        // Carga las traducciones
        const traductions = await cargarTraductions(lang);

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

function submitSexForm() {
    dataInstance.changeSexValue(document.getElementById('sex').value);
}

function submitEducationForm() {
    dataInstance.changeEducationValue(document.getElementById('education').value);
}

function submitAgeForm() {
    dataInstance.changeAgeValue(document.getElementById('age').value);
}

function submitDistrictForm() {
    dataInstance.changeDistrictValue(document.getElementById('district').value);
    /*var selectedDistrict = document.getElementById("district").value;

    // Obtener el div del segundo desplegable
    var barrioDiv = document.getElementById("barrioDiv");

    // Limpiar el desplegable de barrios
    document.getElementById("neighborhood").innerHTML = "";

    // Mostrar el div del segundo desplegable si se ha seleccionado un distrito válido
    if (selectedDistrict !== "0") {
        barrioDiv.style.display = "block";

        // Llenar el desplegable de barrios según el distrito seleccionado
        fillNeighborhoodOptions(selectedDistrict);
    } else {
        // Ocultar el div del segundo desplegable si no se ha seleccionado un distrito válido
        barrioDiv.style.display = "none";
    }
}

function fillNeighborhoodOptions(district) {
    // Aquí debes agregar lógica para llenar las opciones de barrios según el distrito
    // Puedes usar un switch o if-else para manejar cada distrito

    var neighborhoodSelect = document.getElementById("neighborhood");

    // Ejemplo: llenar opciones para Ciutat Vella
    if (district === "1") {
        var neighborhoods = ["Barrio1", "Barrio2", "Barrio3"];
        neighborhoods.forEach(function (neighborhood, index) {
            var option = document.createElement("option");
            option.value = index + 1;
            option.text = neighborhood;
            neighborhoodSelect.add(option);
        });
    }
    // Agrega lógica similar para los demás distritos*/
}

function submitNeighborhoodForm(){
    dataInstance.changeNeighborhoodValue(document.getElementById('neighborhood').value);
}