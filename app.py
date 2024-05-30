from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/', methods=['post', 'get'])
def form():
    resultMsg = ''
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        resultMsg = checkLoginAndPassword(login,password)
    return render_template('index.html', result= resultMsg)


if __name__ == '__main__':
    app.run()

def checkLoginAndPassword(login,password):
    f = open('logpin.txt', 'rt', newline='')
    loginFromFile = f.readline().strip()
    passwordFromFile = f.readline().strip()
    f.close()
    loginFromUser = "".join([c for c in login.strip() if c.isprintable()])
    passwordFromUser = "".join([c for c in password.strip() if c.isprintable()])
    if (loginFromUser != '' and passwordFromUser != '' and loginFromUser == loginFromFile and passwordFromUser == passwordFromFile):
        return  'Верно'
    else:
        return 'Неверно'


