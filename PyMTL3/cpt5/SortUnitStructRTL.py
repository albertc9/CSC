from pymtl3 import *
from pymtl3.stdlib.basic_rtl import Reg, RegRst
from MinMaxUnit import MinMaxUnit  # 引入最小-最大单元模块

class SortUnitStructRTL(Component):
    def construct(s, nbits=8):
        # ---------------------------------------------------------------------
        # 接口定义
        # ---------------------------------------------------------------------
        s.in_val = InPort()  # 输入有效信号
        s.in_ = [InPort(nbits) for _ in range(4)]  # 4个输入端口，每个宽度为nbits
        s.out_val = OutPort()  # 输出有效信号
        s.out = [OutPort(nbits) for _ in range(4)]  # 4个输出端口

        # ---------------------------------------------------------------------
        # Stage S0->S1: 流水线寄存器
        # ---------------------------------------------------------------------
        # 输入有效信号寄存器化（带复位功能）
        s.val_S0S1 = RegRst(Bits1)  
        s.val_S0S1.in_ //= s.in_val  # 将输入有效信号连接到寄存器输入

        # 输入数据寄存器化
        s.elm_S0S1 = [Reg(mk_bits(nbits)) for _ in range(4)]
        for i in range(4):
            s.elm_S0S1[i].in_ //= s.in_[i]  # 将每个输入端口连接到对应寄存器的输入端口

        # ---------------------------------------------------------------------
        # Stage S1: 组合逻辑（最小-最大排序单元）
        # ---------------------------------------------------------------------
        # 第一组比较单元
        s.minmax0_S1 = m = MinMaxUnit(nbits)  # 实例化一个最小-最大单元
        m.in0 //= s.elm_S0S1[0].out  # 第1个寄存器的输出连接到最小-最大单元的输入0
        m.in1 //= s.elm_S0S1[1].out  # 第2个寄存器的输出连接到最小-最大单元的输入1

        # 第二组比较单元
        s.minmax1_S1 = m = MinMaxUnit(nbits)
        m.in0 //= s.elm_S0S1[2].out
        m.in1 //= s.elm_S0S1[3].out

    def line_trace(s):
        # 显示输入、寄存器和输出的状态
        in_values = ", ".join([f"{x}" for x in s.in_])
        reg_values = ", ".join([f"{x.out}" for x in s.elm_S0S1])
        out_values = ", ".join([f"{x}" for x in s.out])
        return f"in: [{in_values}] | regs: [{reg_values}] | out: [{out_values}]"