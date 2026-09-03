pub struct MagicBytes {
    //pub nom: &'static str,
    pub extention: &'static str,
    pub debut: &'static [u8],
    pub fin: &'static [u8],
    pub taille_max: usize,
}

// Una array constante de taille 2 comme type la structure (dictionaire en python)
// On a ici une array de strucs contenant tout les magicbytes
pub const MAGICS: &[MagicBytes] = &[
    MagicBytes {
        //nom: "JPEG",
        extention: "jpg",
        debut: &[0xFF, 0xD8, 0xFF],
        fin: &[0xFF, 0xD9],
        taille_max: 20 * 1024 * 1024,
    },
    MagicBytes {
        //nom: "GIF",
        extention: "gif",
        debut: b"GIF8",
        fin: &[0x3B],
        taille_max: 16 * 1024 * 1024,
    },
    MagicBytes {
        extention: "png",
        debut: &[0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A],
        fin: &[
            0x00, 0x00, 0x00, 0x00, 0x49, 0x45, 0x4E, 0x44, 0xAE, 0x42, 0x60, 0x82,
        ],
        taille_max: 20 * 1024 * 1024,
    },
];
