
import subprocess
import sys


system = sys.platform

encoding = 'cp850' if system.lower() == 'win32' else 'utf-8'

comandos = [
    [['dir'],['ping', 'localhost']] 
    if system.lower() == 'win32' else 
    [['ls','-lha'],['ping','localhost','-c','4']]
]

proc = subprocess.run(
    comandos[0][0], capture_output=True,
    text=True, encoding=encoding
)

processo = subprocess.run(
    comandos[0][1], capture_output=True,
)

print(proc.stdout)

print(80 * '_')

print(processo.args)
print(processo.stderr)
print(processo.stdout.decode(encoding))
print(processo.returncode)
