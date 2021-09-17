from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
'se importan las listas originales de los datos de la empresa'

from listas import productos_ventas, productos_puntuados, mas_vendidos, menos_vendidos, mejor_puntuados, peor_puntuados, mas_buscados, menos_buscados
'se importan las listas auxiliares que fueron creadas para fines del análisis'


'lista de parejas [usuario, contraseña] que tienen acceso al sistema'
lista_permitidos = [['usuario', 'password'],['usuario2', '1234'],['usuario3', '8JDk&3t'],['usuario4', 'password4']]

'variables auxiliares para determinar cuando puede ingresar el usuario y cuando hizo demasiados intentos'
acceso = False
intentos_fallidos = 0

'este ciclo se repite mientras no se ingresen datos correctos pero no se pase de 3 intentos'
while (acceso == False and intentos_fallidos < 3):

 usuario = input("Ingrese su nombre de usuario: ")
 password = input("Ingrese su contraseña: ")
 for permitido in lista_permitidos:
   if (usuario == permitido[0] and password==permitido[1]):
    acceso = True

 if acceso == False:
   print ('Acceso incorrecto.')
   intentos_fallidos += 1
   if intentos_fallidos < 3:
     print('Intente de nuevo.')

   
if acceso:
  print ('Acceso correcto.')
if intentos_fallidos == 3:
  print ('Demasiados intentos fallidos. Acceso no permitido.')

'variables auxiliares para determinar cuándo se muestra el menú'
salir = False
intentos_fallidos = 0

'este ciclo se repite mientras el usuario no decida salir y no tenga más de 3 intentos fallidos de ingreso'
while(salir == False and intentos_fallidos < 3):
 print('MENÚ DE OPCIONES: ')
 print(' 1 Productos más vendidos.')
 print(' 2 Productos menos vendidos.')
 print(' 3 Productos más buscados.')
 print(' 4 Productos menos buscados.')
 print(' 5 Productos mejor puntuados.')
 print(' 6 Productos peor puntuados.')
 print(' 0 Salir')
 

 'al elegir una opcion del menú se muestran los datos relevantes de la lista elegida y siempre se da la opción de salir o volver al menú'
 seleccion = input('Elija una opción del menú ingresando el número correspondiente: ')
 if seleccion == '0':
   salir = True 
 elif seleccion == '1':
    print('Los productos más vendidos son:')
    for i in range(10):
     print(i+1) 
     print(mas_vendidos[i][0][1])
     print('Ventas: ', mas_vendidos[i][1])
     print('Devoluciones: ', mas_vendidos[i][2])
    salir = (input('Ingresa cualquier número para volver al menú o 0 para salir:  ')== '0') 
    
 elif seleccion == '2':
    print('Los productos menos vendidos son:')
    for i in range(10):
     print(i+1) 
     print(menos_vendidos[i][0][1])
     print('Ventas: ', menos_vendidos[i][1])
     print('Devoluciones: ', menos_vendidos[i][2] )

    salir = (input('Ingresa cualquier número para volver al menú o 0 para salir:  ')== '0') 
 elif seleccion == '3':
    print('Los productos más buscados son:')
    for i in range(10):  
     print(i+1) 
     print(mas_buscados[i][0][1])
     print('Búsquedas: ', mas_buscados[i][6])
     print('Ventas: ', mas_buscados[i][1])
     print('Devoluciones: ', mas_buscados[i][2])
    salir = (input('Ingresa cualquier número para volver al menú o 0 para salir:  ')== '0')  
 elif seleccion == '4':
    print('Los productos menos buscados son:')
    for i in range(10):
     print(i+1) 
     print(menos_buscados[i][0][1])
     print('Búsquedas: ', menos_buscados[i][6])
     print('Ventas: ', menos_buscados[i][1])
     print('Devoluciones: ', menos_buscados[i][2])
    salir = (input('Ingresa cualquier número para volver al menú o 0 para salir:  ')== '0') 
 elif seleccion == '5':
    print('Los productos mejor puntuados son:')
    for i in range(10):
     print(i+1) 
     print(mejor_puntuados[i][0][1])
     print('Puntuación promedio: ', mejor_puntuados[i][4] )
     print('Búsquedas: ', mejor_puntuados[i][6])
     print('Ventas: ', mejor_puntuados[i][1])
     print('Devoluciones: ', mejor_puntuados[i][2])
    salir = (input('Ingresa cualquier número para volver al menú o 0 para salir:  ')== '0')  
 elif seleccion == '6':
    print('Los productos peor puntuados son:')
    for i in range(10):
     print(i+1) 
     print(peor_puntuados[i][0][1])
     print('Puntuación promedio: ', peor_puntuados[i][4] )
     print('Búsquedas: ', peor_puntuados[i][6])
     print('Ventas: ', peor_puntuados[i][1])
     print('Devoluciones: ', peor_puntuados[i][2])
    salir = (input('Ingresa cualquier número para volver al menú o 0 para salir:  ')== '0') 
 else:
   print ('Opcion inexistente.')
   intentos_fallidos += 1
   if intentos_fallidos < 3:
     print('Intente de nuevo.')




if intentos_fallidos == 3:
  print ('Demasiados intentos fallidos. Acceso no permitido.')
  
if (salir):
  print ('La sesión ha terminado.' )

