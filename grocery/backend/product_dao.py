import mysql.connector

cnx = mysql.connector.connect(user='root', password='rossi202', host='127.0.0.1', database='grocery')

cursor = cnx.cursor()

query = "SELECT * FROM grocery.products;"

cursor.execute(query)

for (product_id, name, uom_id, price_per_unit) in cursor:
    print(product_id, name, uom_id, price_per_unit)
    pass


cnx.close()
