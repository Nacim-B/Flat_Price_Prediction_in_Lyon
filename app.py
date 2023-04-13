import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import cgi

form = cgi.FieldStorage()
app = Flask(__name__)
model = pickle.load(open('model.pk', 'rb'))

liste = []

liste = liste.append([form.getvalue('balcony'),
                      form.getvalue('elevator'),
                      form.getvalue('terrace'),
                      form.getvalue('garden'),
                      form.getvalue('garage'),
                      form.getvalue('parking_spot'),
                      form.getvalue('new'),
                      form.getvalue('district'),
                      form.getvalue('rooms'),
                      form.getvalue('floor')])

output = liste

#prediction = model.predict(final_features)


#output = round(prediction[0], 2)
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/')
def hello():
    return render_template('index.html', prediction_text='Estimated price for this Apartment: $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
