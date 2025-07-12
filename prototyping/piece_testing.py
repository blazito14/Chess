from colorama import init as colorama_init
from colorama import just_fix_windows_console
from termcolor import colored

for code in range(0x1FA00, 0x1FA6E):  # 0x265A is exclusive
    print(chr(code), f"U+{code:04X}")

for code in range(0x2654, 0x265A):  # 0x265A is exclusive
    print(chr(code), f"U+{code:04X}")
