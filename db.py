import sqlalchemy
import databases
import ormar

metadata = sqlalchemy.MetaData()
database = databases.Database("sqlite:///sqlite_meme.db")
engine = sqlalchemy.create_engine("sqlite:///sqlite_meme.db")


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database
