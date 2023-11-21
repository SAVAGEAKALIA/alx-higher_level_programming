#!/usr/bin/python3

import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info
