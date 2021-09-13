from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

from listas import productos_ventas, mas_vendidos, menos_vendidos



print(menos_vendidos)

print ('Hello, World!')

print ()

lista_permitidos = [['usuario', 'password'],['usuario2', '1234'],['usuario3', '8JDk&3t'],['usuario4', 'password4']]

acceso = False
intentos_fallidos = 0


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

acceso = False
intentos_fallidos = 0

while(acceso == False and intentos_fallidos < 3):
 print('MENÚ DE OPCIONES: ')
 print(' 1 Productos más vendidos.')
 print(' 2 Productos más buscados. ')
 print(' 3 Productos menos vendidos.')
 print(' 4 Productos menos buscados. ')
 print(' 0 Salir')
 
 seleccion = input('Elija una opción del menú ingresando el número correspondiente: ')
 if (seleccion == '0' or seleccion == '1' or seleccion == '2'or seleccion == '3' or seleccion == '4'):
   acceso = True 
   
 else:
   print ('Opcion inexistente.')
   intentos_fallidos += 1
   if intentos_fallidos < 3:
     print('Intente de nuevo.')

if acceso:
  print('Usted seleccionó la opción: ' + seleccion)

if intentos_fallidos == 3:
  print ('Demasiados intentos fallidos. Acceso no permitido.')
  
if (seleccion == '0'):
  print ('La sesión ha terminado.' )

