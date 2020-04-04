///////////////////////////////////////////////////////////////////////////////
//!
//! \file
//! \brief  Ctype DLL interface
//!
///////////////////////////////////////////////////////////////////////////////

#pragma once
struct Complex
{
	int	re;
	int im;
};

extern "C" __declspec( dllexport ) int SumIntegers( int* data, int length );
extern "C" __declspec(dllexport) Complex AddComplexNumbers(Complex* a, Complex* b);
extern "C" __declspec(dllexport) int StringLength(char* string, void* length);
