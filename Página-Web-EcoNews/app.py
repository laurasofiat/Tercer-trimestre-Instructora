from flask import Flask, render_template, request

app = Flask(__name__)

# Página principal
@app.route('/')
def principal():
    return render_template('index6.html')

#Adopta
@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

#Contacto
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

#Inscribete
@app.route('/formulario')
def formu():
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)