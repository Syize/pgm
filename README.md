# PyPgm

This package is for reading portable greymap files.

Functionality still to be added for writing pgm files.

# Installation

```cmd
pip install pgm_reader
```

# Usage

```python
from pgm_reader import Reader

f = 'pgm_file.pgm'
reader = Reader()
image = reader.read_pgm(f)
width = reader.width
```