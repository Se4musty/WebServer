from flask import Flask, render_template

app = Flask(__name__)  # where __name__ is a placeholder for the module name


@app.route('/')
def index():
    return render_template('home.html')  # renders the template indexhtml


if __name__ == '__main__':
    app.run(debug=True)  # Starts application

