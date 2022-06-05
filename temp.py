TILE_SIZE = 2


def out_of_place_block_wise_kernel(odata, idata, matrix_dim):
    tile = [[0 for _ in range(TILE_SIZE)] for _ in range(TILE_SIZE)]
    src_ix = get_src_ix(thread_id_x, block_id_x, matrix_dim)
    dst_ix = get_dst_ix(thread_id_x, block_id_x, matrix_dim)
    tile[thread_id_x.y][thread_id_x.x] = idata[src_ix]

    sync_threads()

    odata[dst_ix] = tile[thread_id_x.x][thread_id_x.y]


def transpose(m, matrix_dim, block_ix):
    src_ix = get_src_ix(thread_id_x, block_ix, matrix_dim.x)
    dst_ix = get_dst_ix(thread_id_x, block_ix, matrix_dim.x)
    upper_tile = [[0 for _ in range(TILE_SIZE)] for _ in range(TILE_SIZE)]
    lower_tile = [[0 for _ in range(TILE_SIZE)] for _ in range(TILE_SIZE)]

    sync_threads()

    m[src_ix] = lower_tile[thread_id_x.x][thread_id_x.y]
    m[dst_ix] = upper_tile[thread_id_x.x][thread_id_x.y]


def in_place_block_wise_kernel(m, matrix_dim):
    if block_id_x.x <= block.id_x.y:
        transpose(m, matrix_dim, block_id_x)


# in-place?
def transpose(matrix):
    # Transpose O(N*N)
    size = len(matrix)
    for i in range(size):
        for j in range(i+1, size):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]


def sync_threads():
    pass


def get_src_ix(thread_id_x, block_id_x, matrix_dim):
    pass


def get_dst_ix(thread_id_x, block_id_x, matrix_dim):
    pass
