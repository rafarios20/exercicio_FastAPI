from sqlalchemy import update
from core import user_table, engine

connect = engine.connect()

update = update(user_table).where(user_table.c.Produto == 'Perfume')

update = update.values(Produto='Agasalho')

result = connect.execute(update)

print(result.rowcount)