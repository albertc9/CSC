from pymtl3 import *

class SortUnitFlatRTL(Component):

    def construct(s, nbits=8):
        # 接口定义
        s.in_val = InPort()                      # 输入有效信号
        s.in_ = [InPort(nbits) for _ in range(4)] # 输入端口数组
        s.out_val = OutPort()                    # 输出有效信号
        s.out = [OutPort(nbits) for _ in range(4)] # 输出端口数组

        # 第一阶段输入寄存器（S0 -> S1）
        s.val_S1 = Wire()                          # 有效性信号寄存器
        s.elm_S1 = [Wire(nbits) for _ in range(4)] # 数据寄存器

        @update_ff
        def pipereg_S0S1():
            if s.reset:
                s.val_S1 <<= 0                    # 复位时清零有效性信号
            else:
                s.val_S1 <<= s.in_val             # 正常传递有效性信号

            for i in range(4):                    # 输入数据存入寄存器
                s.elm_S1[i] <<= s.in_[i]

        # 第一阶段组合逻辑（S1）
        s.elm_next_S1 = [Wire(nbits) for _ in range(4)] # 下一阶段数据

        @update
        def stage_S1():
            # 比较输入数据对 (0,1)
            if s.elm_S1[0] <= s.elm_S1[1]:
                s.elm_next_S1[0] @= s.elm_S1[0]
                s.elm_next_S1[1] @= s.elm_S1[1]
            else:
                s.elm_next_S1[0] @= s.elm_S1[1]
                s.elm_next_S1[1] @= s.elm_S1[0]

            # 比较输入数据对 (2,3)
            if s.elm_S1[2] <= s.elm_S1[3]:
                s.elm_next_S1[2] @= s.elm_S1[2]
                s.elm_next_S1[3] @= s.elm_S1[3]
            else:
                s.elm_next_S1[2] @= s.elm_S1[3]
                s.elm_next_S1[3] @= s.elm_S1[2]

    def line_trace(s):
            in_str = ','.join([f"{x}" for x in s.in_])
            out_str = ','.join([f"{x}" for x in s.out])
            return f"in_val: {s.in_val} in: [{in_str}] | out_val: {s.out_val} out: [{out_str}]"