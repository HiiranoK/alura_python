def foo(valor):
    if valor: #true
        print("Valor é verdadeiro")
    else: #false
        print("Valor é falso")

foo('') #Valor é falso
foo(None) #Valor é falso
print(bool(''))#
print(bool(None))#