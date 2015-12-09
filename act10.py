from collections import OrderedDict
import sys
import turtle
def main():
  args = sys.argv[1:]
  if not args:
    print 'usage: \'sort\' [1]Sort by Key with lambda [2]Sort by value with lambda [3]Sort by key with fn [4]Sort by value with fn '
    print '\'turtle\''
    print '\'calc\' [number] [operation(+ - * /)] [number]'
    sys.exit(1)

 
  if args[0] == 'sort':
    lamb(args[1])
  elif args[0] =='turtle':
      squirtle()
  elif args[0]=='calc':
      calc(args[1],args[2],args[3])
  else:
       print 'Invalid Input'
       print 'usage: \'sort\' [1]Sort by Key with lambda [2]Sort by value with lambda [3]Sort by key with fn [4]Sort by value with fn '
       print '\'turtle\''
       print '\'calc\' [number] [operation(+ - * /)] [number]'
       sys.exit(1)
def lamb(inp):
    people ={'Shepard':30,'Tali\'Zorah vas Normandy':22,'Liara T\'soni':118,'Kaidan Alenko':25,'Ashley Williams':24,'Jeff Moreau':23,'Kenneth Donnelly':23,'Armando-Owen Bailey':34,'Kelly Chambers':23,'Miranda Lawson':23,'Jack':27,'Mordin Solus':25,'Samara':400,'Grunt':2,'Wreax':30,'Thane Krios':39,'Zaeed Massani':60,'Kasumi Goto':25,'James Vega':29,'Javik':50000,'Legion':34,'EDI':5,'Garrus Vakarian':33,'Jacob Taylor':29,'Steven Hackett':67,'David Anderson':57}
    b={}
    a= inp
    if a=='1':
        b = OrderedDict(sorted(people.items(), key = lambda t:t[0],reverse = True))
    elif a=='2':
        b= OrderedDict(sorted(people.items(), key = lambda t:t[1],reverse = True))
    elif a=='3':
        b= OrderedDict(sorted(people.items(), key = byKeys,reverse = True))
    elif a=='4':
        b= OrderedDict(sorted(people.items(), key = byVal,reverse = True))
    for person in b:
        print(person+': '+str(b[person]))
def byKeys(key):
    return key[0]
def byVal(value):
    return value[1]
def squirtle():
    turtle.penup()
    turtle.left(90)
    turtle.forward(100)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(100)
    turtle.backward(50)
    turtle.left(90)
    turtle.forward(150)
    turtle.exitonclick()
def calc(num1,op,num2):
    ans=0
    if op=='+':
        ans=add(num1,num2)
    elif op=='-':
        ans=minus(num1,num2)
    elif op=='*':
        ans=multiply(num1,num2)
    elif op==r"/":
        ans=divide(num1,num2)

    print str(num1)+" "+op+" "+str(num2)+' = '+str(ans)
    
def add(num1,num2):
    return int(num1)+int(num2)
def minus(num1,num2):
    return int(num1)-int(num2)
def divide(num1,num2):
    return int(num1)/int(num2)
def multiply(num1,num2):
    return int(num1)*int(num2)







if __name__ == '__main__':
  main()

