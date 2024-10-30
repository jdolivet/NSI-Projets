<?php
require_once 'includes/auth.php';
redirect_if_not_logged_in();

$user_type = $_SESSION['tipo'] ?? '';
?>

<!doctype html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" type="image/x-icon" href="/source/favicon.png">
    <link href="assets/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="source/login.css" rel="stylesheet">
    <title>Visualisation des Notes</title>
    <link rel="stylesheet" href="source/default.css">
</head>
<body class="bg-light">
    <?php require_once 'template/header.php'; ?>
    <div class="container mt-5">
        <!-- Affichage du message de bienvenue avec le nom de l'utilisateur connecté -->
        <h2 class="mb-4">Bienvenue, <?php echo $_SESSION['user_nome']; ?> !</h2>
        <h3 class="mb-4">Visualisation des Notes</h3>

        <!-- Formulaire de filtrage par matière et, pour les professeurs, par élève -->
        <form method="GET" class="mb-4">
            <div class="row">
                <div class="col-md-4">
                    <label for="materia" class="form-label">Sélectionnez la Matière</label>
                    <select id="materia" name="materia_id" class="form-select">
                        <option value="">Toutes les Matières</option>
                        <?php
                        require_once 'includes/db.php';
                        $stmtMaterias = $pdo->prepare("SELECT id, nome FROM materias");
                        $stmtMaterias->execute();
                        while ($materia = $stmtMaterias->fetch()) {
                            $selected = (isset($_GET['materia_id']) && $_GET['materia_id'] == $materia['id']) ? 'selected' : '';
                            echo "<option value='" . htmlspecialchars($materia['id']) . "' " . $selected . ">" . htmlspecialchars($materia['nome']) . "</option>";
                        }
                        ?>
                    </select>
                </div>

                <!-- Filtre supplémentaire pour les professeurs : choix de l'élève -->
                <?php if ($user_type == 'professor'): ?>
                <div class="col-md-4">
                    <label for="aluno" class="form-label">Sélectionnez l'Élève</label>
                    <select id="aluno" name="aluno_id" class="form-select">
                        <option value="">Tous les Élèves</option>
                        <?php
                        $stmtAlunos = $pdo->prepare("SELECT id, nome FROM usuarios WHERE tipo = 'aluno'");
                        $stmtAlunos->execute();
                        while ($aluno = $stmtAlunos->fetch()) {
                            $selected = (isset($_GET['aluno_id']) && $_GET['aluno_id'] == $aluno['id']) ? 'selected' : '';
                            echo "<option value='" . htmlspecialchars($aluno['id']) . "' " . $selected . ">" . htmlspecialchars($aluno['nome']) . "</option>";
                        }
                        ?>
                    </select>
                </div>
                <?php endif; ?>

                <div class="col-md-2 align-self-end">
                    <button type="submit" class="btn btn-primary">Filtrer</button>
                </div>
            </div>
        </form>

        <!-- Tableau pour afficher les résultats filtrés des notes -->
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>Élève</th>
                    <th>Matière</th>
                    <th>Note</th>
                </tr>
            </thead>
            <tbody>
                <?php
                // Construction de la requête SQL pour obtenir les notes
                $query = "SELECT usuarios.id, usuarios.nome, usuarios.sobrenome, materias.nome AS materia, AVG(notas.nota) AS media ";
                $query .= "FROM usuarios ";
                $query .= "LEFT JOIN notas ON usuarios.id = notas.usuario_id ";
                $query .= "LEFT JOIN materias ON notas.materia_id = materias.id ";
                $query .= "WHERE usuarios.tipo = 'aluno' ";

                // Si l'utilisateur est un professeur, il peut filtrer par élève
                if ($user_type == 'professor' && isset($_GET['aluno_id']) && $_GET['aluno_id'] != '') {
                    $query .= "AND usuarios.id = :aluno_id ";
                } elseif ($user_type != 'professor') {
                    // Les élèves peuvent seulement voir leurs propres notes
                    $query .= "AND usuarios.id = :user_id ";
                }

                // Ajout de la condition de filtre par matière, si applicable
                if (isset($_GET['materia_id']) && $_GET['materia_id'] != '') {
                    $query .= "AND materias.id = :materia_id ";
                }

                // Groupement des résultats par élève et matière
                $query .= "GROUP BY usuarios.id, materias.id";
                $stmt = $pdo->prepare($query);

                // Liaison des paramètres (élève et matière)
                if ($user_type == 'professor' && isset($_GET['aluno_id']) && $_GET['aluno_id'] != '') {
                    $stmt->bindParam(':aluno_id', $_GET['aluno_id'], PDO::PARAM_INT);
                } elseif ($user_type != 'professor') {
                    $stmt->bindParam(':user_id', $_SESSION['user_id'], PDO::PARAM_INT);
                }

                if (isset($_GET['materia_id']) && $_GET['materia_id'] != '') {
                    $stmt->bindParam(':materia_id', $_GET['materia_id'], PDO::PARAM_INT);
                }

                // Exécution de la requête SQL
                $stmt->execute();
                $alunos = $stmt->fetchAll(PDO::FETCH_ASSOC);

                // Affichage des résultats dans le tableau
                foreach ($alunos as $aluno):
                ?>
                    <tr>
                        <td><?php echo htmlspecialchars($aluno['nome']). " ".htmlspecialchars($aluno['sobrenome']); ?></td>
                        <td><?php echo htmlspecialchars($aluno['materia'] ?? '-'); ?></td>
                        <td><?php echo htmlspecialchars($aluno['media'] !== null ? number_format($aluno['media'], 2) : '-'); ?></td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    </div>

    <script src="/assets/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>