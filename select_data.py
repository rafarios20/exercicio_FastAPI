from sqlalchemy import select
from core import user_table


select = select([user_table])

for row in select.execute():
    print(row)