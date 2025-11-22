from flask import Flask, render_template, request

app = Flask(__name__)

# Página principal
@app.route('/')
def principal():
    return render_template('index2.html')

#Adopta
@app.route('/adopta')
def adopta():
    return render_template('adopta.html')

#Contacto
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

#Dona
@app.route('/dona')
def dona():
    return render_template('dona.html')

#Acerca
@app.route('/acerca')
def acerca():
    return render_template('Acerca.html')

if __name__ == '__main__':
    app.run(debug=True)
