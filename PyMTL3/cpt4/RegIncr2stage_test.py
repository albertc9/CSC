import random
from pymtl3 import *
from pymtl3.stdlib.test_utils import run_test_vector_sim
from RegIncr2stage import RegIncr2stage

# 小值测试
def test_small( cmdline_opts ):

    run_test_vector_sim( 
        RegIncr2stage(), 
        [
        ('in_', 'out*'),
        [ 0x00,'?' ],  # 第一周期：输出未知
        [ 0x03,'?' ],  # 第二周期：输出未知
        [ 0x06, 0x02 ],  # 第三周期：输出0x02（0x00+2）
        [ 0x00, 0x05 ],  # 第四周期：输出0x05（0x03+2）
        [ 0x00, 0x08 ],  # 第五周期：输出0x08（0x06+2）
    ],
    cmdline_opts
    )

# 随机测试
def test_random( cmdline_opts ):
    test_vector_table = [('in_', 'out*')]
    last_result_0 = '?'
    last_result_1 = '?'
    for _ in range(20):
        rand_value = b8( random.randint(0, 0xff) )
        test_vector_table.append([rand_value, last_result_1])
        last_result_1 = last_result_0
        last_result_0 = b8(rand_value + 2, trunc_int=True)
    run_test_vector_sim( RegIncr2stage(), test_vector_table, cmdline_opts )