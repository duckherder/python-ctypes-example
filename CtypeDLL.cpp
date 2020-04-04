///////////////////////////////////////////////////////////////////////////////
//!
//! \file
//! \brief  Ctype DLL interface implementation
//!
///////////////////////////////////////////////////////////////////////////////

#include "CtypeDLL.h"
#include <iostream>

//////////////////////////////////////////////////////////////////////////////!
//!
//! \brief  Sum a series of integers
//!
//! \param  data			Data to sum
//! \param  length          Number of integers
//!
//! \return Sum of integers
//!
//////////////////////////////////////////////////////////////////////////////!
int SumIntegers( int* data, int length )
{
	int sum = 0;
	for ( int i = 0; i < length; i++ )
		sum += data[ i ];

	return sum;
}

//////////////////////////////////////////////////////////////////////////////!
//!
//! \brief  Add two complex numbers
//!
//! \param  a				Complex number a
//! \param  b				Complex number b
//!
//! \return Complex number
//!
//////////////////////////////////////////////////////////////////////////////!
Complex AddComplexNumbers(Complex* a, Complex* b)
{
	Complex result;
	result.re = a->re + b->re;
	result.im = a->im + b->im;
	return result;
}

//////////////////////////////////////////////////////////////////////////////!
//!
//! \brief  Compute length of string
//!
//! \param  string				String
//! \param  length				Length to return
//!
//! \return Complex number
//!
//////////////////////////////////////////////////////////////////////////////!
int StringLength(char* string, void* length)
{
	std::cout << "Inside DLL and string is " << string << std::endl;
	int stringLength = static_cast< int >( std::strlen( string ) );
	if ( length )
	{
		int* result = reinterpret_cast< int * >( length );
		*result = stringLength;
	}
	return stringLength;
}