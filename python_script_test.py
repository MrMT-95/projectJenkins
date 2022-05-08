import platform
import sys

python_version = sys.version
windows_bit_version = platform.architecture()[0]

print(python_version)
print(windows_bit_version)