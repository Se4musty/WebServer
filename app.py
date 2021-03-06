from flask import Flask, render_template
from data import Articles

app = Flask(__name__)  # where __name__ is a placeholder for the module name

Articles = Articles()

@app.route('/')
def index():
    return render_template('home.html')  # renders the template home.html


@app.route('/about')
def about():
    return render_template('about.html')  # renders about.html


@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)


@app.route('/article/<string:id>/')
def article(id): # Used later in a query to mySQL Database
    return render_template('article.html', id=id)


if __name__ == '__main__':
    app.run(debug=True)  # Starts application
