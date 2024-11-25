from pymtl3 import *
from pymtl3.stdlib.test_utils import run_test_vector_sim
from cpt4.RegIncr import RegIncr

# 测试小输入值
def test_small(cmdline_opts):
    run_test_vector_sim(RegIncr(), [
        ('in_ out*'),
        [ 0x00, '?' ],   # 第一个周期，我们不关心输出
        [ 0x03, 0x01 ],  # 输入 0x03，期望输出 0x01（上个周期递增 1）
        [ 0x06, 0x04 ],  # 输入 0x06，期望输出 0x04
        [ 0x00, 0x07 ],  # 输入 0x00，期望输出 0x07
    ], cmdline_opts)

# 测试大输入值
def test_large(cmdline_opts):
    run_test_vector_sim(RegIncr(), [
        ('in_ out*'),
        [ 0xa0, '?' ],   # 输入较大值，第一周期不关心输出
        [ 0xb3, 0xa1 ],  # 输入 0xb3，期望输出 0xa1
        [ 0xc6, 0xb4 ],  # 输入 0xc6，期望输出 0xb4
        [ 0x00, 0xc7 ],  # 输入 0x00，期望输出 0xc7
    ], cmdline_opts)

# 测试溢出情况
def test_overflow(cmdline_opts):
    run_test_vector_sim(RegIncr(), [
        ('in_ out*'),
        [ 0x00, '?' ],   # 第一个周期，不关心输出
        [ 0xfe, 0x01 ],  # 输入 0xfe，期望输出 0x01（0xfe + 1 = 0xff，下一周期回到 0x01）
        [ 0xff, 0xff ],  # 输入 0xff，递增至溢出，保持 0xff
        [ 0x00, 0x00 ],  # 输入 0x00，重置输出为 0x00
    ], cmdline_opts)