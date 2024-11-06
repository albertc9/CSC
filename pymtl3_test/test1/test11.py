#=========================================================================
# RegIncr
# p14 Figure8: A registered incrementer
#=========================================================================
# This is a simple model for a registered incrementer. An eight-bit value
# is read from the input port, registered, incremented by one, and
# finally written to the output port.

from pymtl3 import *

class Incre(Component):
    def construct(s, nbits):

        # 声明输入输出端口
        s.in_ = InPort(nbits)
        s.out = OutPort(nbits)

        # 内部的线网变量
        s.reg_out = Wire(nbits)

        # 时序逻辑 用于寄存 
        @update_ff
        def block1():
            # reset是Component的默认内置信号
            if s.reset:
                # 表示非阻塞赋值
                s.reg_out <<= 0
            else:
                s.reg_out <<= s.in_

        # 组合逻辑 用于加1
        @update
        def block2():
            s.out @= s.reg_out + 1