<?php
require_once '../includes/db.php';
require_once '../includes/auth.php';
redirect_if_not_logged_in();

// Vérifie si l'utilisateur est un professeur ou un élève
$tipo_usuario = $_SESSION['tipo'];
$usuario_id = $_SESSION['user_id'];

if ($_SERVER['REQUEST_METHOD'] == 'POST' && $tipo_usuario == 'professor') {
    // Récupère les données du formulaire pour créer une nouvelle note
    $aluno_id = $_POST['aluno_id'];
    $materia_id = $_POST['materia_id'];
    $nota = number_format($_POST['nota'], 2, '.', '');

    // Insère la nouvelle note dans la base de données
    $stmt = $pdo->prepare("INSERT INTO notas (usuario_id, materia_id, nota) VALUES (?, ?, ?)");
    $stmt->execute([$aluno_id, $materia_id, $nota]);

    // Redirige vers la page de gestion des notes
    header("Location: notes");
    exit();
}

if (isset($_GET['delete']) && $tipo_usuario == 'professor') {
    // Supprime une note spécifique
    $id = $_GET['delete'];
    $stmt = $pdo->prepare("DELETE FROM notas WHERE id = ?");
    $stmt->execute([$id]);
    header("Location: notes");
    exit();
}

// Définit les critères de tri
$sort_column = $_GET['sort'] ?? 'aluno';
$sort_order = $_GET['order'] ?? 'asc';
$allowed_columns = ['aluno', 'materia', 'nota', 'data_lancamento'];

if (!in_array($sort_column, $allowed_columns)) {
    $sort_column = 'aluno';
}

