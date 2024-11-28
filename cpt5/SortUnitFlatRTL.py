#=========================================================================
# SortUnitFlatRTL
#=========================================================================
# Flat RTL model of a four-element sort unit. This model demonstrates how
# to use PyMTL3 to construct a bitonic sorting network using explicit
# wires and logic.

from pymtl3 import *

class SortUnitFlatRTL( Component ):

    def construct( s, nbits=8 ):
        #-----------------------------------------------------------------
        # Interface
        #-----------------------------------------------------------------

        s.in_val = InPort()                        # Input valid signal
        s.in_ = [ InPort(nbits) for _ in range(4) ]  # Four input elements

        s.out_val = OutPort()                      # Output valid signal
        s.out = [ OutPort(nbits) for _ in range(4) ] # Four output elements

        #-----------------------------------------------------------------
        # Stage S0->S1 pipeline registers
        #-----------------------------------------------------------------

        s.val_S1 = Wire()                          # Valid signal for stage S1
        s.elm_S1 = [ Wire(nbits) for _ in range(4) ] # Data wires for stage S1

        @update_ff
        def pipereg_S0S1():
            if s.reset:
                s.val_S1 <<= 0
            else:
                s.val_S1 <<= s.in_val

            for i in range(4):
                s.elm_S1[i] <<= s.in_[i]

        #-----------------------------------------------------------------
        # Stage S1 combinational logic
        #-----------------------------------------------------------------

        s.elm_next_S1 = [ Wire(nbits) for _ in range(4) ] # Sorted elements for stage S1

        @update
        def stage_S1():
            # Sort elements 0 and 1
            if s.elm_S1[0] <= s.elm_S1[1]:
                s.elm_next_S1[0] @= s.elm_S1[0]
                s.elm_next_S1[1] @= s.elm_S1[1]
            else:
                s.elm_next_S1[0] @= s.elm_S1[1]
                s.elm_next_S1[1] @= s.elm_S1[0]

            # Sort elements 2 and 3
            if s.elm_S1[2] <= s.elm_S1[3]:
                s.elm_next_S1[2] @= s.elm_S1[2]
                s.elm_next_S1[3] @= s.elm_S1[3]
            else:
                s.elm_next_S1[2] @= s.elm_S1[3]
                s.elm_next_S1[3] @= s.elm_S1[2]

        #-----------------------------------------------------------------
        # Stage S1->S2 pipeline registers
        #-----------------------------------------------------------------

        s.val_S2 = Wire()
        s.elm_S2 = [ Wire(nbits) for _ in range(4) ]

        @update_ff
        def pipereg_S1S2():
            if s.reset:
                s.val_S2 <<= 0
            else:
                s.val_S2 <<= s.val_S1

            for i in range(4):
                s.elm_S2[i] <<= s.elm_next_S1[i]

        #-----------------------------------------------------------------
        # Stage S2 combinational logic
        #-----------------------------------------------------------------

        s.elm_next_S2 = [ Wire(nbits) for _ in range(4) ]

        @update
        def stage_S2():
            # Sort elements 0 and 2
            if s.elm_S2[0] <= s.elm_S2[2]:
                s.elm_next_S2[0] @= s.elm_S2[0]
                s.elm_next_S2[2] @= s.elm_S2[2]
            else:
                s.elm_next_S2[0] @= s.elm_S2[2]
                s.elm_next_S2[2] @= s.elm_S2[0]

            # Sort elements 1 and 3
            if s.elm_S2[1] <= s.elm_S2[3]:
                s.elm_next_S2[1] @= s.elm_S2[1]
                s.elm_next_S2[3] @= s.elm_S2[3]
            else:
                s.elm_next_S2[1] @= s.elm_S2[3]
                s.elm_next_S2[3] @= s.elm_S2[1]

        #-----------------------------------------------------------------
        # Stage S2->S3 pipeline registers
        #-----------------------------------------------------------------

        s.val_S3 = Wire()
        s.elm_S3 = [ Wire(nbits) for _ in range(4) ]

        @update_ff
        def pipereg_S2S3():
            if s.reset:
                s.val_S3 <<= 0
            else:
                s.val_S3 <<= s.val_S2

            for i in range(4):
                s.elm_S3[i] <<= s.elm_next_S2[i]

        #-----------------------------------------------------------------
        # Stage S3 combinational logic
        #-----------------------------------------------------------------

        s.elm_next_S3 = [ Wire(nbits) for _ in range(4) ]

        @update
        def stage_S3():
            # Sort elements 1 and 2
            if s.elm_S3[1] <= s.elm_S3[2]:
                s.elm_next_S3[1] @= s.elm_S3[1]
                s.elm_next_S3[2] @= s.elm_S3[2]
            else:
                s.elm_next_S3[1] @= s.elm_S3[2]
                s.elm_next_S3[2] @= s.elm_S3[1]

            # Pass through elements 0 and 3
            s.elm_next_S3[0] @= s.elm_S3[0]
            s.elm_next_S3[3] @= s.elm_S3[3]

        #-----------------------------------------------------------------
        # Stage S3->Output pipeline registers
        #-----------------------------------------------------------------

        @update_ff
        def pipereg_S3Out():
            if s.reset:
                s.out_val <<= 0
            else:
                s.out_val <<= s.val_S3

            for i in range(4):
                s.out[i] <<= s.elm_next_S3[i]

        #-----------------------------------------------------------------
        # Line Tracing
        #-----------------------------------------------------------------

        def line_trace( s ):
            return f"{s.in_} ({s.val_S1}|{s.val_S2}|{s.val_S3}) {s.out}"