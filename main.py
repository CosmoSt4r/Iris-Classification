from app import app
from classifier.classifier import predict_iris_type
from flask import render_template, request, redirect


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
