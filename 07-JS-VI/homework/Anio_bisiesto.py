'''def año_bisiesto(año):
                 
    if not año.isnumeric():
        print("ingrese un año en formato numerico!!!")
    
    elif int(año)%4 ==0:
        
        if int(año)%100 != 0 or int(año)%400==0:
             print("el año {} es bisiesto".format(año))
        else:
             print("el año {} no es bisiesto".format(año))
    else:
         print("el año {} no es bisiesto".format(año))
       

flag=True   
while flag:
    año=input("ingrese un año o escriba ´salir´ para finalizar\n ")
    if año =="salir":
         flag=False
    else:
        año_bisiesto(año)'''








def ano_hermoso_bisiesto():
    año_ingresado = input("Ingrese el año: ")
    while año_ingresado.isnumeric() == False:
        año_ingresado = input("Usted no a ingresado un año, porfavor ingrese un año: ")
    año_numero = int(año_ingresado)
    if año_numero % 400 == 0:
        print("Es bisiesto tu año!")
    elif año_numero % 100 == 0 or año_numero % 4 != 0:
        print("Tu año no es bisiesto")
    else:
        print("Es bisiesto tu año!")
ano_hermoso_bisiesto()
