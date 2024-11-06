from pymtl3 import *

class SimpleALU(Component):
    def construct(s):
        s.a = InPort( Bits32 )
        s.b = InPort( Bits32 )
        s.result = OutPort( Bits32 )

        @update
        def comb_logic():
            s.result @= s.a + s.b

alu = SimpleALU()
alu.apply(DefaultPassGroup())
alu.sim_reset()
alu.a @= 10
alu.b @= 20
alu.sim_eval_combinational()
print(alu.result)  # 应输出30