use crate::magicbytes::MAGICS;

use std::fs::File;
use std::io::{Read, Write};
use std::path::{Path, PathBuf};

pub fn chercheur(path: PathBuf, outdir: &Path) -> std::io::Result<()> {
    let mut file = File::open(path)?;
    let mut buffer = [0_u8; 64 * 1024];

    let mut fenetre: Vec<u8> = Vec::new();
    let mut fichier: Vec<u8> = Vec::new();
    let mut magic_actuel: Option<usize> = None;

    let mut numero = 0;

    let mut plus_grand_debut = 0;
    for magic in MAGICS {
        if magic.debut.len() > plus_grand_debut {
            plus_grand_debut = magic.debut.len();
        }
    }

    loop {
        // Mise à jour du visuel.
        crate::visual::maj();

        // Si on lit 0 octet c'est qu'on est arrivé au bout.
        let octets_lus = file.read(&mut buffer)?;
        if octets_lus == 0 {
            break;
        }

        // On fait une lecture par blocs, en deux états.
        // Soit on cherche le début, soit on cherche sa fin.
        for octet in &buffer[..octets_lus] {
            if let Some(indice) = magic_actuel {
                let magic = &MAGICS[indice];
                fichier.push(*octet);

                // La signature JPEG ne fait que 3 octets, alors on tombe dessus
                // par hasard tout le temps. Mais dans un vrai JPEG le 4e octet
                // est toujours un marqueur connu, alors on le vérifie tout de suite.
                if magic.extention == "jpg"
                    && fichier.len() == 4
                    && !marqueur_jpeg_possible(fichier[3])
                {
                    fenetre.clear();
                    fenetre.extend_from_slice(&fichier[1..]);
                    fichier.clear();
                    magic_actuel = None;
                    continue;
                }

                let mut fini = false;

                let candidat = fichier.len() > magic.fin.len()
                    && fichier.ends_with(magic.fin)
                    && match magic.extention {
                        "gif" => fichier[fichier.len() - 2] == 0x00,
                        _ => true,
                    };

                if candidat {
                    // On regarde si c'est un vrai fichier avant de l'écrire.
                    let valide = match magic.extention {
                        "jpg" => jpeg_valide(&fichier),
                        "gif" => gif_valide(&fichier),
                        "png" => png_valide(&fichier),
                        _ => false,
                    };

                    if valide {
                        // Écriture du fichier.
                        let nom = format!("image_{numero}.{}", magic.extention);
                        let mut sortie = File::options()
                            .write(true)
                            .create_new(true)
                            .open(outdir.join(nom))?;
                        sortie.write_all(&fichier)?;
                        numero += 1;
                        fini = true;
                    }
                }

                // Deux raisons d'arriver ici : soit l'image est écrite, soit on renonce
                // parce que ça fait trop longtemps qu'on accumule.
                if fini || fichier.len() >= magic.taille_max {
                    fichier.clear();
                    magic_actuel = None;
                    fenetre.clear();
                }

                // On repart au prochain octet.
                continue;
            }

            fenetre.push(*octet);
            let mut encontrou = false;

            // Ici on cherche un début de magic et on change l'état de encontrou.
            for indice in 0..MAGICS.len() {
                let magic = &MAGICS[indice];
                if fenetre.ends_with(magic.debut) {
                    fichier.extend_from_slice(magic.debut);
                    magic_actuel = Some(indice);
                    fenetre.clear();
                    encontrou = true;
                    break;
                }
            }

            // Glissement de la fenêtre.
            if !encontrou && fenetre.len() >= plus_grand_debut {
                fenetre.remove(0);
            }
        }
    }

    Ok(())
}

// Étant donné que trouver quelques octets communs est très facile,
// alors le chercheur trouvait plusieurs images.
// On utilise le jpeg_decoder qui fait la vérification.
fn jpeg_valide(bytes: &[u8]) -> bool {
    let cursor = std::io::Cursor::new(bytes);
    let mut decoder = jpeg_decoder::Decoder::new(cursor);
    decoder.set_max_decoding_buffer_size(256 * 1024 * 1024);
    decoder.decode().is_ok()
}

// De même avec le gif.
fn gif_valide(bytes: &[u8]) -> bool {
    let cursor = std::io::Cursor::new(bytes);

    let decoder = match gif::Decoder::new(cursor) {
        Ok(decoder) => decoder,
        Err(_) => return false,
    };

    let mut frames = decoder.into_iter();

    match frames.next() {
        Some(Ok(_)) => {
            // premier frame existe et est valide
        }
        Some(Err(_)) => {
            return false;
        }
        None => {
            return false;
        }
    }

    for frame in frames {
        match frame {
            Ok(_) => {
                // frame valide
            }
            Err(_) => {
                return false;
            }
        }
    }

    true
}

// Ici on fait comme jpeg_valide, on utilise le décodeur pour vérifier.
fn png_valide(bytes: &[u8]) -> bool {
    let curseur = std::io::Cursor::new(bytes);
    let mut decodeur = png::Decoder::new(curseur);

    let mut limites = png::Limits::default();
    limites.bytes = 64 * 1024 * 1024;
    decodeur.set_limits(limites);

    let mut lecteur = match decodeur.read_info() {
        Ok(lect) => lect,
        Err(_) => return false,
    };

    let mut tampon = vec![0; lecteur.output_buffer_size()];
    lecteur.next_frame(&mut tampon).is_ok()
}

// On a le marqueur possible qui aide à retirer vite de faux JPEG.
fn marqueur_jpeg_possible(octet: u8) -> bool {
    matches!(octet, 0xE0..=0xEF | 0xC0..=0xC4 | 0xDB | 0xDD | 0xFE | 0xFF)
}
