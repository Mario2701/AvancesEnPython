from flask import Flask,request

app = Flask(__name__) #se crea una varible global que es el nombre de la aplicacion

@app.route('/')
def index():
    return '<center><h1>BIENVENIDO A MI SERVIDOR WEB CON FLASK</h1></center>'

@app.route('/saludo')
def mostrarSaludo():
    nombre = request.args.get('nombre','no hay nombre')
    return '<b>Hola {}</b>'.format(nombre)

@app.route('/suma')
def suma():
    n1 = request.args.get('n1','0')
    n2 = request.args.get('n2','0')
    resultado = int(n1) + int(n2)
    return 'La suma de {} + {} es {}'.format(n1,n2,resultado)

@app.route('/operaciones')
def operator():
    n1 = request.args.get('n1','0')
    n2 = request.args.get('n2','0')
    ope = request.args.get('ope','0')
    op = ''

    if(ope == 'suma'): 
        resultado = int(n1) + int(n2)
        op = '+'
    elif(ope == 'resta'): 
        resultado = int(n1) - int(n2)
        op = '-'
    elif(ope == 'multiplicacion'): 
        resultado = int(n1) * int(n2)
        op = '*'
    elif(ope == 'division'): 
        resultado = int(n1) / int(n2)
        op = '/'
    else:
        resultado = ''
    
    if(resultado != ''):
        return 'La {} de {} {} {} es {}'.format(ope,n1,op,n2,resultado)
    else:
        return 'No se ha ingresado el operador'
    
@app.route('/resta/<int:n1>/<int:n2>')
def resta(n1=0,n2=0):
    resultado = n1 - n2
    return '<center>la resta de {} - {} es {}'.format(n1,n2,resultado)


app.run(debug=True)
# debug=True : indica que esta en modo de prueba para no tener que estar cerrando y abriendo el programa
# pip freeze > requirements.txt
