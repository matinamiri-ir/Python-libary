import sys

print('sys version->',sys.version)


print('Command line args: ',sys.argv)


print('os platform: ',sys.platform)

x = 432470137418741373
print('the Memory size of an object (in Bytes): ',sys.getsizeof(x))


##########################################################################
## Sys Path
# use append(path)


with open('log.txt','w') as file:
    sys.stdout = file
    for i in range(29):
        print(f'the line number {i}')
        
    sys.stdout = sys.__stdout__
    
print('the log finished')


## stdin

# text = sys.stdin.readlines()
# print('text',text)

import time

for i in range(5):
    print(f"Processing step {i + 1}", flush=True)
    time.sleep(1)
    


print("Hello", end="", flush=True )

# time.sleep(5)

print(" Python")

from itertools import cycle

for i in cycle('!@#$'):
    sys.stdout.write(f'matin_loading {i}\r')
    sys.stdout.flush()
    time.sleep(0.4)