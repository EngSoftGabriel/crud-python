from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Criando o motor do banco de dados
engine = create_engine('sqlite:///contatos.db')

# Criando a base para as classes de modelo
Base = declarative_base()

# Definindo a classe de modelo para a tabela 'contatos'
class Contato(Base):
    __tablename__ = 'contatos'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    telefone = Column(String)

# Criando as tabelas no banco de dados
Base.metadata.create_all(engine)

# Criando uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Funções CRUD

def criar_contato(nome, telefone):
    novo_contato = Contato(nome=nome, telefone=telefone)
    session.add(novo_contato)
    session.commit()

def ler_contatos():
    contatos = session.query(Contato).all()
    for contato in contatos:
        print(f"ID: {contato.id}, Nome: {contato.nome}, Telefone: {contato.telefone}")

def atualizar_contato(id, novo_nome, novo_telefone):
    contato = session.query(Contato).filter_by(id=id).first()
    contato.nome = novo_nome
    contato.telefone = novo_telefone
    session.commit()

def deletar_contato(id):
    contato = session.query(Contato).filter_by(id=id).first()
    session.delete(contato)
    session.commit()

# Exemplo de uso
criar_contato("Gabriel Silva", "123456789")
criar_contato("Thais Santos", "987654321")
ler_contatos()
atualizar_contato(1, "Josué Demetrio", "987654321")
ler_contatos()
deletar_contato(1)
ler_contatos()

session.close()