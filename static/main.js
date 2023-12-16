//const Data = require('./Data');
//const dataInstance = new Data();

document.addEventListener('DOMContentLoaded', function() {
    // Inicializa el idioma predeterminado al cargar la página y el dataInstance
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
    //dataInstance.changeSexValue(document.getElementById('sex').value);
}

function submitEducationForm() {
    //dataInstance.changeEducationValue(document.getElementById('education').value);
}

function submitAgeForm() {
    //dataInstance.changeAgeValue(document.getElementById('age').value);
}

function submitDistrictForm() {
    //dataInstance.changeDistrictValue(document.getElementById('district').value);
    var selectedDistrict = document.getElementById("district").value;
    var neighborhoodDiv = document.getElementById("subcategoryNeighborhoodContainer");
    var neighborhoodSelect = document.getElementById("neighborhood");
    neighborhoodSelect.innerHTML = "";
    if (selectedDistrict != "0") {
        neighborhoodDiv.style.display = "block";
        fillNeighborhoodOptions(selectedDistrict, neighborhoodSelect);    
    }
    else{
        neighborhoodDiv.style.display = "none";}
}

function fillNeighborhoodOptions(district, neighborhoodSelect){
    neighborhoods = [];
    if (district == 1) {
        var neighborhoods = ["","Barrio1", "Barrio2", "Barrio3"];}
    else if (district == 2) {
        var neighborhoods = ["Barrio1", "Barrio2", "Barrio3"];}
    else if (district == 3) {
        var neighborhoods = ["Barrio1", "Barrio2", "Barrio3"];}
    else if (district == 4) {
        var neighborhoods = ["Barrio1", "Barrio2", "Barrio3"];}
    else if (district == 5) {
        var neighborhoods = ["Barrio1", "Barrio2", "DSS"];}
    else if (district == 6) {
        var neighborhoods = ["Barrio1", "Barrio2", "Barrio3"];}
    else if (district == 7) {
        var neighborhoods = ["Barrio1", "Barrio2", "Barrio3"];}
    else if (district == 7) {
        var neighborhoods = ["Barrio1", "Barrio2", "Barrio3"];}
    else if (district == 9) {
        var neighborhoods = ["Barrio1", "Barrio2", "Barrio3"];}
    else if (district == 10) {
        var neighborhoods = ["Barrio1", "Barrio2", "BB"];}  
    else{
        console.error(`Error al cargar los barrios`);} 
    neighborhoods.forEach(function (neighborhood, index) {
        var option = document.createElement("option");
        option.value = index;
        option.text = neighborhood;
        neighborhoodSelect.add(option);
    })
}

function submitNeighborhoodForm(){
    //dataInstance.changeNeighborhoodValue(document.getElementById('neighborhood').value);
}