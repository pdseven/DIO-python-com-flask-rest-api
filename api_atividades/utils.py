from models import Pessoas, Usuarios


# insere dados
def insere_pessoas():
    pessoa = Pessoas(nome='Galleani', idade=25)
    print(pessoa)
    pessoa.save()


# consulta
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    print(pessoa.idade)


# altera
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Galleani').first()
    pessoa.nome = 'Felipe'
    pessoa.save()


# exclui
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    # insere_pessoas()
    # consulta_pessoas()
    # altera_pessoa()
    # exclui_pessoa()
    # consulta_pessoas()
    insere_usuario('rafael', '1234')
    insere_usuario('galleani', '4321')
    consulta_todos_usuarios()