from core import user_table, engine

connect = engine.connect()

insert = user_table.insert()

new_product = insert.values(Produto='Agasalho',
                           Preço='200',
                           Quantidade='10')

connect.execute(new_product)

# connect.execute(user_table.insert(), [
#     {'Produto': 'Camisa','Preço': '40', 'Quantidade': '25'},
#     {'Produto': 'Calça','Preço': '70', 'Quantidade': '30'},
#     {'Produto': 'Perfume','Preço': '200', 'Quantidade': '10'},
# ])