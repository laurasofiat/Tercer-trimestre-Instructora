from flask import Flask, render_template, request

app = Flask(__name__)

# Página principal
@app.route('/')
def principal():
    return render_template('index.html')

#Carrito
@app.route('/carrito')
def carrito():
    return render_template('carrito.html')

#Contactanos
@app.route('/contactanos')
def contac():
    return render_template('contactanos.html')

#Donde
@app.route('/donde')
def donde():
    return render_template('donde.html')

#Historia
@app.route('/historia')
def histo():
    return render_template('historia.html')

#Mapa
@app.route('/mapa')
def mapa():
    return render_template('mapa.html')

#Nuestros
@app.route('/nuestros')
def nuestros():
    return render_template('nuestros.html')


#Pro
@app.route('/pro')
def pro():
    return render_template('pro.html')


#Quienes
@app.route('/quienes')
def quienes():
    return render_template('quienes.html')


#Redes
@app.route('/redes')
def redes():
    return render_template('redes.html')


#Servicios
@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

if __name__ == '__main__':
    app.run(debug=True)
