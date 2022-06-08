import threading
import time
import numpy as np

TILE_SIZE = 2


def transpose_threads(matrix):
    threads = []
    size = len(matrix)
    startTime = time.time()
    for i in range(size):
        thread = threading.Thread(target=transpose_step, args=(i, matrix))
        threads.append(thread)

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    endTime = time.time()
    duration = endTime - startTime
    return duration

def transpose_step(i, matrix):
    size = len(matrix)
    for j in range(i + 1, size):
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
    # for n in range(5, 25, 1):
    matrix_size = (20000, 20000)
    matrix = np.random.randint(min_value, max_value, size = matrix_size)
    duration = transpose(matrix)
    duration_threads = transpose_threads(matrix)
    print("-" * 50)
    print("matrix size = " + str(matrix_size))
    print("transposition without threads - duration = " + str(round(duration, 2)))
    print("transposition with threads - duration = " + str(round(duration_threads, 2)))
    result = duration_threads/duration
    print("transposition without threads is " + str(round(result, 2)) + " times faster than with threads")
