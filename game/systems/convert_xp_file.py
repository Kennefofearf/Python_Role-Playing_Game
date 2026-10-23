import gzip
import struct


def load_xp(filename):

    with gzip.open(filename, "rb") as file:

        version = struct.unpack("<i", file.read(4))[0]
        layer_count = struct.unpack("<i", file.read(4))[0]

        width = struct.unpack("<i", file.read(4))[0]
        height = struct.unpack("<i", file.read(4))[0]

        cells = [[None for _ in range(width)] for _ in range(height)]

        for x in range(width):
            for y in range(height):
                cells[y][x] = struct.unpack("<i6B", file.read(10))

    return cells