if (!in_array($sort_order, ['asc', 'desc'])) {
    $sort_order = 'asc';
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
    <title>Gestion des Notes - PlusNote</title>
    <link rel="stylesheet" href="../source/default.css">
</head>
<body class="bg-light">
    <?php require_once '../template/header.php'; ?>
    <div class="container mt-5">
        <!-- Formulaire de saisie des notes, réservé aux professeurs -->
        <?php if ($tipo_usuario == 'professor'): ?>
            <h2 class="mb-4">Gestion des Notes</h2>
            <form method="POST" class="mb-4">
                <div class="mb-3">
                    <label for="aluno_id" class="form-label">Élève</label>
                    <select id="aluno_id" name="aluno_id" class="form-select" required>
                        <option value="">Sélectionnez un élève</option>
                        <?php
                        $stmtAlunos = $pdo->query("SELECT id, nome, sobrenome FROM usuarios WHERE tipo = 'aluno'");
                        while ($aluno = $stmtAlunos->fetch()) {
                            echo "<option value='" . htmlspecialchars($aluno['id']) . "'>" . htmlspecialchars($aluno['nome']) ." ".htmlspecialchars($aluno['sobrenome'])."</option>";
                        }
                        ?>
                    </select>
                </div>
                <div class="mb-3">
                    <label for="materia_id" class="form-label">Matière</label>
                    <select id="materia_id" name="materia_id" class="form-select" required>
                        <option value="">Sélectionnez une matière</option>
                        <?php
                        $stmtMaterias = $pdo->query("SELECT id, nome FROM materias");
                        while ($materia = $stmtMaterias->fetch()) {
                            echo "<option value='" . htmlspecialchars($materia['id']) . "'>" . htmlspecialchars($materia['nome']) . "</option>";
                        }
                        ?>
                    </select>
                </div>
                <div class="mb-3">
                    <label for="nota" class="form-label">Note</label>
                    <input type="number" step="0.01" class="form-control" id="nota" name="nota" placeholder="Note" required>
                </div>
                <button type="submit" class="btn btn-primary">Enregistrer la Note</button>
            </form>
        <?php endif; ?>

        <h2 class="mb-4">Liste des Notes</h2>
        <!-- Formulaire de filtrage des notes -->
        <form method="GET" class="mb-4">
            <div class="row">
                <div class="col-md-4">
                    <label for="materia_filtro" class="form-label">Filtrer par Matière</label>
                    <select id="materia_filtro" name="materia_id" class="form-select">
                        <option value="">Toutes les Matières</option>
                        <?php
                        $stmtMateriasFiltro = $pdo->query("SELECT id, nome FROM materias");
                        while ($materia = $stmtMateriasFiltro->fetch()) {
                            $selected = (isset($_GET['materia_id']) && $_GET['materia_id'] == $materia['id']) ? 'selected' : '';
                            echo "<option value='" . htmlspecialchars($materia['id']) . "' " . $selected . ">" . htmlspecialchars($materia['nome']) . "</option>";
                        }
                        ?>
                    </select>
                </div>
                <?php if ($tipo_usuario == 'professor'): ?>
                <div class="col-md-4">
                    <label for="aluno_filtro" class="form-label">Filtrer par Élève</label>
                    <select id="aluno_filtro" name="aluno_id" class="form-select">
                        <option value="">Tous les Élèves</option>
                        <?php
                        $stmtAlunosFiltro = $pdo->query("SELECT id, nome, sobrenome FROM usuarios WHERE tipo = 'aluno'");
                        while ($aluno = $stmtAlunosFiltro->fetch()) {
                            $selected = (isset($_GET['aluno_id']) && $_GET['aluno_id'] == $aluno['id']) ? 'selected' : '';
                            echo "<option value='" . htmlspecialchars($aluno['id']) . "' " . $selected . ">" . htmlspecialchars($aluno['nome']) ." ". htmlspecialchars($aluno['sobrenome'])."</option>";
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
                    <th><a href="?sort=aluno&order=<?php echo ($sort_column == 'aluno' && $sort_order == 'asc') ? 'desc' : 'asc'; ?>" class="sortable">Élève</a></th>
                    <th><a href="?sort=materia&order=<?php echo ($sort_column == 'materia' && $sort_order == 'asc') ? 'desc' : 'asc'; ?>" class="sortable">Matière</a></th>
                    <th><a href="?sort=nota&order=<?php echo ($sort_column == 'nota' && $sort_order == 'asc') ? 'desc' : 'asc'; ?>" class="sortable">Note</a></th>
                    <th><a href="?sort=data_lancamento&order=<?php echo ($sort_column == 'data_lancamento' && $sort_order == 'asc') ? 'desc' : 'asc'; ?>" class="sortable">Date de Publication</a></th>
                    <?php if ($tipo_usuario == 'professor'): ?>
                    <th>Actions</th>
                    <?php endif; ?>
                </tr>
            </thead>
            <tbody>
                <?php
                // Construction de la requête pour récupérer les notes
                $query = "SELECT notas.id, usuarios.nome AS aluno, usuarios.sobrenome AS sobrenome_aluno, materias.nome AS materia, notas.nota, notas.data_lancamento FROM notas ";
                $query .= "JOIN usuarios ON notas.usuario_id = usuarios.id ";
                $query .= "JOIN materias ON notas.materia_id = materias.id ";
                $conditions = [];
                $params = [];

                // Filtrage par matière si sélectionné
                if (isset($_GET['materia_id']) && $_GET['materia_id'] != '') {
                    $conditions[] = "materias.id = :materia_id";
                    $params[':materia_id'] = $_GET['materia_id'];
                }

                // Si l'utilisateur est un élève, il ne peut voir que ses propres notes
                if ($tipo_usuario == 'aluno') {
                    $conditions[] = "usuarios.id = :usuario_id";
                    $params[':usuario_id'] = $usuario_id;
                } elseif (isset($_GET['aluno_id']) && $_GET['aluno_id'] != '') {
                    $conditions[] = "usuarios.id = :aluno_id";
                    $params[':aluno_id'] = $_GET['aluno_id'];
                }

                if ($conditions) {
                    $query .= "WHERE " . implode(" AND ", $conditions);
                }

                // Tri des résultats
                $query .= " ORDER BY " . $sort_column . " " . $sort_order;

                $stmtNotas = $pdo->prepare($query);
                $stmtNotas->execute($params);

                // Affichage des notes dans le tableau
                while ($nota = $stmtNotas->fetch()) {
                    echo "<tr>
                            <td>" . htmlspecialchars($nota['aluno']) ." ". htmlspecialchars($nota['sobrenome_aluno'])."</td>
                            <td>" . htmlspecialchars($nota['materia']) . "</td>
                            <td>" . htmlspecialchars(number_format($nota['nota'], 2)) . "</td>
                            <td>" . htmlspecialchars(date('d/m/Y', strtotime($nota['data_lancamento']))) . "</td>";
                    if ($tipo_usuario == 'professor') {
                        echo "<td>
                                <a href='notes?delete=" . $nota['id'] . "' class='btn btn-danger btn-sm' onclick=\"return confirm('Êtes-vous sûr de vouloir supprimer cette note ?');\">Supprimer</a>
                              </td>";
                    }
                    echo "</tr>";
                }
                ?>
            </tbody>
        </table>
    </div>
    <script src="../assets/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>