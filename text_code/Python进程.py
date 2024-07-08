import os
import sys
print('Process (%s) start...' % os.getpid())


pid = os.fork()

if pid == 0:
    print('我是子进程：',os.getpid())
else:
    print('我是父进程：',os.getpid())
