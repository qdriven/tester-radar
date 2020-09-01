from tokenize import String

from sqlalchemy import Column, Integer, ARRAY

from backups.app.crud.base_class import Base


class GithubRepo(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    stars = Column(Integer)
    url = Column(String)
    ## TODO: unstand array type and json
    labels=Column(ARRAY)
