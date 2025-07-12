from colorama import init as colorama_init
from colorama import just_fix_windows_console

colorama_init()
just_fix_windows_console()

print('\033[?1049l')  # Return to main buffer
