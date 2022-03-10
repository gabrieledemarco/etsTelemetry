from datetime import datetime
import config_postgress_alchemy as cfa
from sqlalchemy import PrimaryKeyConstraint
# from sqlalchemy_utils import database_exists, create_database
# from config_postgres_alchemy import postgres_sql as settings
from sqlalchemy import Table, Column, Integer, String, Float, TIMESTAMP, MetaData, Boolean, Identity, BigInteger
from sqlalchemy import create_engine

url = f"postgresql://{cfa.user}:{cfa.password}@{cfa.host}:{cfa.port}" \
      f"/{cfa.db}"

engine_fin = create_engine(url, pool_size=5, echo=False)

meta = MetaData()
start_time = datetime.now()

user = Table('users', meta,
             Column('id_user', Integer, Identity("always"), nullable=False, primary_key=True),
             Column('nickname', String(50), nullable=False),
             Column('pass_word', String(50), nullable=False),
             Column('telemetry_url', String, nullable= False),
             PrimaryKeyConstraint('id_user', name='id_user_pk'))

meta.create_all(engine_fin)
