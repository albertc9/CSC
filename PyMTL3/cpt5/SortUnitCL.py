from collections import deque
from copy import deepcopy
from pymtl3 import *
from SortUnitFL import sort_fl

# 排序单元 CL 模型
class SortUnitCL(Component):

    # 构造函数
    def construct(s, nbits=8, nstages=3):
        # 定义输入端口
        s.in_val = InPort()
        s.in_ = [InPort(nbits) for _ in range(4)]
        
        # 定义输出端口
        s.out_val = OutPort()
        s.out = [OutPort(nbits) for _ in range(4)]
        
        # 初始化流水线队列
        s.pipe = deque([[0, 0, 0, 0, 0]] * (nstages - 1))

        # 更新块：核心排序与流水线逻辑
        @update_ff
        def block():
            # 将输入值与有效性标志排序后存入队列
            s.pipe.append(deepcopy([s.in_val] + sort_fl(s.in_)))
            # 从队列中取出最早的值
            data = s.pipe.popleft()
            # 更新输出端口
            s.out_val <<= data[0]
            for i, v in enumerate(data[1:]):
                s.out[i] <<= v

    # 行跟踪（显示输入输出状态）
    def line_trace(s):
        # 输入状态字符串
        in_str = '{' + ','.join(map(str, s.in_)) + '}'
        if not s.in_val:
            in_str = ' ' * len(in_str)

        # 输出状态字符串
        out_str = '{' + ','.join(map(str, s.out)) + '}'
        if not s.out_val:
            out_str = ' ' * len(out_str)

        # 返回格式化的输入输出状态
        return f"{in_str}|{out_str}"