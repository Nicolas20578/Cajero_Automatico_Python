'''
Realizar un cajero automatico que tenga un menu:
1. Consignar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Consultar dinero disponible
4. Salir
'''

saldo = 1000

print("\t..:MENU:..")
print("1. Consignar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Consultar dinero disponible")
print("4. Salir")
opcion = int(input("Digite una opcion de menu: "))

print()

if opcion==1 :
    extra = float(input("Cuanto dinero desea consignar -> "))
    saldo =+ extra
    print(f"Dinero en la cuenta: {saldo}")
elif opcion==2:
    retirar = float(input("Cuanto dinero desea retirar -> "))
    if retirar>saldo:
        print("No tiene esa cantidad de dinero")
    else:
        saldo -= retirar
        print(f"Dinero en la cuenta: {saldo}")
elif opcion==3:
    print(f"Dinero en la cuenta: {saldo}")
elif opcion==4: 
    print("Gracias por utilizar el cajero automatico")
else:
    print("Se, equivoco de opcion de menu")