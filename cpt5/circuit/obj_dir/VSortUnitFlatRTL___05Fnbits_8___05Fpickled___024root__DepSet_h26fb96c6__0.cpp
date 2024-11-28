// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See VSortUnitFlatRTL___05Fnbits_8___05Fpickled.h for the primary calling header

#include "VSortUnitFlatRTL___05Fnbits_8___05Fpickled__pch.h"
#include "VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root.h"

void VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_act(VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VSortUnitFlatRTL___05Fnbits_8___05Fpickled__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_act\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
}

void VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_nba(VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VSortUnitFlatRTL___05Fnbits_8___05Fpickled__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_nba\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
}

void VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_triggers__act(VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root* vlSelf);

bool VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_phase__act(VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VSortUnitFlatRTL___05Fnbits_8___05Fpickled__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_phase__act\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Init
    VlTriggerVec<0> __VpreTriggered;
    CData/*0:0*/ __VactExecute;
    // Body
    VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_triggers__act(vlSelf);
    __VactExecute = vlSelfRef.__VactTriggered.any();
    if (__VactExecute) {
        __VpreTriggered.andNot(vlSelfRef.__VactTriggered, vlSelfRef.__VnbaTriggered);
        vlSelfRef.__VnbaTriggered.thisOr(vlSelfRef.__VactTriggered);
        VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_act(vlSelf);
    }
    return (__VactExecute);
}

bool VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_phase__nba(VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VSortUnitFlatRTL___05Fnbits_8___05Fpickled__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_phase__nba\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Init
    CData/*0:0*/ __VnbaExecute;
    // Body
    __VnbaExecute = vlSelfRef.__VnbaTriggered.any();
    if (__VnbaExecute) {
        VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_nba(vlSelf);
        vlSelfRef.__VnbaTriggered.clear();
    }
    return (__VnbaExecute);
}

#ifdef VL_DEBUG
VL_ATTR_COLD void VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___dump_triggers__nba(VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root* vlSelf);
#endif  // VL_DEBUG
#ifdef VL_DEBUG
VL_ATTR_COLD void VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___dump_triggers__act(VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root* vlSelf);
#endif  // VL_DEBUG

void VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval(VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VSortUnitFlatRTL___05Fnbits_8___05Fpickled__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Init
    IData/*31:0*/ __VnbaIterCount;
    CData/*0:0*/ __VnbaContinue;
    // Body
    __VnbaIterCount = 0U;
    __VnbaContinue = 1U;
    while (__VnbaContinue) {
        if (VL_UNLIKELY((0x64U < __VnbaIterCount))) {
#ifdef VL_DEBUG
            VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___dump_triggers__nba(vlSelf);
#endif
            VL_FATAL_MT("SortUnitFlatRTL__nbits_8__pickled.v", 9, "", "NBA region did not converge.");
        }
        __VnbaIterCount = ((IData)(1U) + __VnbaIterCount);
        __VnbaContinue = 0U;
        vlSelfRef.__VactIterCount = 0U;
        vlSelfRef.__VactContinue = 1U;
        while (vlSelfRef.__VactContinue) {
            if (VL_UNLIKELY((0x64U < vlSelfRef.__VactIterCount))) {
#ifdef VL_DEBUG
                VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___dump_triggers__act(vlSelf);
#endif
                VL_FATAL_MT("SortUnitFlatRTL__nbits_8__pickled.v", 9, "", "Active region did not converge.");
            }
            vlSelfRef.__VactIterCount = ((IData)(1U) 
                                         + vlSelfRef.__VactIterCount);
            vlSelfRef.__VactContinue = 0U;
            if (VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_phase__act(vlSelf)) {
                vlSelfRef.__VactContinue = 1U;
            }
        }
        if (VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_phase__nba(vlSelf)) {
            __VnbaContinue = 1U;
        }
    }
}

#ifdef VL_DEBUG
void VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_debug_assertions(VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VSortUnitFlatRTL___05Fnbits_8___05Fpickled__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_debug_assertions\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if (VL_UNLIKELY((vlSelfRef.clk & 0xfeU))) {
        Verilated::overWidthError("clk");}
    if (VL_UNLIKELY((vlSelfRef.in_val & 0xfeU))) {
        Verilated::overWidthError("in_val");}
    if (VL_UNLIKELY((vlSelfRef.reset & 0xfeU))) {
        Verilated::overWidthError("reset");}
}
#endif  // VL_DEBUG
