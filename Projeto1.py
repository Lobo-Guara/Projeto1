# Bibliotecas para a pagina
from bottle import jinja2_view, route, run, request, template, response, get, post

#Biblioteca para sqlite
import sqlite3


#VAriaveis usada na pagina
host = 'localhost'
port = '8080'



with sqlite3.connect("BDUsuarios.db") as db:
    cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Usuarios(
IDUsuario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
Nome VARCHAR(20) NOT NULL,
Username VARCHAR(20) NOT NULL,
Password VARCHAR(32) NOT NULL,
Sal VARCHAR(06) NOT NULL)
''')

with sqlite3.connect("BDDispositivos.db") as db:
    cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Dispositivos(
IDDispositivo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
Local VARCHAR(20) NOT NULL,
Tomadas VARCHAR(10) NOT NULL,
Janelas VARCHAR(10) NOT NULL,
Cortinas VARCHAR(10) NOT NULL,
Lampadas VARCHAR(10) NOT NULL,
Sensores VARCHAR(10) NOT NULL)
''')


@route('/')
@jinja2_view('PastaHTML/PaginaHome.html')
def PaginaHome():

    return

@route('/Login')
@jinja2_view('PastaHTML/PaginaLogin.html')
def Usuario_Get():
    return

@route('/Login', method='POST')
@jinja2_view('PastaHTML/PaginaPainelDeControle.html')
def Usuario_Post():
    username = request.forms.get('username')
    password = request.forms.get('password')

    with sqlite3.connect("BDUsuarios.db") as db:
        cursor = db.cursor()
    find_Usuarios = ("SELECT * FROM Usuarios WHERE Username = ? AND Password = ?")
    cursor.execute(find_Usuarios,[(username), (password)])
    Logado = cursor.fetchall()

    if Logado:
        #response.set_cookie("visited", "yes")
        HtmlTabela = True

        return dict(HtmlTabela=HtmlTabela)

    else:
        #request.get_cookie("visited")
        HtmlTabela = False

        return dict(HtmlTabela=HtmlTabela)

@route('/VisaoGeral')
@jinja2_view('PastaHTML/PaginaPainelDeControleVisaoGeral.html')
def VisaoGeralPost():

            Comodo1 = 'Sala'
            Comodo1LampadaEstado = 'Ligada'
            Comodo1TomanadaEstado = 'Ligada'
            Comodo1JanelaEstado = 'Abeta'
            Comodo1CortinaEstado = 'Abeta'
            HtmlTabela = True

            return dict(
            Comodo1=Comodo1,
            HtmlTabela=HtmlTabela,
            Comodo1LampadaEstado=Comodo1LampadaEstado,
            Comodo1TomanadaEstado=Comodo1TomanadaEstado,
            Comodo1JanelaEstado=Comodo1JanelaEstado,
            Comodo1CortinaEstado=Comodo1CortinaEstado)


@route('/Lampadas', method='GET')
@jinja2_view('PastaHTML/PaginaPainelDeControleLampadas.html')

def LampadasPost():

    with sqlite3.connect('BDDispositivos.db') as conn:
    	cursor = conn.cursor()
    cursor.execute("""SELECT Lampadas FROM Dispositivos""")


    op1_checked = request.forms.get('Comodo1LampadaEstadoR')
    for linha in cursor.fetchone():
        SaidaBD = linha
        #print(linha)
        Comodo1LampadaEstado = True
        return dict(
        op1_checked=op1_checked,
        SaidaBD=SaidaBD,
        Comodo1LampadaEstado=Comodo1LampadaEstado)



@route('/Lampadas', method='POST')
@jinja2_view('PastaHTML/PaginaPainelDeControleLampadas.html')

def LampadasGet():

    #MudarLampadas = request.forms.get('MudarLampadas')

    return dict(MudarLampadas=MudarLampadas)

@route('/Tomadas', method='GET')
@jinja2_view('PastaHTML/PaginaPainelDeControleTomadas.html')
def TomadasGet():
	return


@route('/Tomadas', method='POST')
@jinja2_view('PastaHTML/PaginaPainelDeControleTomadas.html')
def TomadasPost():
	return

@route('/Janelas', method='GET')
@jinja2_view('PastaHTML/PaginaPainelDeControleJanelas.html')
def JanelasGet():
	return


@route('/Janelas', method='POST')
@jinja2_view('PastaHTML/PaginaPainelDeControleJanelas.html')
def JanelasPost():
	return


@route('/Cortinas', method='GET')
@jinja2_view('PastaHTML/PaginaPainelDeControleCortinas.html')
def JanelasGet():
	return


@route('/Cortinass', method='POST')
@jinja2_view('PastaHTML/PaginaPainelDeControleCortinas.html')
def JanelasPost():
	return


run(host=host, port=port, debug=True)

