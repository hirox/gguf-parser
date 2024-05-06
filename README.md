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

### Example output

```bash
$ python -m gguf_parser models/Meta-Llama-3-70B-Instruct.Q3_K_L.gguf
```

```
Magic Number: b'GGUF'
Version: 3
Tensors Info:
  Name: token_embd.weight,	Shape: (8192, 128256),	Type: GGML_TYPE_Q3_K,	Offset: 0
  Name: blk.0.attn_norm.weight,	Shape: (8192,),	Type: GGML_TYPE_F32,	Offset: 451461120
  Name: blk.0.ffn_down.weight,	Shape: (28672, 8192),	Type: GGML_TYPE_Q5_K,	Offset: 451493888
  Name: blk.0.ffn_gate.weight,	Shape: (8192, 28672),	Type: GGML_TYPE_Q3_K,	Offset: 612974592
  Name: blk.0.ffn_up.weight,	Shape: (8192, 28672),	Type: GGML_TYPE_Q3_K,	Offset: 713900032
  Name: blk.0.ffn_norm.weight,	Shape: (8192,),	Type: GGML_TYPE_F32,	Offset: 814825472
  Name: blk.0.attn_k.weight,	Shape: (8192, 1024),	Type: GGML_TYPE_Q3_K,	Offset: 814858240
  Name: blk.0.attn_output.weight,	Shape: (8192, 8192),	Type: GGML_TYPE_Q5_K,	Offset: 818462720
  Name: blk.0.attn_q.weight,	Shape: (8192, 8192),	Type: GGML_TYPE_Q3_K,	Offset: 864600064
  Name: blk.0.attn_v.weight,	Shape: (8192, 1024),	Type: GGML_TYPE_Q5_K,	Offset: 893435904
  Name: blk.1.ffn_gate.weight,	Shape: (8192, 28672),	Type: GGML_TYPE_Q3_K,	Offset: 899203072
  Name: blk.1.attn_k.weight,	Shape: (8192, 1024),	Type: GGML_TYPE_Q3_K,	Offset: 1000128512
  Name: blk.1.attn_output.weight,	Shape: (8192, 8192),	Type: GGML_TYPE_Q5_K,	Offset: 1003732992
  Name: blk.1.attn_q.weight,	Shape: (8192, 8192),	Type: GGML_TYPE_Q3_K,	Offset: 1049870336
  Name: blk.1.attn_v.weight,	Shape: (8192, 1024),	Type: GGML_TYPE_Q5_K,	Offset: 1078706176
  Name: blk.1.attn_norm.weight,	Shape: (8192,),	Type: GGML_TYPE_F32,	Offset: 1084473344
  Name: blk.1.ffn_down.weight,	Shape: (28672, 8192),	Type: GGML_TYPE_Q5_K,	Offset: 1084506112
  Name: blk.1.ffn_up.weight,	Shape: (8192, 28672),	Type: GGML_TYPE_Q3_K,	Offset: 1245986816
  Name: blk.1.ffn_norm.weight,	Shape: (8192,),	Type: GGML_TYPE_F32,	Offset: 1346912256
  Name: blk.2.attn_norm.weight,	Shape: (8192,),	Type: GGML_TYPE_F32,	Offset: 1346945024
  Name: blk.2.ffn_down.weight,	Shape: (28672, 8192),	Type: GGML_TYPE_Q5_K,	Offset: 1346977792
  Name: blk.2.ffn_gate.weight,	Shape: (8192, 28672),	Type: GGML_TYPE_Q3_K,	Offset: 1508458496
  Name: blk.2.ffn_up.weight,	Shape: (8192, 28672),	Type: GGML_TYPE_Q3_K,	Offset: 1609383936
  Name: blk.2.ffn_norm.weight,	Shape: (8192,),	Type: GGML_TYPE_F32,	Offset: 1710309376
  Name: blk.2.attn_k.weight,	Shape: (8192, 1024),	Type: GGML_TYPE_Q3_K,	Offset: 1710342144
  Name: blk.2.attn_output.weight,	Shape: (8192, 8192),	Type: GGML_TYPE_Q5_K,	Offset: 1713946624
  Name: blk.2.attn_q.weight,	Shape: (8192, 8192),	Type: GGML_TYPE_Q3_K,	Offset: 1760083968
  Name: blk.2.attn_v.weight,	Shape: (8192, 1024),	Type: GGML_TYPE_Q5_K,	Offset: 1788919808
  Name: blk.3.attn_norm.weight,	Shape: (8192,),	Type: GGML_TYPE_F32,	Offset: 1794686976
  Name: blk.3.ffn_down.weight,	Shape: (28672, 8192),	Type: GGML_TYPE_Q5_K,	Offset: 1794719744
  Name: blk.3.ffn_gate.weight,	Shape: (8192, 28672),	Type: GGML_TYPE_Q3_K,	Offset: 1956200448
  Name: blk.3.ffn_up.weight,	Shape: (8192, 28672),	Type: GGML_TYPE_Q3_K,	Offset: 2057125888
  Name: blk.3.ffn_norm.weight,	Shape: (8192,),	Type: GGML_TYPE_F32,	Offset: 2158051328
  Name: blk.3.attn_k.weight,	Shape: (8192, 1024),	Type: GGML_TYPE_Q3_K,	Offset: 2158084096
  Name: blk.3.attn_output.weight,	Shape: (8192, 8192),	Type: GGML_TYPE_Q5_K,	Offset: 2161688576
  Name: blk.3.attn_q.weight,	Shape: (8192, 8192),	Type: GGML_TYPE_Q3_K,	Offset: 2207825920
  Name: blk.3.attn_v.weight,	Shape: (8192, 1024),	Type: GGML_TYPE_Q5_K,	Offset: 2236661760
  ... (truncated)
  Name: blk.78.attn_v.weight,	Shape: (8192, 1024),	Type: GGML_TYPE_Q5_K,	Offset: 35817308160
  Name: blk.79.attn_norm.weight,	Shape: (8192,),	Type: GGML_TYPE_F32,	Offset: 35823075328
  Name: blk.79.ffn_down.weight,	Shape: (28672, 8192),	Type: GGML_TYPE_Q5_K,	Offset: 35823108096
  Name: blk.79.ffn_gate.weight,	Shape: (8192, 28672),	Type: GGML_TYPE_Q3_K,	Offset: 35984588800
  Name: blk.79.ffn_up.weight,	Shape: (8192, 28672),	Type: GGML_TYPE_Q3_K,	Offset: 36085514240
  Name: blk.79.ffn_norm.weight,	Shape: (8192,),	Type: GGML_TYPE_F32,	Offset: 36186439680
  Name: blk.79.attn_k.weight,	Shape: (8192, 1024),	Type: GGML_TYPE_Q3_K,	Offset: 36186472448
  Name: blk.79.attn_output.weight,	Shape: (8192, 8192),	Type: GGML_TYPE_Q5_K,	Offset: 36190076928
  Name: blk.79.attn_q.weight,	Shape: (8192, 8192),	Type: GGML_TYPE_Q3_K,	Offset: 36236214272
  Name: blk.79.attn_v.weight,	Shape: (8192, 1024),	Type: GGML_TYPE_Q5_K,	Offset: 36265050112
  Name: output_norm.weight,	Shape: (8192,),	Type: GGML_TYPE_F32,	Offset: 36270817280
  Name: output.weight,	Shape: (8192, 128256),	Type: GGML_TYPE_Q6_K,	Offset: 36270850048
Metadata:
  general.architecture: llama
  general.name: hub
  llama.vocab_size: 128256
  llama.context_length: 8192
  llama.embedding_length: 8192
  llama.block_count: 80
  llama.feed_forward_length: 28672
  llama.rope.dimension_count: 128
  llama.attention.head_count: 64
  llama.attention.head_count_kv: 8
  llama.attention.layer_norm_rms_epsilon: 9.999999747378752e-06
  llama.rope.freq_base: 500000.0
  general.file_type: 13
  tokenizer.ggml.model: gpt2
  tokenizer.ggml.tokens: ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']... (128206 more elements)
  tokenizer.ggml.scores: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]... (128206 more elements)
  tokenizer.ggml.token_type: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]... (128206 more elements)
  tokenizer.ggml.merges: ['Ġ Ġ', 'Ġ ĠĠĠ', 'ĠĠ ĠĠ', 'ĠĠĠ Ġ', 'i n', 'Ġ t', 'Ġ ĠĠĠĠĠĠĠ', 'ĠĠ ĠĠĠĠĠĠ', 'ĠĠĠĠ ĠĠĠĠ', 'ĠĠĠ ĠĠĠĠĠ', 'ĠĠĠĠĠĠĠ Ġ', 'ĠĠĠĠĠ ĠĠĠ', 'ĠĠĠĠĠĠ ĠĠ', 'e r', 'Ġ ĠĠ', 'ĠĠ Ġ', 'o n', 'Ġ a', 'r e', 'a t', 's t', 'e n', 'o r', 'Ġ th', 'Ġt h', 'Ċ Ċ', 'Ġ c', 'l e', 'Ġ s', 'i t', 'a n', 'a r', 'a l', 'Ġ the', 'Ġt he', 'Ġth e', '; Ċ', 'Ġ p', 'Ġ f', 'o u', 'Ġ =', 'i s', 'Ġ ĠĠĠĠĠĠ', 'ĠĠ ĠĠĠĠĠ', 'ĠĠĠĠ ĠĠĠ', 'ĠĠĠ ĠĠĠĠ', 'ĠĠĠĠĠ ĠĠ', 'ĠĠĠĠĠĠ Ġ', 'i ng', 'in g']... (280097 more elements)
  tokenizer.ggml.bos_token_id: 128000
  tokenizer.ggml.eos_token_id: 128001
  tokenizer.chat_template: {% set loop_messages = messages %}{% for message in loop_messages %}{% set content = '<|start_header_id|>' + message['role'] + '<|end_header_id|>

'+ message['content'] | trim + '<|eot_id|>' %}{% if loop.index0 == 0 %}{% set content = bos_token + content %}{% endif %}{{ content }}{% endfor %}{{ '<|start_header_id|>assistant<|end_header_id|>

' }}
  general.quantization_version: 2
```

## Contributing

Contributions to gguf-parser are welcome!

## License

gguf-parser is licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for more information.
