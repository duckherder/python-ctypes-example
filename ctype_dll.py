import ctypes
from ctypes import *
import win32api
import win32con

CTYPEDLL_DLL = r'x64\Release\CtypeDLL.dll'

class Complex(ctypes.Structure):
    # use the fields attribute from Structure to define your structure types
    _fields_ = [("re", ctypes.c_int),
                ("im", ctypes.c_int)]

class Calculator:
    """uses CtypeDLL.dll interface to do various calculations"""

    def __init__(self):
        """initialise DLL interface and create necessary functions"""
        dll_handle = win32api.LoadLibraryEx(CTYPEDLL_DLL, 0, win32con.LOAD_WITH_ALTERED_SEARCH_PATH)
        ctype_dll = ctypes.WinDLL(CTYPEDLL_DLL, handle=dll_handle)

        # lightweight method one using a function pointer from DLL object attributes
        self.accumulate_fn_method1 = ctype_dll.SumIntegers
        self.accumulate_fn_method1.restype = ctypes.c_int
        self.accumulate_fn_method1.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
        print("method 1:", self.accumulate_fn_method1)

        # method 2 using create function by prototype - our DLL uses /Gd (__cdecl calling convention)
        _accumulate_fn_proto = ctypes.CFUNCTYPE(
            ctypes.c_int,                           # return type
            ctypes.POINTER(ctypes.c_int),           # pointer to an array of integers
            ctypes.c_int)                           # length of array
        self.accumulate_fn_method2 = _accumulate_fn_proto(("SumIntegers", ctype_dll),)
        print("method 2: ", self.accumulate_fn_method2)

        # method 3 using create function by prototype with named parameters and default values
        _accumulate_fn_flags = (1, "data", None), (1, "length", 0),         # 1 specifies this is an input
        self.accumulate_fn_method3 = _accumulate_fn_proto(("SumIntegers", ctype_dll), _accumulate_fn_flags)
        print("method 3: ", self.accumulate_fn_method3)

        # create a function for adding to complex numbers using structures
        self.complex_add_fn = ctype_dll.AddComplexNumbers
        self.complex_add_fn.restype = Complex
        self.complex_add_fn.argtypes = [ctypes.POINTER(Complex), ctypes.POINTER(Complex)]

        # create a function for computing string length
        self.string_length_fn = ctype_dll.StringLength
        self.string_length_fn.restype = int
        self.string_length_fn.argtypes = [ctypes.c_char_p, ctypes.c_void_p]

    def sum_integers(self, integers):
        """sum a python list using ctypes DLL"""
        # convert list to a ctypes array
        print("sum of input list: ", sum(integers))
        _array = (ctypes.c_int * len(integers))(*integers)
        # derive a C-types pointer and ctype data length
        _ptr = ctypes.cast(_array, ctypes.POINTER(ctypes.c_int))
        _length = ctypes.c_int(len(integers))

        _result = self.accumulate_fn_method1(_ptr, _length)
        print("result type: ", type(_result))
        print("sum returned from DLL using method 1:", _result)

        _result = self.accumulate_fn_method2(_ptr, _length)
        print("sum returned from DLL using method 2 using pointer:", _result)
        _result = self.accumulate_fn_method2(_array, _length)   # doesn't require creation of pointer object
        print("sum returned from DLL using method 2 by automatic byref:", _result)

        _result = self.accumulate_fn_method3(length=_length, data=_ptr)
        print("sum returned from DLL using method 3 using named parameters:", _result)

    def add_complex_numbers(self, a, b):
        """add two complex numbers together"""
        _a = Complex(a[0], a[1])
        _b = Complex(b[0], b[1])
        _result = self.complex_add_fn(_a, _b)
        print(_result.re, " + ", _result.im, "i")

    def compute_string_length(self, my_string):
        """compute length of string"""
        _length = ctypes.c_int(0)
        _result = self.string_length_fn(ctypes.c_char_p(my_string.encode('utf-8')), ctypes.byref(_length))
        print("string length is ", _length.value)

if __name__ == '__main__':
    _my_calculator = Calculator()
    _integer_list = [4, 7, 1, -4, 3, 9]
    _my_calculator.sum_integers(_integer_list)
    _my_calculator.add_complex_numbers((3, -1), (4, 3))
    _my_calculator.compute_string_length("the quick brown fox")
