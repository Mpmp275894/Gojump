from flask import Flask, render_template
 
app = Flask(__name__)

if __name__ == '_app__':
    app,run(debug=True)
    
@app.route('/')
def home():
    return "Hello, world!"

@app.route('/about')
def about():
    return "To jest strona 'O nas'."

if __name__ == '__main__':
    app.run(debug=True)


 
   