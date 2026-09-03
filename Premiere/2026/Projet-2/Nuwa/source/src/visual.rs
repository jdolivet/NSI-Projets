use std::time::{SystemTime, UNIX_EPOCH};

const CADRES: [&str; 8] = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧"];

pub fn maj() {
    let ms = SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_millis();

    let symbole = CADRES[(ms / 80) as usize % CADRES.len()];

    print!("\x1B[H\x1B[J\nnüwa — récupération en cours [{symbole}]\n");
}
