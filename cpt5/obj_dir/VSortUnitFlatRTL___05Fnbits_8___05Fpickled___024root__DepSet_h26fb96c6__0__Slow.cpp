// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See VSortUnitFlatRTL___05Fnbits_8___05Fpickled.h for the primary calling header

#include "VSortUnitFlatRTL___05Fnbits_8___05Fpickled__pch.h"
#include "VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root.h"

VL_ATTR_COLD void VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_static(VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VSortUnitFlatRTL___05Fnbits_8___05Fpickled__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_static\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
}

VL_ATTR_COLD void VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_initial(VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VSortUnitFlatRTL___05Fnbits_8___05Fpickled__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_initial\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
}

VL_ATTR_COLD void VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_final(VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VSortUnitFlatRTL___05Fnbits_8___05Fpickled__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_final\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
}

VL_ATTR_COLD void VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_settle(VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VSortUnitFlatRTL___05Fnbits_8___05Fpickled__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_settle\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
}

#ifdef VL_DEBUG
VL_ATTR_COLD void VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___dump_triggers__act(VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VSortUnitFlatRTL___05Fnbits_8___05Fpickled__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___dump_triggers__act\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if ((1U & (~ vlSelfRef.__VactTriggered.any()))) {
        VL_DBG_MSGF("         No triggers active\n");
    }
}
#endif  // VL_DEBUG

#ifdef VL_DEBUG
VL_ATTR_COLD void VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___dump_triggers__nba(VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VSortUnitFlatRTL___05Fnbits_8___05Fpickled__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___dump_triggers__nba\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if ((1U & (~ vlSelfRef.__VnbaTriggered.any()))) {
        VL_DBG_MSGF("         No triggers active\n");
    }
}
#endif  // VL_DEBUG

VL_ATTR_COLD void VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___ctor_var_reset(VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VSortUnitFlatRTL___05Fnbits_8___05Fpickled__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___ctor_var_reset\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Body
    vlSelf->clk = VL_RAND_RESET_I(1);
    for (int __Vi0 = 0; __Vi0 < 4; ++__Vi0) {
        vlSelf->in_[__Vi0] = VL_RAND_RESET_I(8);
    }
    vlSelf->in_val = VL_RAND_RESET_I(1);
    for (int __Vi0 = 0; __Vi0 < 4; ++__Vi0) {
        vlSelf->out[__Vi0] = VL_RAND_RESET_I(8);
    }
    vlSelf->out_val = VL_RAND_RESET_I(1);
    vlSelf->reset = VL_RAND_RESET_I(1);
}
