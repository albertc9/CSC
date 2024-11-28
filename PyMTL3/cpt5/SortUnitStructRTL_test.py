#=========================================================================
# SortUnitStructRTL_test
#=========================================================================
# 测试 SortUnitStructRTL 模块，包括基本功能测试和随机输入测试。

import random
import pytest
from pymtl3 import *
from pymtl3.stdlib.test_utils import run_test_vector_sim

# 引入待测试的模块
from SortUnitStructRTL import SortUnitStructRTL

#-------------------------------------------------------------------------
# Helper Function: 生成测试向量表
#-------------------------------------------------------------------------
def mk_test_vector_table(input_data, valid_bit=True):
    """
    创建测试向量表。
    :param input_data: 输入数据列表，每个元素是长度为4的列表。
    :param valid_bit: 输入信号是否有效。
    :return: 测试向量表，包含输入数据和期望输出。
    """
    nbits = 8
    test_vector_table = [('in_val', 'in_[0]', 'in_[1]', 'in_[2]', 'in_[3]', 'out_val*', 'out[0]*', 'out[1]*', 'out[2]*', 'out[3]*')]

    for data in input_data:
        sorted_data = sorted(data)  # 期望输出为排序后的数据
        if valid_bit:
            test_vector_table.append([1] + data + [1] + sorted_data)
        else:
            test_vector_table.append([0] + data + [0] + [0]*4)  # 无效信号，输出应为0

    return test_vector_table

#-------------------------------------------------------------------------
# 测试用例: 基本功能测试
#-------------------------------------------------------------------------
def test_basic(cmdline_opts):
    """
    测试模块基本功能，包括简单的排序逻辑。
    """
    input_data = [
        [0x04, 0x02, 0x03, 0x01],  # 输入：无序数据
        [0x10, 0x30, 0x20, 0x40],  # 输入：另一组无序数据
        [0x00, 0xFF, 0x7F, 0x80],  # 输入：包含最大值和最小值
    ]
    test_vector_table = mk_test_vector_table(input_data)
    run_test_vector_sim(SortUnitStructRTL(), test_vector_table, cmdline_opts)

#-------------------------------------------------------------------------
# 测试用例: 无效信号测试
#-------------------------------------------------------------------------
def test_invalid_signal(cmdline_opts):
    """
    测试当输入有效信号为0时，输出是否为0。
    """
    input_data = [
        [0x04, 0x02, 0x03, 0x01],  # 输入：无序数据
    ]
    test_vector_table = mk_test_vector_table(input_data, valid_bit=False)
    run_test_vector_sim(SortUnitStructRTL(), test_vector_table, cmdline_opts)

#-------------------------------------------------------------------------
# 测试用例: 随机输入测试
#-------------------------------------------------------------------------
def test_random(cmdline_opts):
    """
    测试随机输入数据的排序逻辑。
    """
    random.seed(42)  # 固定随机种子，确保测试可重复
    input_data = [[random.randint(0, 0xFF) for _ in range(4)] for _ in range(10)]  # 生成10组随机数据
    test_vector_table = mk_test_vector_table(input_data)
    run_test_vector_sim(SortUnitStructRTL(), test_vector_table, cmdline_opts)

#-------------------------------------------------------------------------
# 测试用例: 边界值测试
#-------------------------------------------------------------------------
def test_boundary_values(cmdline_opts):
    """
    测试边界值，包括全0和全最大值。
    """
    input_data = [
        [0x00, 0x00, 0x00, 0x00],  # 全0
        [0xFF, 0xFF, 0xFF, 0xFF],  # 全最大值
    ]
    test_vector_table = mk_test_vector_table(input_data)
    run_test_vector_sim(SortUnitStructRTL(), test_vector_table, cmdline_opts)

#-------------------------------------------------------------------------
# 主测试函数
#-------------------------------------------------------------------------
@pytest.mark.parametrize("test", [test_basic, test_invalid_signal, test_random, test_boundary_values])
def test_all(test, cmdline_opts):
    """
    参数化测试，运行所有测试用例。
    """
    test(cmdline_opts)