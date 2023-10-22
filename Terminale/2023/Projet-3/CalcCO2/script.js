const tabs = document.querySelectorAll('[data-tab-target]')
const tabContents = document.querySelectorAll('[data-tab-content]')

tabs.forEach(tab => {
    tab.addEventListener('click',() => {
        const target = document.querySelector(tab.dataset.tabTarget) 
        tabContents.forEach(tabContent => {
            tabContent.classList.remove('active')
        } )
        // Permet que l'afichage de l'onglet precedente ne s'affiche pas sur la nouvelle onglet
        tabs.forEach(tab => {
            tab.classList.remove('active')
        } )
        tab.classList.add('active')
        target.classList.add('active')
    })
    
});  

document.getElementById('formulaire-empreinte-carbone').addEventListener('submit', function (e) {
    e.preventDefault();

    // Récupérez les valeurs des champs du formulaire

    const kmVoiture = parseFloat(document.getElementById('km-voiture').value);
    const heuresAvion = parseFloat(document.getElementById('heures-avion').value);
    const consommationElectricite = parseFloat(document.getElementById('consommation-electricite').value);
    const viandeSemaine = parseFloat(document.getElementById('viande-semaine').value);
    const courrielsEnvoyes = parseFloat(document.getElementById('courriels-envoyes').value);

    // Calcule l'empreinte carbone 

    const empreinteCarbone = ((kmVoiture * 0.18 * 365) // Calcul emission voiture
                            + (heuresAvion * 0.2) 
                            + (consommationElectricite * 0.23) 
                            + (viandeSemaine * 6.29) 
                            + (courrielsEnvoyes * 0.035))
                            /1000; // Convertion en tC02/an

    // Affichez le résultat
    document.getElementById('empreinte-carbone').textContent = empreinteCarbone.toFixed(2);

    const moyenneFrance = 9.52; //Comparaison avec la moyenne de la France de 9.52 tCO2/an
            if (empreinteCarbone > moyenneFrance) {
                document.getElementById('comparaison-moyenne').textContent = "Votre empreinte carbone est supérieure à la moyenne en France(9,52 tCO2e/habitant) :(";
            } else if (empreinteCarbone < moyenneFrance) {
                document.getElementById('comparaison-moyenne').textContent = "Votre empreinte carbone est inférieure à la moyenne en France(9,52 tCO2e/habitant) (:";
            } else {
                document.getElementById('comparaison-moyenne').textContent = "Votre empreinte carbone est égale à la moyenne en France(9,52 tCO2e/habitant).";
            }
});



