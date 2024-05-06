"""
GGUF Parser Main

This module provides the main entry point for the GGUF parser when used as a
standalone script. It takes a GGUF file as an argument and prints the parsed
information.

Usage:
    python -m gguf_parser /path/to/file.gguf
"""

import argparse
from .gguf_parser import GGUFParser, GGUFParseError


def main():
    """Main function for the GGUF parser script."""
    parser = argparse.ArgumentParser(description="Parse a GGUF file.")
    parser.add_argument("file_path", help="The path to the GGUF file.")
    args = parser.parse_args()

    gguf_parser = GGUFParser(args.file_path)
    try:
        gguf_parser.parse()
    except GGUFParseError as e:
        print(f"Error: {e}")
    else:
        gguf_parser.print()


if __name__ == "__main__":
    main()
