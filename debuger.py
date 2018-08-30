import pdb
import sys

def add(n1 = 0,n2 = 0):
    return int(n1)+int(n2)
def sub(n1 = 0,n2 = 0):
    return int(n1)-int(n2)

def main():
    print(sys.argv)
    #断点设置,开始调试
    pdb.set_trace()
    
    addition = add(sys.argv[1],sys.argv[2])
    print(addition)
    subtraction=sub(sys.argv[1],sys.argv[2])
    print(subtraction)

main()