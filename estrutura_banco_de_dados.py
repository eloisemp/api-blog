from flask import Flask  # permite criar o api
from flask_sqlalchemy import SQLAlchemy  # permite banco de dados

from urllib.parse import quote

# Criar um API flask
app = Flask(__name__)

# Criar um instância de SQLAlchemy
# acesso de autenticação unico
app.config['SECRET_KEY'] = 'FSD2323f#$!SAH'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db' === mudei para supabase este é o original funcionando
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.sukjxwcevxngxeueechg:' + \
    quote('Q-5@Lv)Wz?nKGcE')+'@aws-0-us-west-1.pooler.supabase.com:5432/postgres'

db = SQLAlchemy(app)
db: SQLAlchemy


class Postagem(db.Model):
    __tablename__ = 'postagem'  # nome da tabela
    # tipo inteiro, valores unicos incrementado de 1 a 1 sem se repetir
    id_postagem = db.Column(db.Integer, primary_key=True)
    # nome da variável é nome da coluna
    titulo = db.Column(db.String)
# autor, relaciona com a tabela autor para saber quem foi o autor daquela postagem
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))


class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')

# Executar  o comando para criar o banco de dados


def inicializar_banco():
    with app.app_context():
        db.drop_all()
        db.create_all()  # cria todas as tabelas anexadas ao db
        # Criar usuários administradores
        autor = Autor(nome='eloise', email='eloisemp@email.com',
                      senha='12345', admin=True)
        db.session.add(autor)
        db.session.commit()


if __name__ == '__main__':
    inicializar_banco()
