from flask import Flask, render_template, request

app = Flask(__name__)

# Página principal
@app.route('/')
def principal():
    return render_template('index3.html')

# Página 
@app.route('/index4')
def secundaria():
    return render_template('index4.html')

# Página principal
@app.route('/index5')
def Terciaria():
    return render_template('index5.html')

if __name__ == '__main__':
    app.run(debug=True)