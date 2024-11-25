// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See VSortUnitFlatRTL___05Fnbits_8___05Fpickled.h for the primary calling header

#include "VSortUnitFlatRTL___05Fnbits_8___05Fpickled__pch.h"
#include "VSortUnitFlatRTL___05Fnbits_8___05Fpickled__Syms.h"
#include "VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root.h"

#ifdef VL_DEBUG
VL_ATTR_COLD void VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___dump_triggers__act(VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root* vlSelf);
#endif  // VL_DEBUG

void VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_triggers__act(VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root* vlSelf) {
    (void)vlSelf;  // Prevent unused variable warning
    VSortUnitFlatRTL___05Fnbits_8___05Fpickled__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    VL_DEBUG_IF(VL_DBG_MSGF("+    VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_triggers__act\n"); );
    auto &vlSelfRef = std::ref(*vlSelf).get();
    // Body
#ifdef VL_DEBUG
    if (VL_UNLIKELY(vlSymsp->_vm_contextp__->debug())) {
        VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___dump_triggers__act(vlSelf);
    }
#endif
}
