# pgm

This package is for reading pgm files.

Functionality will later be added for writing pgm files.

# Usage

```
f = 'pgm_file.pgm'
reader = Reader()
image = reader.read_pgm(f)
wdith = reader.width
```