from pymtl3 import *
from pymtl3.stdlib.test_utils import run_test_vector_sim
from SortUnitFL import SortUnitFL

# 基本测试
def test_basic(cmdline_opts):
    run_test_vector_sim(SortUnitFL(), [
        # 定义测试向量表：第一行为端口名称，后续行为测试数据
        ('in_val in_[0] in_[1] in_[2] in_[3] out_val out[0] out[1] out[2] out[3]*'),
        # 复位周期：无输入，无输出
        [ 0,      0,    0,    0,    0,    0,     0,     0,     0,     0       ],
        # 第一个输入周期：输入有效，等待排序结果
        [ 1,      8,    3,    5,    1,    0,     0,     0,     0,     0       ],
        # 输出周期：输出排序结果
        [ 0,      0,    0,    0,    0,    1,     1,     3,     5,     8       ],
    ], cmdline_opts)

# 随机测试
def test_random(cmdline_opts):
    import random
    # 定义测试向量表
    test_vector_table = [
        ('in_val in_[0] in_[1] in_[2] in_[3] out_val out[0] out[1] out[2] out[3]*')
    ]
    # 添加复位周期
    test_vector_table.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    
    # 生成随机输入测试
    for _ in range(20):
        # 随机生成4个输入值
        rand_inputs = [random.randint(0, 255) for _ in range(4)]
        sorted_outputs = sorted(rand_inputs)  # 对随机输入进行排序
        # 输入有效周期
        test_vector_table.append([1] + rand_inputs + [0] + [0, 0, 0, 0])
        # 输出有效周期
        test_vector_table.append([0, 0, 0, 0, 0, 1] + sorted_outputs)
    
    # 运行测试
    run_test_vector_sim(SortUnitFL(), test_vector_table, cmdline_opts)