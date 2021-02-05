

def operatoren(num1,num2):
    op = input ("Bite gewünschte operation eingeben :")
    if op=="+":
        print (num1+num2)
    elif op=="-":
        print (num1-num2)
    elif op=="*":
        print(num1*num2)
    elif op=="/":
        print(num1/num2)
    else:
        print("falsche Eingabe")
        operatoren()

def taschenrechner():
    print("hallo ich bin ein taschenrechner")
    num1 = int (input ("Bitte zahl eins eingeben :"))
    num2 = int (input ("Bitte zahl zwei eingeben :"))
    operatoren(num1,num2)

taschenrechner()
