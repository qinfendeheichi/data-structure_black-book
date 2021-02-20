"""
a super easy version of a calculator
"""


class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()
        
import os
import time
flag=[0,0,0]
number=0
value1=0
value2=''
operand=None
getch = _Getch()
while(1):
    getch = _Getch()
    char=getch.impl().decode('utf-8')
    if char=='o':
        i=os.system("cls")
        continue
    if char in ['+','-','*','/']:
        i=os.system("cls")
        if flag[2]==1:

            if operand=='+':         
                value1=float(value1)+float(value2)
                

            if operand=='-':
                value1=float(value1)-float(value2)
            if operand=='*':
                value1=float(value1)*float(value2)
            if operand=='/':
                value1=float(value1)/float(value2)
            print(value1,char,sep='')
        elif flag[2]==0:
            value1=value2
            print(value1,char,sep='')
        operand=char
        flag[0]=1
        flag[1]=1
        flag[2]=0
        number=0
        value2=''
    
    if char=='=':
        i=os.system("cls")
        print(value1,operand,value2,'= ',end='')
        value1=float(value1)
        if operand=='+':
            result=value1+float(value2)     
        if operand=='-':
            result=value1-float(value2)
        if operand=='*':
            result=value1*float(value2)
        if operand=='/':
            result=value1/float(value2)
        print(result)
        operand='='
        value1=result
        flag[0]=1
        flag[1]=0
        number=0
        value2=''
    # input a number character 
    elif char in [chr(i+48) for i in range(10)]:
        os.system("cls")
        # continue the process of inputing a number
        if number==1:
            value2=value2+char
        elif flag[0]==0:                                  
            value2=value2+char
            flag[0]=1
            number=1
        else:
            value2=value2+char
            flag[2]=1
            number=1
        if operand!=None:
            print(value1,operand,value2,sep='')
        else:
            print(value2,sep=' ')
