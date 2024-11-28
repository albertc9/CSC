// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Symbol table internal header
//
// Internal details; most calling programs do not need this header,
// unless using verilator public meta comments.

#ifndef VERILATED_VSORTUNITFLATRTL___05FNBITS_8___05FPICKLED__SYMS_H_
#define VERILATED_VSORTUNITFLATRTL___05FNBITS_8___05FPICKLED__SYMS_H_  // guard

#include "verilated.h"

// INCLUDE MODEL CLASS

#include "VSortUnitFlatRTL___05Fnbits_8___05Fpickled.h"

// INCLUDE MODULE CLASSES
#include "VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root.h"

// SYMS CLASS (contains all model state)
class alignas(VL_CACHE_LINE_BYTES)VSortUnitFlatRTL___05Fnbits_8___05Fpickled__Syms final : public VerilatedSyms {
  public:
    // INTERNAL STATE
    VSortUnitFlatRTL___05Fnbits_8___05Fpickled* const __Vm_modelp;
    VlDeleter __Vm_deleter;
    bool __Vm_didInit = false;

    // MODULE INSTANCE STATE
    VSortUnitFlatRTL___05Fnbits_8___05Fpickled___024root TOP;

    // CONSTRUCTORS
    VSortUnitFlatRTL___05Fnbits_8___05Fpickled__Syms(VerilatedContext* contextp, const char* namep, VSortUnitFlatRTL___05Fnbits_8___05Fpickled* modelp);
    ~VSortUnitFlatRTL___05Fnbits_8___05Fpickled__Syms();

    // METHODS
    const char* name() { return TOP.name(); }
};

#endif  // guard
