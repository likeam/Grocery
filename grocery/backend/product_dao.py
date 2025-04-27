
from sql_connection import get_sql_connection

def get_all_products(connection):

  

    cursor = connection.cursor()

    query = ("select products.prodcuct_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name from products inner join uom on products.uom_id = uom.uom_id")

    cursor.execute(query)

    response =[]

    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
          'product_id': product_id, 
          'name': name, 
          'uom_id': uom_id, 
          'price_per_unit': price_per_unit, 
          'uom_name': uom_name      
        })
        
    return response
def insert_new_product(connection, product):
    cursor = connection.cursor()

    query = ('insert into products (name, uom_id, price_per_unit) VALUES (%S %s %s)')
    data =(product['prodcut_name'], product['uom_id'], product[ 'price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowind

def delete_product(connection, product_id):
    cursor = connection.cursor()

    query = ('DELETE FROM products where product_id=' + str(product_id))
   
    cursor.execute(query)
    connection.commit()
    return cursor.lastrowind


if __name__=='__main__':
    connection = get_sql_connection()
    insert_new_product(connection, {
        'prodcut_name': 'carret',
        'uom_id': '1',
        'price_per_unit': '120'
    })
