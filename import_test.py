
import pgm_reader

f = 'pgm_file.pgm'
reader = pgm_reader.Reader()
image = reader.read_pgm(f)
reader.show_img()
