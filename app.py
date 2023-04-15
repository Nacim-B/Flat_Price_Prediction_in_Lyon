import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    #int_features = [int(x) for x in request.form.values()]
    #final_features = np.array(int_features)
    #final_features = np.append(final_features, [0]*51)
    #final_features = np.reshape(final_features, (1, -1))

    list_features = []

    list_features = np.append(list_features, request.form.get('area'))
    list_features = np.append(list_features, request.form.get('balcony'))
    list_features = np.append(list_features, request.form.get('elevator'))
    list_features = np.append(list_features, request.form.get('terrace'))
    list_features = np.append(list_features, request.form.get('garden'))
    list_features = np.append(list_features, request.form.get('garage'))
    list_features = np.append(list_features, request.form.get('parking_spot'))
    list_features = np.append(list_features, request.form.get('new'))

    list_district = [0] * 34

    district_number = int(request.form.get('district'))

    list_district[district_number] = 1
    list_features = np.append(list_features, list_district)

    list_rooms = [0] * 11
    rooms_number = int(request.form.get('rooms'))
    list_rooms[rooms_number] = 1
    list_features = np.append(list_features, list_rooms)

    list_floors = [0] * 3
    floors_number = int(request.form.get('floor'))
    list_floors[floors_number] = 1
    list_features = np.append(list_features, list_floors)

    list_features = np.reshape(list_features, (1, -1))

    prediction = model.predict(list_features)

    output = round(prediction[0], 0)

    return render_template('index.html', prediction_text='Le prix de votre appartement est estimé à {} €.'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
