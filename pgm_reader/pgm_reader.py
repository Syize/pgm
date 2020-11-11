import numpy as np 
from matplotlib import pyplot as plt


class Reader:
    def __init__(self):
        self.data = None
        self.codec = None
        self.width = None
        self.height = None

    def read_pgm(self, pgm_file_name):
        with open(pgm_file_name, 'rb') as f:
            codec = f.readline()

        print(f"Codec: {codec}")
        if codec == b"P2\n":
            return self._read_p2(pgm_file_name)
        elif codec == b'P5\n':
            return self._read_p5(pgm_file_name)
        else:
            raise Exception(f"Incorrect format of PGM: {codec}")

    def _read_p2(self, pgm_name):
        print(f"Reading P2 maps")
        with open(pgm_name, 'r') as f:
            lines = f.readlines()

        for l in list(lines):
            if l[0] == '#':
                lines.remove(l)
        # here,it makes sure it is ASCII format (P2)
        codec = lines[0].strip()

        # Converts data to a list of integers
        data = []
        for line in lines[1:]:
            data.extend([int(c) for c in line.split()])

        data = (np.array(data[3:]),(data[1],data[0]),data[2])

        self.width = data[1][1]
        self.height = data[1][0]

        data = np.reshape(data[0],data[1])
        self.data = data

        return data
    
    def _read_p5(self, pgm_name):
        print(f"Reading P5 maps")
        with open(pgm_name, 'rb') as pgmf:
            assert pgmf.readline() == b'P5\n'

            t = pgmf.readline()
            while t[0] == '#':
                t = pgmf.readline()
                
            wh_line = pgmf.readline().split()
            (width, height) = [int(i) for i in wh_line]
            depth = int(pgmf.readline())
            assert depth <= 255

            raster = []
            for y in range(height):
                row = []
                for y in range(width):
                    row.append(ord(pgmf.read(1)))
                raster.append(row)

        data = np.array(raster)
            
        self.height = height
        self.width = width
        self.data = data 

        return data 
        
    def show_img(self):
        plt.imshow(self.data)
        plt.show()



def test():
    f = 'pypgm/race_track.pgm'
    reader = Reader()
    image = reader.read_pgm(f)

    plt.imshow(image)
    plt.show()


if __name__ == "__main__":
    test()

