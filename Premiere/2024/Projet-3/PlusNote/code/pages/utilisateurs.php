<?php
require_once '../includes/db.php';
require_once '../includes/auth.php';
redirect_if_not_logged_in();

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Récupère les données du formulaire
    $nome = $_POST['nome'];
    $sobrenome = $_POST['sobrenome'];
    $email = $_POST['email'];
    $tipo = $_POST['tipo'];
    // Génère un code de mot de passe temporaire
    $codigo_senha = bin2hex(random_bytes(6));
    // Hash du mot de passe pour plus de sécurité
    $senha = password_hash($codigo_senha, PASSWORD_DEFAULT);

    // Insère le nouvel utilisateur dans la base de données
    $stmt = $pdo->prepare("INSERT INTO usuarios (nome, sobrenome, email, tipo, senha) VALUES (?, ?, ?, ?, ?)");
    $stmt->execute([$nome, $sobrenome, $email, $tipo, $senha]);

    require '../source/vendor/autoload.php';

    $mail = new PHPMailer(true);

    try {
        // Paramètres du serveur SMTP
        $mail->isSMTP();
        $mail->Host       = ''; // Adresse du serveur SMTP
        $mail->SMTPAuth   = true;                   
        $mail->Username   = ''; // email SMTP
        $mail->Password   = '';             // mot de passe SMTP
        $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS; // Utilisation du chiffrement TLS ou SSL
        $mail->Port       = 587;                    // Port SMTP

        // Définit l'expéditeur et les destinataires
        $mail->setFrom('', '');
        $mail->addAddress("$email", "$nome $sobrenome");

        // Contenu de l'email
        $mail->isHTML(true);                                  // Définit que l'email sera en format HTML
        $mail->Subject = 'Votre mot de passe pour le PlusNote';
        $mail->Body    = "Login: <b>$email</b><br>
                            Mot de passe: <b>$codigo_senha</b>";

        // Envoie l'email
        $mail->send();
        echo 'Utilisateur enregistré avec succès !';
    } catch (Exception $e) {
        // Affiche une erreur si l'envoi d'email échoue
        echo "Erreur lors de l'enregistrement de l'utilisateur: {$mail->ErrorInfo}";
    }
    // Redirection vers la liste des utilisateurs après l'enregistrement
    header("Location: utilisateurs");
    exit();
}

if (isset($_GET['delete'])) {
    // Supprime un utilisateur sauf celui avec l'ID 9 (par mesure de sécurité)
    $user_id = $_SESSION['user_id'];

    $id = $_GET['delete'];
    $stmt = $pdo->prepare("DELETE FROM usuarios WHERE id = ? AND id != 1 AND id != $user_id");
    $stmt->execute([$id]);
    header("Location: utilisateurs");
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
    <title>Gestion des Utilisateurs - PlusNote</title>
    <link rel="stylesheet" href="../source/default.css">
</head>
<body class="bg-light">
    <?php require_once '../template/header.php'; ?>
    <div class="container mt-5">
        <h2 class="mb-4">Gestion des Utilisateurs</h2>
        <form method="POST" class="mb-4">
            <div class="mb-3">
                <label for="nome" class="form-label">Prénom</label>
                <input type="text" class="form-control" id="nome" name="nome" placeholder="Prénom" required>
            </div>
            <div class="mb-3">
                <label for="sobrenome" class="form-label">Nom de famille</label>
                <input type="text" class="form-control" id="sobrenome" name="sobrenome" placeholder="Nom de famille" required>
            </div>
            <div class="mb-3">
                <label for="tipo" class="form-label">Type</label>
                <select id="tipo" name="tipo" class="form-select" required>
                    <option value="">Sélectionnez un type</option>
                    <option value="professor">Professeur</option>
                    <option value="aluno">Élève</option>
                </select>
            </div>
            <div class="mb-3">
                <label for="email" class="form-label">Email</label>
                <input type="email" class="form-control" id="email" name="email" placeholder="Email" required>
            </div>
            <!-- Bouton pour soumettre le formulaire d'enregistrement -->
            <button type="submit" class="btn btn-primary">Enregistrer l'utilisateur</button>
        </form>

        <h2 class="mb-4">Liste des Utilisateurs</h2>
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>Prénom</th>
                    <th>Nom de famille</th>
                    <th>Email</th>
                    <th>Type</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <?php
                // Récupère la liste des utilisateurs dans la base de données
                $stmt = $pdo->query("SELECT * FROM usuarios");
                while ($aluno = $stmt->fetch()) {
                    echo "<tr>
                            <td>" . htmlspecialchars($aluno['nome']) . "</td>
                            <td>" . htmlspecialchars($aluno['sobrenome']) . "</td>
                            <td>" . htmlspecialchars($aluno['email']) . "</td>
                            <td>" . htmlspecialchars($aluno['tipo']) . "</td>
                            <td>
                                <a href='utilisateurs?delete=" . $aluno['id'] . "' class='btn btn-danger btn-sm' onclick=\"return confirm('Êtes-vous sûr de vouloir supprimer cet utilisateur ?');\">Supprimer</a>
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
