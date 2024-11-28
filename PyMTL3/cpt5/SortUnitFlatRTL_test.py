from pymtl3 import *
from pymtl3.stdlib.test_utils import run_test_vector_sim

from SortUnitFlatRTL import SortUnitFlatRTL  # 引入待测模块

def test_sort_unit_flatrtl(cmdline_opts):
    # 定义测试向量
    test_vectors = [
        ('in_val in_[0] in_[1] in_[2] in_[3] out_val out[0] out[1] out[2] out[3]'),
        # 初始阶段，输入信号无效，但输入必须为合法值（如全为 0）
        [  0,      0x00,   0x00,   0x00,   0x00,   0,      0x00,   0x00,   0x00,   0x00 ],
        # 输入第一组数据，排序结果不可用
        [  1,      0x03,   0x09,   0x04,   0x01,   0,      0x00,   0x00,   0x00,   0x00 ],
        # 第一阶段寄存器传递数据
        [  0,      0x00,   0x00,   0x00,   0x00,   1,      0x01,   0x03,   0x04,   0x09 ],
        # 输入第二组数据，排序结果不可用
        [  1,      0x10,   0x20,   0x15,   0x05,   0,      0x01,   0x03,   0x04,   0x09 ],
        # 第二组排序完成
        [  0,      0x00,   0x00,   0x00,   0x00,   1,      0x05,   0x10,   0x15,   0x20 ],
    ]

    # 运行测试
    run_test_vector_sim(SortUnitFlatRTL(), test_vectors, cmdline_opts, print_line_trace=True)