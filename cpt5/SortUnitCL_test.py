from pymtl3 import *
from pymtl3.stdlib.test_utils import run_test_vector_sim
from SortUnitCL import SortUnitCL

def test_3stage_stream(cmdline_opts):
    run_test_vector_sim(SortUnitCL(nstages=3), [
        ('in_val in_[0] in_[1] in_[2] in_[3] out_val out[0] out[1] out[2] out[3]*'),
        [ 1,      4,    2,    3,    1,    0,     0,     0,     0,     0       ],
        [ 0,      0,    0,    0,    0,    0,     0,     0,     0,     0       ],
        [ 0,      0,    0,    0,    0,    0,     0,     0,     0,     0       ],
        [ 0,      0,    0,    0,    0,    1,     1,     2,     3,     4       ],
    ], cmdline_opts)