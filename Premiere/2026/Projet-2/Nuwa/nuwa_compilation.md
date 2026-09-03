# Compilation

nüwa est un projet Rust géré par Cargo.

Installation de la chaîne d'outils, sous Linux :

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```
https://doc.rust-lang.org/book/ch01-01-installation.html

La commande suivante doit être lancée depuis la racine du projet,
c'est-à-dire le dossier qui contient `Cargo.toml` et le répertoire `src/` :

```
cargo build --release
```

Cargo récupère les dépendances (jpeg_decoder, gif, png) et compile le projet.
L'option `--release` active les optimisations du compilateur :
l'exécutable obtenu est plus rapide qu'en mode debug,
ce qui compte sur des images disque de plusieurs gigaoctets.

Le binaire e se trouve dans `target/release/nuwa`.
