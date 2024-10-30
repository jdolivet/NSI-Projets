<?php
define('BASE_URL', '/');

$tipo_usuario = $_SESSION['tipo'] ?? '';
?>
<header class="bg-white text-dark py-3">
    <div class="container d-flex justify-content-between align-items-center">
        <a href="<?php echo BASE_URL; ?>index"><img src="<?php echo BASE_URL; ?>source/logo.png" alt="Logo" width="100"></a>
        <nav>
            <a href="<?php echo BASE_URL; ?>" class="btn btn-outline-primary me-2">Accueil</a>
            <!-- Liens supplémentaires pour les professeurs -->
            <?php if ($tipo_usuario == 'professor'): ?>
                <a href="<?php echo BASE_URL; ?>pages/utilisateurs" class="btn btn-outline-primary me-2">Utilisateurs</a>
                <a href="<?php echo BASE_URL; ?>pages/matieres" class="btn btn-outline-primary me-2">Matières</a>
            <?php endif; ?>
            <a href="<?php echo BASE_URL; ?>pages/notes" class="btn btn-outline-primary me-2">Notes</a>
            <a href="<?php echo BASE_URL; ?>logout" class="btn btn-outline-danger">Déconnexion</a>
        </nav>
    </div>
</header>
