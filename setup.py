import cx_Freeze
import sys
import matplotlib

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("Text2Image.py",base=base)]


cx_Freeze.setup(
    name = "SEARCH",
    options = {"build_exe":{"packages":["Tkinter","matplotlib","pytesser"],
                            "excludes":['collections.abc'],
                            "include_files":["a.jpg","b.jpg","c.jpg","f.jpg","g.jpg","d.jpg","e.jpg"]}},
    version = "0.01",
    executables = executables
    )
