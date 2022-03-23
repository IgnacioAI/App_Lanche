from flask import render_template, request
from aplication import app, db
from aplication.models.tables import Cliente
from aplication.models.tables import Produto


@app.route('/')
@app.route('/index')
@app.route('/listagem')
def listagem():
    clientes = Cliente.query.all()
    return render_template('listagem.html', clientes=clientes, ordem='id')


@app.route('/selecao/<int:id>')
def selecao(id=0):
    '''definindo as rotas para SELEÇÃO'''
    cliente = Cliente.query.filter_by(id=id).all()
    return render_template('listagem.html', clientes=cliente, ordem='id')


@app.route('/order/<campo>/<ordem_anterior>')
def order(campo='id', ordem_anterior=''):
    '''definindo as rotas para ORDENAÇÃO DE REGISTRO'''
    if campo == 'id':
        if ordem_anterior == campo:
            clientes = Cliente.query.order_by(Cliente.id.desc()).all()
        else:
            clientes = Cliente.query.order_by(Cliente.id).all()
    elif campo == 'nome':
        if ordem_anterior == campo:
            clientes = Cliente.query.order_by(Cliente.nome.desc()).all()
        else:
            clientes = Cliente.query.order_by(Cliente.nome).all()
    elif campo == 'phone':
        if ordem_anterior == campo:
            clientes = Cliente.query.order_by(Cliente.salario.desc()).all()
        else:
            clientes = Cliente.query.order_by(Cliente.salario).all()
    else:
        clientes = Cliente.query.order_by(Cliente.id).all()
    return render_template('listagem.html', clientes=clientes, ordem=campo)


@app.route('/consulta', methods=['POST'])
def consulta():
    '''definindo as rotas para CONSULTA DE REGISTRO'''
    consulta = '%' + request.form.get('consulta') + '%'
    campo = request.form.get('campo')

    if campo == 'nome':
        clientes = Cliente.query.filter(Cliente.nome.like(consulta)).all()
    elif campo == 'sexo':
        clientes = Cliente.query.filter(Cliente.phone.like(consulta)).all()
    else:
        clientes = Cliente.query.all()

    return render_template('listagem.html', clientes=clientes, ordem='id')


@app.route('/insert')
def insert():
    '''definindo as rotas para INSERÇÃO DE REGISTRO'''
    return render_template('insert.html')


@app.route('/save_insert', methods=['POST'])
def save_insert():
    Nome = request.form.get('nome')
    Phone = float(request.form.get('phone'))

    cliente = Cliente(Nome, Phone)

    db.session.add(cliente)
    db.session.commit()

    clientes = Cliente.query.all()
    return render_template('listagem.html', clientes=clientes, ordem='id')


@app.route('/edit/<int:id>')
def edit(id=0):
    '''definindo as rotas para EDIÇÃO de REGISTRO'''
    cliente = Cliente.query.filter_by(id=id).first()
    return render_template('edit.html', cliente=cliente)


@app.route('/save_edit', methods=['POST'])
def save_edit():
    Id = int(request.form.get('id'))
    Nome = request.form.get('nome')
    Phone = float(request.form.get('phone'))

    cliente = Cliente.query.filter_by(id=id).first()

    cliente.nome = Nome
    cliente.phone = Phone

    db.session.commit()

    clientes = Cliente.query.all()
    return render_template('listagem.html', clientes=clientes, ordem='id')


@app.route('/delete/<int:id>')
def delete(id=0):
    '''definindo as rotas para DELEÇÃO DE REGISTROS'''
    cliente = Cliente.query.filter_by(id=id).first()
    return render_template('delete.html', cliente=cliente)


@app.route('/save_edit1', methods=['POST'])
def save_edit1():
    cliente = Cliente.query.filter_by(id=id).first()

    db.session.delete(cliente)
    db.session.commit()

    clientes = Cliente.query.all()
    return render_template('listagem.html', clientes=clientes, ordem='id')





