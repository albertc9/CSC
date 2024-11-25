from pymtl3 import *

class RegIncr(Component):

    def construct(s):

        # 端口接口
        s.in_ = InPort(Bits8)
        s.out = OutPort(Bits8)

        # 内部信号
        s.reg_out = Wire(8)

        # 寄存器逻辑
        @update_ff
        def block1():
            if s.reset:
                s.reg_out <<= 0
            else:
                s.reg_out <<= s.in_

        # 递增逻辑
        @update
        def block2():
            s.out @= s.reg_out + 1

    def line_trace(s):
        return f"{s.in_} ({s.reg_out}) {s.out}"