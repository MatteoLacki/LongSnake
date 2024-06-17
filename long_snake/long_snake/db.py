import json

from pony.orm import *

from .config_parser import hash_dict

db = Database()


# TODO: update
class SnakemakePath(db.Entity):
    id = PrimaryKey(int, unsigned=True, auto=True)
    config = Required(Json)


db.bind(provider="sqlite", filename="database.sqlite", create_db=True)
db.generate_mapping(create_tables=True)


@db_session
def add_config(c: dict):
    # hash_dict(c) # TODO use it .
    query = select(sp for sp in SnakemakePath)

    for x in query:
        if x.config == c:
            return x.id

    sp = SnakemakePath(config=c)
    commit()  # commit here to be able to acces the id in the next step
    print(sp.id)
    return sp.id
