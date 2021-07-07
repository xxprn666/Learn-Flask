from services.serve import app

@app.route('/')
def index():
    return 'hellow'


if __name__ == '__main__':
    app.run('0.0.0.0')
