from data import MatrixDim, RegionIdx


def in_place_region_kernel(matrix, matrix_dim: MatrixDim, region_idx: RegionIdx):
    block_ix = None
    block_ix.x = region_idx.x * region_dim.x + block_idx.x
    block_ix.y = region_idx.x * region_dim.x + block_idx.x
