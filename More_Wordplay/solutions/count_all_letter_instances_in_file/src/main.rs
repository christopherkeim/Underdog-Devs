use std::env;
use std::error::Error;
use std::fs;
use std::process;

fn main() {
    let args: Vec<String> = get_cli_arguments();

    let config: Config = Config::build(&args).unwrap_or_else(|err| {
        println!("Problem parsing arguments: {err}");
        process::exit(1);
    });

    //println!("Counting total number of: {}'s", config.vowel);
    println!("In file: {}", config.file_path);

    let data: String = load_text_from_file(&config.file_path).unwrap_or_else(|err| {
        println!("Problem loading file: {err}");
        process::exit(1);
    });

    let count: i32 = count_all_letter_instances(&config.vowel, &data);

    println!("Number of {}'s in file: {}", config.vowel, count);
}

// Collect command-line arguments from the user
fn get_cli_arguments() -> Vec<String> {
    let args: Vec<String> = env::args().collect();
    return args;
}

// CLI arguments struct
struct Config {
    vowel: char,
    file_path: String,
}

// Constructor for Config: map CLI arguments to variables
impl Config {
    fn build(args: &[String]) -> Result<Config, &'static str> {
        // Validation for input
        if args.len() > 3 {
            return Err("This function requires 2 arguments.");
        }

        let vowel: char = args[1].clone().to_uppercase().chars().nth(0).unwrap();
        let file_path: String = args[2].clone();

        Ok(Config { vowel, file_path })
    }
}

// Load data from a file into memory
fn load_text_from_file(file_path: &String) -> Result<String, Box<dyn Error>> {
    let data: String = fs::read_to_string(file_path)?;
    Ok(data)
}

// Count all instances of the character 'a' in string
fn count_all_letter_instances(letter: &char, document: &String) -> i32 {
    let mut counter: i32 = 0;
    for c in document.chars() {
        if c == *letter {
            counter += 1;
        }
    }
    return counter;
}
