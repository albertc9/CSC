from pymtl3 import *
from pymtl3.stdlib.test_utils import config_model_with_cmdline_opts
from cpt4.RegIncr import RegIncr

def test_basic(cmdline_opts):
    model = RegIncr()
    model = config_model_with_cmdline_opts(model, cmdline_opts, duts=[])

    model.apply(DefaultPassGroup(linetrace=True))
    model.sim_reset()

    def t(in_, out):
        model.in_ @= in_
        model.sim_eval_combinational()

        if out != '?':
            assert model.out == out

        model.sim_tick()

    t(0x00, '?')
    t(0x13, 0x01)
    t(0x27, 0x14)
    t(0x00, 0x28)
    t(0x00, 0x01)
    t(0x00, 0x01)