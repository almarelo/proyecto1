"""
This is the LifeStore_SalesList data:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]

Se creó la nueva lista productos_ventas, la cual por cada producto, registra cantidad de ventas, cantidad de devoluciones, puntuación promedio, si tiene o no puntuación y el número de búsquedas.

productos_ventas = [producto[], ventas, refunds, ventas- refunds, score_promedio, puntuado, searches]

"""


from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches 
'se importan las listas originales con los datos de la empresa'

from operator import itemgetter, attrgetter
'se importan estos operadores para poder ordenas listas respecto a un índice particular'


productos_ventas=[]
'variable para almacenar la lista de productos'

for producto in lifestore_products:
  'se va a crear un elemento por cada producto existente en la tienda y cada uno tendrá asignados los siguientes parámetros'
  sales=0
  refunds =0
  suma_scores = 0
  searches = 0
  
  for venta in lifestore_sales:
    'ciclo para contar el número de ventas y el número de devoluciones con los datos de la lista lifestore_sales'
    if producto[0]== venta[1]:
      sales += 1
      refunds += venta[4]
      suma_scores += venta[2]
  if (sales == 0): 
    'en caso de no tener ventas, no tendrá puntuación'
    puntuado = 0
    score_promedio = 'N/A'  
  else:  
    'en caso de tener ventas, se almacena la puntuación promedio de todas las ventas'
    puntuado = 1
    score_promedio = suma_scores/sales
  for search in lifestore_searches:
    if producto[0] == search[1]:
      searches += 1
  
  'se almacena el elemento con todos sus atributos'
  productos_ventas.append([producto, sales, refunds, sales - refunds, score_promedio, puntuado, searches])


'se almacenan en una nueva lista los 10 más vendidos en orden'
mas_vendidos = sorted(productos_ventas, key=itemgetter(3), reverse=True)[0:10]

'se almacenan en una nueva lista los 10 menos vendidos en orden'
menos_vendidos = sorted(productos_ventas, key=itemgetter(3))[0:10]

productos_puntuados = []

'para las listas referentes a puntuación, solo se considerarán los productos que sí están puntuados'
for producto in productos_ventas:
  if producto[5]:
    productos_puntuados.append(producto) 

'se almacenan en una nueva lista los 10 mejores puntuados'
mejor_puntuados = sorted(productos_puntuados, key=itemgetter(4), reverse= True)[0:10]

'se almacenan en una nueva lista los 10 peores puntuados'
peor_puntuados = sorted(productos_puntuados, key=itemgetter(4))[0:10]

'se almacenan en una nueva lista los 10 más buscados'
mas_buscados = sorted(productos_ventas, key=itemgetter(6), reverse=True)[0:10]

'se almacenan en una nueva lista los 10 menos buscados'
menos_buscados = sorted(productos_ventas, key=itemgetter(6))[0:10]