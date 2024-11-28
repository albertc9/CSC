from pymtl3 import *

# 排序功能实现
def sort_fl(arr):

    return sorted(arr)

# 排序单元 FL 模型
class SortUnitFL(Component):

    # 构造函数
    def construct(s, nbits=8):
        # 定义输入端口
        s.in_val = InPort()  # 输入有效性标志
        s.in_ = [InPort(nbits) for _ in range(4)]  # 四个输入端口
        
        # 定义输出端口
        s.out_val = OutPort()  # 输出有效性标志
        s.out = [OutPort(nbits) for _ in range(4)]  # 四个输出端口
        
        # 核心排序逻辑（update_ff 块）
        @update_ff
        def block():
            # 将输入有效性标志传递到输出
            s.out_val <<= s.in_val
            
            # 对输入端口值排序，并赋值到输出端口
            for i, v in enumerate(sort_fl(s.in_)):
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