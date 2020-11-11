from pgm_reader import Reader

f = 'pgm_file.pgm'
reader = Reader()
image = reader.read_pgm(f)
width = reader.width
