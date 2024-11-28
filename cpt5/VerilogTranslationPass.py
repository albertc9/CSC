from pymtl3 import *
from pymtl3.passes.backends.verilog import *
from SortUnitFlatRTL import SortUnitFlatRTL

model = SortUnitFlatRTL()

# 启用Verilog翻译功能
model.set_metadata(VerilogTranslationPass.enable, True)

# 应用Verilog翻译
model.apply(VerilogTranslationPass())