from pymtl3 import *
from test11 import *

# 创建模型
regi = Incre(8)

# 应用仿真器
regi.apply(DefaultPassGroup())

# 时钟清零
regi.sim_reset()

# @=表示信号赋值操作符，组合逻辑
regi.in_ @= 42

# 仿真器走一个时钟周期
regi.sim_tick()

# 测试验证
if regi.out == 43:
    print("Success!")
else:
    print(f"Failed!{regi.out}")