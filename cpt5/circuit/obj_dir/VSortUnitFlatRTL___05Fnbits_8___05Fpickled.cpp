// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Model implementation (design independent parts)

#include "VSortUnitFlatRTL___05Fnbits_8___05Fpickled__pch.h"

//============================================================
// Constructors

VSortUnitFlatRTL___05Fnbits_8___05Fpickled::VSortUnitFlatRTL___05Fnbits_8___05Fpickled(VerilatedContext* _vcontextp__, const char* _vcname__)
    : VerilatedModel{*_vcontextp__}
    , vlSymsp{new VSortUnitFlatRTL___05Fnbits_8___05Fpickled__Syms(contextp(), _vcname__, this)}
    , clk{vlSymsp->TOP.clk}
    , in_val{vlSymsp->TOP.in_val}
    , out_val{vlSymsp->TOP.out_val}
    , reset{vlSymsp->TOP.reset}
    , in_{vlSymsp->TOP.in_}
    , out{vlSymsp->TOP.out}
    , rootp{&(vlSymsp->TOP)}
{
    // Register model with the context
    contextp()->addModel(this);
}

VSortUnitFlatRTL___05Fnbits_8___05Fpickled::VSortUnitFlatRTL___05Fnbits_8___05Fpickled(const char* _vcname__)
    : VSortUnitFlatRTL___05Fnbits_8___05Fpickled(Verilated::threadContextp(), _vcname__)
{
}

//============================================================
// Destructor

VSortUnitFlatRTL___05Fnbits_8___05Fpickled::~VSortUnitFlatRTL___05Fnbits_8___05Fpickled() {
    delete vlSymsp;
}

//============================================================
// Evaluation function

#ifdef VL_DEBUG
void VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_debug_assertions(VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root* vlSelf);
#endif  // VL_DEBUG
void VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_static(VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root* vlSelf);
void VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_initial(VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root* vlSelf);
void VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_settle(VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root* vlSelf);
void VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval(VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root* vlSelf);

void VSortUnitFlatRTL___05Fnbits_8___05Fpickled::eval_step() {
    VL_DEBUG_IF(VL_DBG_MSGF("+++++TOP Evaluate VSortUnitFlatRTL___05Fnbits_8___05Fpickled::eval_step\n"); );
#ifdef VL_DEBUG
    // Debug assertions
    VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_debug_assertions(&(vlSymsp->TOP));
#endif  // VL_DEBUG
    vlSymsp->__Vm_deleter.deleteAll();
    if (VL_UNLIKELY(!vlSymsp->__Vm_didInit)) {
        vlSymsp->__Vm_didInit = true;
        VL_DEBUG_IF(VL_DBG_MSGF("+ Initial\n"););
        VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_static(&(vlSymsp->TOP));
        VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_initial(&(vlSymsp->TOP));
        VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_settle(&(vlSymsp->TOP));
    }
    VL_DEBUG_IF(VL_DBG_MSGF("+ Eval\n"););
    VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval(&(vlSymsp->TOP));
    // Evaluate cleanup
    Verilated::endOfEval(vlSymsp->__Vm_evalMsgQp);
}

//============================================================
// Events and timing
bool VSortUnitFlatRTL___05Fnbits_8___05Fpickled::eventsPending() { return false; }

uint64_t VSortUnitFlatRTL___05Fnbits_8___05Fpickled::nextTimeSlot() {
    VL_FATAL_MT(__FILE__, __LINE__, "", "%Error: No delays in the design");
    return 0;
}

//============================================================
// Utilities

const char* VSortUnitFlatRTL___05Fnbits_8___05Fpickled::name() const {
    return vlSymsp->name();
}

//============================================================
// Invoke final blocks

void VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_final(VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root* vlSelf);

VL_ATTR_COLD void VSortUnitFlatRTL___05Fnbits_8___05Fpickled::final() {
    VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root___eval_final(&(vlSymsp->TOP));
}

//============================================================
// Implementations of abstract methods from VerilatedModel

const char* VSortUnitFlatRTL___05Fnbits_8___05Fpickled::hierName() const { return vlSymsp->name(); }
const char* VSortUnitFlatRTL___05Fnbits_8___05Fpickled::modelName() const { return "VSortUnitFlatRTL___05Fnbits_8___05Fpickled"; }
unsigned VSortUnitFlatRTL___05Fnbits_8___05Fpickled::threads() const { return 1; }
void VSortUnitFlatRTL___05Fnbits_8___05Fpickled::prepareClone() const { contextp()->prepareClone(); }
void VSortUnitFlatRTL___05Fnbits_8___05Fpickled::atClone() const {
    contextp()->threadPoolpOnClone();
}
