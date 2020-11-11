# PyPgm

This package is for reading portable greymap files.

Functionality still to be added for writing pgm files.

# Usage

```python
f = 'pgm_file.pgm'
reader = Reader()
image = reader.read_pgm(f)
wdith = reader.width
```