from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuracion de my  sql 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'final'
mysql = MySQL(app)

# configuraciones 
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM final')
    data = cur.fetchall()
    print (data)
    return render_template('index.html', productos = data)

@app.route('/agregar', methods=['POST'])
def agregar():
    if request.method == 'POST':
        codigo = request.form['codigo']
        nombre = request.form['nombre']
        precio = request.form['precio']
        cantidad = request.form['cantidad']
        cur = MySQL.connection.cursor()
        cur.execute("INSERT INTO agregar (codigo, nombre, precio, cantidad) VALUES (%s, %s, %s, %s)", (codigo, nombre, precio, cantidad))
        MySQL.connection.commit()
        flash('Producto agregado correctamente')
        return redirect(url_for('Index'))

@app.route('/editar7<id>')
def get_productos(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM final WHERE id = %s', (id))
    data = cur.fetchall()
    return render_template('editar.htm', productos = data[0])

@app.route('/actualizar/<id>')
def get_actualizar(id):
    if request.method == 'POST':
        codigo = request.form['codigo']
        nombre = request.form['nombre']
        precio = request.form['precio']
        cantidad = request.form['cantidad']
        cur = mysql.connection.cursor()
        cur.execute("""
            ACTUALIZAR productos 
            SET codigo = %s,
            nombre = %s,
            precio = %s,
            cantiad = %s
            WHERE id = %s""",(codigo, nombre, precio, cantidad, id))
        flash('Producto actualizado correctamente')
        return redirect(url_for('Index'))

@app.route('/borrar/<string:id>')
def borrar():
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM final WHERE id = %s', (id,))
    mysql.connection.commit()
    flash('Producto borrado correctamente')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)


