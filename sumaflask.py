from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/calculo', methods=['GET','POST'])
def calculate():
    a = request.form['a']
    b = request.form['b']
    c = float(a) + float(b)
    return render_template('calculo.html', total = c)

if __name__ == '__main__':
    app.run(debug = True, port = 5000)