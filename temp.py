import threading
import time
import numpy as np

TILE_SIZE = 2


# def out_of_place_block_wise_kernel(odata, idata, matrix_dim):
#     tile = [[0 for _ in range(TILE_SIZE)] for _ in range(TILE_SIZE)]
#     src_ix = get_src_ix(thread_id_x, block_id_x, matrix_dim)
#     dst_ix = get_dst_ix(thread_id_x, block_id_x, matrix_dim)
#     tile[thread_id_x.y][thread_id_x.x] = idata[src_ix]
#
#     sync_threads()
#
#     odata[dst_ix] = tile[thread_id_x.x][thread_id_x.y]
#
#
# def transpose(m, matrix_dim, block_ix):
#     src_ix = get_src_ix(thread_id_x, block_ix, matrix_dim.x)
#     dst_ix = get_dst_ix(thread_id_x, block_ix, matrix_dim.x)
#     upper_tile = [[0 for _ in range(TILE_SIZE)] for _ in range(TILE_SIZE)]
#     lower_tile = [[0 for _ in range(TILE_SIZE)] for _ in range(TILE_SIZE)]
#
#     sync_threads()
#
#     m[src_ix] = lower_tile[thread_id_x.x][thread_id_x.y]
#     m[dst_ix] = upper_tile[thread_id_x.x][thread_id_x.y]
#
#
# def in_place_block_wise_kernel(m, matrix_dim):
#     if block_id_x.x <= block.id_x.y:
#         transpose(m, matrix_dim, block_id_x)


# in-place?
def transpose_threads(matrix):
    threads = []
    size = len(matrix)
    startTime = time.time()
    for i in range(size):
        for j in range(i+1, size):
            thread = threading.Thread(target = transpose_step, args = (i, j, matrix))
            threads.append(thread)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    endTime = time.time()
    duration = endTime - startTime
    return duration

def transpose_step(i, j, matrix):
    matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]


def transpose(matrix):
    # Transpose O(N*N)
    size = len(matrix)
    startTime = time.time()
    for i in range(size):
        for j in range(i+1, size):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    endTime = time.time()
    duration = endTime - startTime
    return duration


def sync_threads():
    pass


def get_src_ix(thread_id_x, block_id_x, matrix_dim):
    pass


def get_dst_ix(thread_id_x, block_id_x, matrix_dim):
    pass


if __name__ == "__main__":
    min_value = 1
    max_value = 10
    for n in range(5, 25, 1):
        matrix_size = (100 * n, 100 * n)
        matrix = np.random.randint(min_value, max_value, size = matrix_size)
        duration = transpose(matrix)
        duration_threads = transpose_threads(matrix)
        print("-" * 50)
        print("matrix size = " + str(matrix_size))
        print("transposition without threads - duration = " + str(round(duration, 2)))
        print("transposition with threads - duration = " + str(round(duration_threads, 2)))
        result = duration_threads/duration
        print("transposition without threads is " + str(round(result, 2)) + " times faster than with threads")
