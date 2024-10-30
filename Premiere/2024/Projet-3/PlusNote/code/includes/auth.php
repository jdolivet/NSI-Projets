<?php
session_start();

# Verifie si l'utilisateur est autentiquer
function is_logged_in() {
    return isset($_SESSION['user_id']);
}

# Renvoie l'utilisateur a la page de login, si il n'est pas autentiquer.
function redirect_if_not_logged_in() {
    if (!is_logged_in()) {
        header("Location: /pages/login");
        exit;
    }
}

# Renvoie l'utilisateur a la page de login, si il n'est pas professeur.
function redirect_si_pas_professeur() {
    if ($_SESSION['tipo'] != "professor") {
        header("Location: /");
        exit;
    }
}
?>
