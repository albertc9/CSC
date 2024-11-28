from pymtl3 import *
from RegIncr import RegIncr

class RegIncr2stage( Component ):
    
    # 构造函数
    def construct( s ):
        
        # 接口定义：输入和输出均为 8 位宽
        s.in_ = InPort(8)
        s.out = OutPort(8)
        
        # 第一级：实例化第一个单级寄存递增器
        s.reg_incr_0 = RegIncr()
        connect( s.in_, s.reg_incr_0.in_ )
        
        # 第二级：实例化第二个单级寄存递增器
        s.reg_incr_1 = RegIncr()
        s.reg_incr_0.out //= s.reg_incr_1.in_  # 使用//= 连接信号
        s.reg_incr_1.out //= s.out

    def line_trace( s ):
        return "{} ({}|{}) {}".format(
            s.in_,
            s.reg_incr_0.line_trace(),  # 第一阶段的线性跟踪
            s.reg_incr_1.line_trace(),  # 第二阶段的线性跟踪
            s.out
        )