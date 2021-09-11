"""
This is the LifeStore_SalesList data:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]

Some new useful lists:

cantidad_ventas = [id_product, total_ventas]

"""



from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches


cantidad_ventas=[]

for producto in lifestore_products:
  contador=0
  for venta in lifestore_sales:
    if producto[0]== venta[1]:
      contador += 1
  cantidad_ventas.append([producto[0], contador])



mas_vendidos = []
