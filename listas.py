"""
This is the LifeStore_SalesList data:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]

Some new useful lists:

productos_ventas = [id_product, ventas, refunds, ventas-refunds]

mas_vendidos = [id_product, name, ventas, refunds ]
"""



from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

from operator import itemgetter, attrgetter


productos_ventas=[]

for producto in lifestore_products:
  sales=0
  refunds =0
  for venta in lifestore_sales:
    if producto[0]== venta[1]:
      sales += 1
      refunds += venta[4]
  productos_ventas.append([producto, sales, refunds, sales - refunds])



mas_vendidos = sorted(productos_ventas, key=itemgetter(3), reverse=True)[0:10]

menos_vendidos = sorted(productos_ventas, key=itemgetter(3))[0:10]