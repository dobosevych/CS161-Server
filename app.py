from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "Ho-ho!"
    
>>>>>>> 459ee87cab359353d767eca9c25c5ab2f6e81b9c
if __name__ == '__main__':
    app.run()

