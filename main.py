from app import app
from flask import render_template, request, redirect


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
