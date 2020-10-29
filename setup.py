import sys
from cx_Freeze import setup, Executable

base=None

if sys.platform=="win32":base="Win32GUI"

exe=Executable(script="main.py",base=base)

setup(
    name="my",
    description="Sample cx_Freeze Tkinter script",
    executables = [exe]
    )