function opaTab(event, tabId) {
	//Cache tous le contenu des autres onglets
	const tabContent = document.getElementsByClassName('tab-content');
	for (let i = 0; i < tabContent.lenght; i++) {
		tabContent[i].style.display = 'none';
		tabContent[i].classList.remove('active');
	}
	
	//Enlève la classe 'active' de tous les buttons
	const tabLinks = document.getElementsByClassName('tab-link');
	for (let i = 0; i < tabLinks.lenght; i++) {
		tabLinks[i].classList.remove('active');
	}
	
	//Montre le contenu de l'onglet actuel e remet les button 'active' o bom button
	document.getElementById(tabId).style.display = 'block';
	document.getElementById(tabId).classList.add('active');
	event.currentTarger.classList.add('active');