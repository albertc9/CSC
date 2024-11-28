// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design internal header
// See VSortUnitFlatRTL___05Fnbits_8___05Fpickled.h for the primary calling header

#ifndef VERILATED_VSORTUNITFLATRTL___05FNBITS_8___05FPICKLED___024ROOT_H_
#define VERILATED_VSORTUNITFLATRTL___05FNBITS_8___05FPICKLED___024ROOT_H_  // guard

#include "verilated.h"


class VSortUnitFlatRTL___05Fnbits_8___05Fpickled__Syms;

class alignas(VL_CACHE_LINE_BYTES) VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root final : public VerilatedModule {
  public:

    // DESIGN SPECIFIC STATE
    VL_IN8(clk,0,0);
    VL_IN8(in_val,0,0);
    VL_OUT8(out_val,0,0);
    VL_IN8(reset,0,0);
    CData/*0:0*/ __VactContinue;
    IData/*31:0*/ __VactIterCount;
    VL_IN8(in_[4],7,0);
    VL_OUT8(out[4],7,0);
    VlTriggerVec<0> __VactTriggered;
    VlTriggerVec<0> __VnbaTriggered;

    // INTERNAL VARIABLES
    VSortUnitFlatRTL___05Fnbits_8___05Fpickled__Syms* const vlSymsp;

    // CONSTRUCTORS
    VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root(VSortUnitFlatRTL___05Fnbits_8___05Fpickled__Syms* symsp, const char* v__name);
    ~VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root();
    VL_UNCOPYABLE(VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root);

    // INTERNAL METHODS
    void __Vconfigure(bool first);
};


#endif  // guard
