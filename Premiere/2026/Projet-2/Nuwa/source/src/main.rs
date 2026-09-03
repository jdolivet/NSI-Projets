mod chercheur;
mod cli;
mod magicbytes;
mod visual;

use clap::Parser; // (en python:: import clap.Parser)
use cli::CliArgs; // meme chose

use std::fs;
use std::io;

fn main() -> io::Result<()> {
    let args = CliArgs::parse();

    fs::create_dir_all(&args.outdirstd)?;

    chercheur::chercheur(args.path, &args.outdirstd)?;

    Ok(())
}
