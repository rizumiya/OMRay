import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"
executables = [Executable("main.py", base=base)]

setup(
    name = "OMRay",
    version = "1.0",
    description = "Melakukan pengecekan jawaban pada lembar jawab ujian yang tidak berbasis LJK",
    executables = executables
)
   
