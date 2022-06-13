from threading import Thread
import time
import numpy as np

SIZE = 1500
TILE_SIZE = 500

class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return


def transpose_step(matrix):
    size = len(matrix)
    copy = matrix.copy()
    for i in range(size):
        for j in range(i+1, size):
            copy[j][i], copy[i][j] = matrix[i][j], matrix[j][i]
    return copy

def transpose_threads(matrix):
    startTime = time.time()
    threads = []
    tiles = []
    output_matrix = []
    size = len(matrix)
    tiles_in_row_number = size//TILE_SIZE

    for i in range(size):
        if i % TILE_SIZE == 0:
            rows = []
            for j in range(size):
                if j % TILE_SIZE == 0:
                    matrix_tile = matrix[i:i + TILE_SIZE, j:j + TILE_SIZE]
                    rows.append(matrix_tile)
                    thread = ThreadWithReturnValue(target=transpose_step, args=(matrix_tile,))
                    threads.append(thread)
            tiles.append(rows)
    for thread in threads:
        thread.start()

    output_row = []
    for i, thread in enumerate(threads):
        ret_value = thread.join()
        output_row.append(ret_value)
        if (i + 1) % tiles_in_row_number == 0:
            output_matrix.append(output_row)
            output_row = []

    for i in range(tiles_in_row_number):
        for j in range(i+1, tiles_in_row_number):
            output_matrix[j][i], output_matrix[i][j] = output_matrix[i][j], output_matrix[j][i]
    # tutaj mamy listę list z małymi macierzami,
    # nie wiem czy żeby spełniano to warunki trzeba by było doprowadzić to do takiej samej
    # postaci jak w transpose() ??
    return time.time() - startTime


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


if __name__ == "__main__":
    min_value = 1
    max_value = 10
    # for n in range(5, 25, 1):
    matrix_size = (SIZE, SIZE)
    random_matrix = np.random.randint(min_value, max_value, size = matrix_size)
    duration_threads = transpose_threads(random_matrix)
    duration = transpose(random_matrix)
    print("-" * 50)
    print("matrix size = " + str(matrix_size))
    print("tile size = " + str(TILE_SIZE))
    print("transposition without threads - duration = " + str(round(duration, 2)) + " seconds")
    print("transposition with threads - duration = " + str(round(duration_threads, 2)) + " seconds")
    result = duration_threads/duration
    if result > 1.0:
        print("transposition without threads is " + str(round(result, 2)) + " times faster than with threads")
    else:
        print("transposition with threads is " + str(round(1/result, 2)) + " times faster than without threads")
