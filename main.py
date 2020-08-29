from app import app
from classifier.classifier import predict_iris_type
from flask import render_template, request, redirect


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        s_len = request.form['sepal_length']
        s_wid = request.form['sepal_width']
        p_len = request.form['petal_length']
        p_wid = request.form['petal_width']

        predicted_type = predict_iris_type(s_len, s_wid, p_len, p_wid)
        return f'<h1>{predicted_type}</h1>'
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
