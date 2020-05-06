from sqlalchemy import MetaData, Table, Column, String, Integer

metadata = MetaData()

shorts_table: Table = Table(
    'shorts',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('short', String),
    Column('original', String)
)
