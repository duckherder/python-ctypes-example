# python-ctypes-example

Example of the use of Python ctypes. This allows you to call C functions within a Windows
DLL from a Python script.

To run the example simply build the 64-bit Release version of the DLL using Microsoft Visual Studio 2017.
You will then need to install a Python package. You can do this in an Anaconda environment
from a command prompt as such...

```
conda create -n ctypes
conda activate ctypes
conda install pywin32
```

Then simply run ```python ctype_dll.py```.

Tested with
* Python: 3.8.2
* pywin32: 227
* Microsoft Visual Studio 2017 Community: 15.9.19
