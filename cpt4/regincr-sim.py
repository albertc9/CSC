#!/usr/bin/env python
#=========================================================================
# regincr-sim <input-values>
#=========================================================================
from pymtl3 import *
from sys import argv
from regIncr import RegIncr

# 从命令行获取输入值列表
input_values = [int(x, 0) for x in argv[1:]]

# 在输入值列表末尾添加三个零值，以便模拟多几个周期，方便观察输出
input_values.extend([0] * 3)

model = RegIncr()
model.elaborate()

# 应用默认的通用 Pass 组以添加模拟功能
# model.apply(DefaultPassGroup(vcdwave='regIncr-sim'))

# model.apply(DefaultPassGroup(textwave=True))

model.apply(DefaultPassGroup(textwave=True))

# 重置模拟器
model.sim_reset()

# 输入值应用与输出值显示
for input_value in input_values:
    model.in_ @= input_value
    model.sim_eval_combinational()
    
    # 显示当前周期的输入与输出
    print(f"cycle = {model.sim_cycle_count()}: in = {model.in_}, out = {model.out}")
    
    # 模拟器前进一个周期
    model.sim_tick()

    model.print_textwave()