from sqlalchemy import Column, Integer, String
from database import Base

class Job(Base):
    __tablename__ = 'job'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100))
    cargo = Column(String(100))
    salario = Column(String(100))
    descricao = Column(String(100))

    def __init__(self, titulo=None, cargo=None, salario=None, descricao=None):
        self.titulo = titulo
        self.cargo = cargo
        self.salario = salario
        self.descricao = descricao

    def __repr__(self):
        return '<User %r>' % (self.titulo)
