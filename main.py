from app import app
from classifier.classifier import predict_iris_type
from static.iris_types.iris_description import give_description
from flask import render_template, request, url_for


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        s_len = request.form['sepal_length']
        s_wid = request.form['sepal_width']
        p_len = request.form['petal_length']
        p_wid = request.form['petal_width']

        predicted_type = predict_iris_type(s_len, s_wid, p_len, p_wid)

        iris_image = url_for('static', filename=f'iris_types/{predicted_type}.jpg')
        iris_type = predicted_type.replace('-', ' ')
        iris_description = give_description(predicted_type)

        return render_template('iris_type.html', iris_image=iris_image,
                               iris_type=iris_type, iris_description=iris_description)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
