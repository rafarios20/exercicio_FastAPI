from sqlalchemy import (create_engine, MetaData, Column, Table, Integer, String)

engine = create_engine('sqlite:///teste.db', echo=False)

metadata = MetaData(bind=engine)

user_table = Table('produtos', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('Produto', String(20), index=True),
                   Column('Preço', Integer, nullable=False),
                   Column('Quantidade', Integer, nullable=False))

metadata.create_all()