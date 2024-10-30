<?php
session_start();
require_once '../includes/db.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Vérifie si les champs sont définis
    if (isset($_POST['email'], $_POST['senha'])) {
        // Nettoie et valide l'email
        $email = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL);
        $senha = $_POST['senha'];

        // Recherche l'utilisateur dans la base de données
        $stmt = $pdo->prepare("SELECT * FROM usuarios WHERE email = ?");
        $stmt->execute([$email]);
        $user = $stmt->fetch();

        // Vérifie le mot de passe
        if ($user && password_verify($senha, $user['senha'])) {
            // Stocke les informations de l'utilisateur dans la session
            $_SESSION['user_nome'] = $user['nome'];
            $_SESSION['user_id'] = $user['id'];
            $_SESSION['tipo'] = $user['tipo'];
            header("Location: ../index");
            exit();
        } else {
            // Message d'erreur en cas de mauvais identifiants
            $loginError = "Email ou mot de passe incorrect.";
        }
    }
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
    <link href="../source/login.css" rel="stylesheet">
    <title>Connexion - PlusNote</title>
</head>
<body class="d-flex align-items-center py-4 bg-body-tertiary">
    <main class="form-signin w-100 m-auto div-logo">
        <form method="POST">
            <img class="mb-4" src="../source/logo.png" alt="" width="202">
            <h1 class="h3 mb-3 fw-normal">Veuillez vous connecter</h1>

            <?php if (isset($loginError)): ?>
                <!-- Affiche un message d'erreur si l'authentification échoue -->
                <div class="alert alert-danger"><?php echo htmlspecialchars($loginError); ?></div>
            <?php endif; ?>

            <div class="form-floating">
                <input type="email" class="form-control" id="floatingInput" name="email" placeholder="name@example.com" value="<?php echo htmlspecialchars($email ?? ''); ?>" required aria-label="Adresse e-mail">
                <label for="floatingInput">Adresse e-mail</label>
            </div>
            <div class="form-floating">
                <input type="password" class="form-control" id="floatingPassword" name="senha" placeholder="Mot de passe" required aria-label="Mot de passe">
                <label for="floatingPassword">Mot de passe</label>
            </div>

            <div class="form-check text-start my-3">
                <input class="form-check-input" type="checkbox" value="remember-me" id="flexCheckDefault">
                <label class="form-check-label" for="flexCheckDefault">
                    Se souvenir de moi
                </label>
            </div>
            <!-- Bouton pour soumettre le formulaire de connexion -->
            <button class="btn btn-primary w-100 py-2" type="submit">Se connecter</button>
            <p class="mt-5 mb-3 text-body-secondary">&copy; 2024–2024</p>
        </form>
    </main>
    <script src="../assets/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
