from sqlalchemy import delete
from core import user_table, engine

connect = engine.connect()

delete = delete(user_table).where(user_table.c.Produto == 'Agasalho')

result = connect.execute(delete)

print(result.rowcount)