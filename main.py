#!/usr/bin/env python3
"""
Project: CLI Language Analyzer
Author: Mathias Tichota
License: GPLv3
Description: A simple command-line tool to analyze text files.
             It calculates total word count and unique vocabulary size.
             Designed to support UTF-8 for Czech, German, and other languages with spaces.
"""

import argparse
import sys
import string

def read_file(filepath: str) -> str:
    """
    Reads the content of a text file safely.
    
    Args:
        filepath (str): The path to the file.
        
    Returns:
        str: The raw content of the file.
    """
    try:
        # We use 'utf-8' encoding to ensure characters like 'ř', 'ö', or '猫' 
        # are read correctly without crashing.
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.", file=sys.stderr)
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Error: '{filepath}' is not a valid text file (it might be binary).", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

def get_words(text: str) -> list[str]:
    """
    Normalizes text and splits it into a list of words.
    
    1. Converts to lowercase (so "The" and "the" are counted as the same word).
    2. Removes punctuation (so "cat." becomes "cat").
    3. Splits by whitespace.
    """
    # 1. Normalize case
    text_lower = text.lower()
    
    # 2. Remove punctuation
    # str.maketrans creates a mapping table that tells translate() to replace 
    # every punctuation character with None (deleting them).
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text_lower.translate(translator)
    
    # 3. Split into a list
    return clean_text.split()

def main() -> None:
    # ---------------------------------------------------------
    # 1. Argument Parsing
    # ---------------------------------------------------------
    parser = argparse.ArgumentParser(
        description="A CLI language analyzer written in Python."
    )

    # Positional argument: The file to analyze
    parser.add_argument(
        "file",
        help="The path to the text file to analyze"
    )

    # Optional Flag: -c / --count
    parser.add_argument(
        "-c", "--count",
        action="store_true",
        help="Show total word count (tokens)."
    )

    # Optional Flag: -u / --unique
    parser.add_argument(
        "-u", "--unique",
        action="store_true",
        help="Show number of unique words (types)."
    )

    args = parser.parse_args()

    # If no flags are provided, print usage and exit (optional UX choice)
    if not args.count and not args.unique:
        print("Please specify at least one action: -c (count) or -u (unique).")
        parser.print_help()
        sys.exit(0)

    # ---------------------------------------------------------
    # 2. Data Processing
    # ---------------------------------------------------------
    content = read_file(args.file)
    words = get_words(content)

    # ---------------------------------------------------------
    # 3. Output Logic
    # ---------------------------------------------------------
    
    # Handle Total Count (-c)
    if args.count:
        total_words = len(words)
        print(f"Total Words: {total_words}")

    # Handle Unique Count (-u)
    if args.unique:
        # converting a list to a 'set' automatically removes duplicates
        unique_words = len(set(words))
        print(f"Unique Words: {unique_words}")

if __name__ == "__main__":
    main()
