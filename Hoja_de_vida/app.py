from flask import Flask, render_template, request

app = Flask(__name__)

# Página principal
@app.route('/')
def principal():
    return render_template('info_p.html')

@app.route('/conta')
def conta():
    return render_template('contacto.html')

@app.route('/ob')
def obje():
    return render_template('obje.html')

@app.route('/info_f')
def info_estu():
    return render_template('info_f.html')

if __name__ == '__main__':
    app.run(debug=True)