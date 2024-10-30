<?php
require_once '../includes/db.php';
require_once '../includes/auth.php';
redirect_if_not_logged_in();
redirect_si_pas_professeur();

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Récupère le nom de la matière depuis le formulaire
    $nome = $_POST['nome'];

    // Insère la nouvelle matière dans la base de données
    $stmt = $pdo->prepare("INSERT INTO materias (nome) VALUES (?)");
    $stmt->execute([$nome]);

    // Redirection vers la page de gestion des matières après l'enregistrement
    header("Location: matieres");
    exit();
}

if (isset($_GET['delete'])) {
    // Supprime une matière spécifique de la base de données
    $id = $_GET['delete'];
    $stmt = $pdo->prepare("DELETE FROM materias WHERE id = ?");
    $stmt->execute([$id]);
    header("Location: matieres");
    exit();
}
?>

<!doctype html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/x-icon" href="../source/favicon.png">
    <link href="../assets/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>Gestion des Matières - PlusNote</title>
    <link rel="stylesheet" href="../source/default.css">
</head>
<body class="bg-light">
    <?php require_once '../template/header.php'; ?>
    <div class="container mt-5">
        <h2 class="mb-4">Gestion une Matière</h2>
        <form method="POST" class="mb-4">
            <div class="mb-3">
                <label for="nome" class="form-label">Nom de la Matière</label>
                <input type="text" class="form-control" id="nome" name="nome" placeholder="Nom de la Matière" required>
            </div>
            <!-- Bouton pour soumettre le formulaire d'enregistrement -->
            <button type="submit" class="btn btn-primary">Enregistrer la Matière</button>
        </form>

        <h2 class="mb-4">Liste des Matières</h2>
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>Nom</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <?php
                // Récupère la liste des matières depuis la base de données
                $stmt = $pdo->query("SELECT * FROM materias");
                while ($materia = $stmt->fetch()) {
                    echo "<tr>
                            <td>" . htmlspecialchars($materia['nome']) . "</td>
                            <td>
                                <a href='matieres?delete=" . $materia['id'] . "' class='btn btn-danger btn-sm' onclick=\"return confirm('Êtes-vous sûr de vouloir supprimer cette matière ?');\">Supprimer</a>
                            </td>
                          </tr>";
                }
                ?>
            </tbody>
        </table>
    </div>
    <script src="../assets/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
