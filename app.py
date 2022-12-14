def add(a , b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer))

def sub(a,b):
    answer = a - b
    print(str(a) + "-" + str(b) + "=" + str(answer))

def mul(a,b):
    answer = a+b
    print(str(a) + "*" str(b) + "=" + str(answer))

def div(a,b):
    answer = a+b
    print(str(a) + "/" + str(b) + "=" + str(answer))            


print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Divsion")
print("E. Exit")

if choice == "a" or "A":
    print("Addition")
    a = int(input("Add first number: "))
    b = int(input("Add second number: "))
    add(a , b)