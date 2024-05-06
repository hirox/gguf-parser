# GGUF Parser

`gguf-parser` is a Python package for parsing GGUF files. It provides a `GGUFParser` class that can be used to read and parse GGUF files, and extract useful information such as version, tensor information, and metadata.

## Installation

To install `gguf-parser`, you can clone this repository and install it using `pip`:

```bash
git clone https://github.com/hirox/gguf-parser.git
cd gguf-parser
pip install .
```

## Usage

You can use `gguf-parser` as a library in your Python code:

```python
from gguf_parser import GGUFParser

parser = GGUFParser("/path/to/file.gguf")
parser.parse()
parser.print()
```

You can also use it as a standalone script:

```bash
python -m gguf_parser /path/to/file.gguf
```

This will print the parsed information to the console.

## Contributing

Contributions to gguf-parser are welcome!

## License

gguf-parser is licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for more information.
