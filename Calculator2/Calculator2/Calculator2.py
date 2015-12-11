def add(num1,num2):
   
    return num1+num2
def sub(num1,num2):
    return num1-num2
def div(num1,num2):
    return num1/num2
def mul(num1,num2):
    return num1*num2
def operator(op,num1,num2):
    #if op=='+':
    #    return add(num1,num2)
    #elif op =='-':
    #    return sub(num1,num2)
    #elif op == '*':
    #    return mul(num1,num2)
    #elif op == '/':
    #    return div(num1,num2)
    #else:
    #    return None
    functions = {'+':add,'-':sub,'*':mul,'/':div}
    func = functions.get(op,None)
    if func:
            return func(num1,num2)
    return None

def input1():
    return int(raw_input('Enter a number: '))

def input2():
    return int(raw_input('Enter a number: '))
def inputop(input = raw_input):
    return input('Enter operator: ')

def output(num1,op,num2,ans):
    return "{} {} {} = {}".format(num1,op,num2,ans)

def maine():
    
    num1 = input1()
    op = inputop().strip()
    num2 = input2()
    ans = operator(op,num1,num2)
    print output(num1,op,num2,ans)

if __name__ == "__main__":
    maine()