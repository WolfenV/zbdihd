from data import BlockIx
from matrix import Matrix

TILE_SIZE = 0


def transpose(m: Matrix, block_ix: BlockIx):
    src_ix = get_src_ix(thread_id_x, block_ix, m.x)
    dst_ix = get_dst_ix(thread_id_x, block_ix, m.x)
    upper_tile = [[0 for _ in range(TILE_SIZE)] for _ in range(TILE_SIZE)]
    lower_tile = [[0 for _ in range(TILE_SIZE)] for _ in range(TILE_SIZE)]

    sync_threads()

    m[src_ix] = lower_tile[thread_id_x.x][thread_id_x.y]
    m[dst_ix] = upper_tile[thread_id_x.x][thread_id_x.y]


def in_place_block_wise_kernel(m: Matrix):
    if block_id_x.x <= block.id_x.y:
        transpose(m, block_id_x)

