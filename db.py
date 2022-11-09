import sqlalchemy
import databases

metadata = sqlalchemy.MetaData()
database = databases.Database("sqlite:///sqlite_meme.db")
engine = sqlalchemy.create_engine("sqlite:///sqlite_meme.db")
