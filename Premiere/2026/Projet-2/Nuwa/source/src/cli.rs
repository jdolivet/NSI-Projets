use clap::Parser;
use std::path::PathBuf;

#[derive(Parser)]
#[command(
    name = "nuwa",
    version,
    about = "Récupère des fichiers à partir de leurs signatures binaires (magicbytes).",
    long_about = "Nüwa analyse un fichier ou une image de disque.
    Elle recherche des signatures connus, puis enregistre les fichiers
récupérés dans un dossier séparé.",
    arg_required_else_help = true,
    next_line_help = true,
    after_help = "\
    EXEMPLES :
        ./nuwa --chemin usb.img
        ./nuwa --chemin usb.img --sortie images_recuperes
        sudo ./nuwa -c /dev/sdb -s images
"
)]
pub struct CliArgs {
    /// Chemin pour le path de la recuperation
    #[arg(short = 'c', long = "chemin", help_heading = "ENTRÉE")]
    pub path: PathBuf,

    /// Chemin pour la recuperation standard
    #[arg(
        short = 's',
        long = "sortie",
        default_value = "img_recuperees/",
        help_heading = "SORTIE"
    )]
    pub outdirstd: PathBuf,
}
