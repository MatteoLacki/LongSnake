from pony.orm import *
import json


db = Database()


class SnakemakePath(db.Entity):
    id = PrimaryKey(int, unsigned=True, auto=True)
    config = Required(Json)


db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


@db_session
def add_config(c):

    query = select(sp for sp in SnakemakePath)

    for x in query:
        if x.config == c:
            return x.id

    sp = SnakemakePath(config=c)
    commit()    # commit here to be able to acces the id in the next step
    print(sp.id)
    return sp.id
