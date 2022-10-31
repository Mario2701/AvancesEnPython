from flask import Flask,jsonify,request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ofertas_laborales'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/oferta')
def getOfertas():
    
    cursor = mysql.connection.cursor() #estableces la conexion con la base de datos
    cursor.execute('select * from oferta') #ejecuta el siguiente comando MySQL
    data = cursor.fetchall() #Capta todo el conjunto de datos
    print(data)
    cursor.close()
    
    context = {
        'status':True,
        'content':data
    }
    
    return jsonify(context)
    
    
@app.route('/')
def index():
    context = {
        'content':'bienvenido a mi api con flask y mysql'
    }
    return jsonify(context)

app.run(debug=True)