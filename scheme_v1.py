from math import floor, sqrt

from data import BlockIdx


class SchemeV1:
    @staticmethod
    def get_k(block_id_x: BlockIdx, grid_dim):
        x, y = block_id_x.x, block_id_x.y
        return (y**2 - y) / 2 + x

    @staticmethod
    def decode_y(k):
        return floor((sqrt(8 * k + 1) + 1) / 2)

    @staticmethod
    def decode_x(k, y):
        return k - ((y**2 - y) / 2)
