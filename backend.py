import os
from flask import Flask, g, current_app, jsonify, request, send_from_directory
import db

app = Flask(__name__)


@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


@app.route('/')
def root():
    return send_from_directory('static', 'index.html')


@app.route('/afspraken', methods=['GET'])
def get_alle_afspraken():
    res = []
    afspraken = db.execute_sql('SELECT * FROM afspraak ORDER BY tijdstip')
    for afspraak in afspraken:
        res.append({
            'naam': afspraak['naam'],
            'tijdstip': afspraak['tijdstip']
        })
    return jsonify(res), 200, {'ContentType': 'application/json'}


@app.route('/afspraak', methods=['GET'])
def get_afspraken_via_email():
    data = request.json
    res = []
    if 'email' in data:
        afspraken = db.execute_sql(
            "SELECT * FROM afspraak WHERE email = '{}'".format(data['email']))
        for afspraak in afspraken:
            res.append({
                'naam': afspraak['naam'],
                'tijdstip': afspraak['tijdstip']
            })
    return jsonify(res), 200, {'ContentType': 'application/json'}


@app.route('/afspraak', methods=['POST'])
def maak_afspraak():
    data = request.json
    if 'tijdstip' in data:
        available = db.execute_sql(
            "SELECT COUNT(*) AS count FROM afspraak WHERE tijdstip = '{}'".format(data['tijdstip']))

        valid = True
        for row in available:
            if row['count'] == 1:
                valid = False

        if valid:
            db.execute_sql("INSERT INTO afspraak(naam, email, tijdstip) VALUES ('{}','{}','{}')".format(
                data['naam'], data['email'], data['tijdstip']))
            return jsonify({'success': True}), 200, {'ContentType': 'application/json'}
        else:
            return jsonify({'success': False, 'reason': 'Date and time already taken'}), 200, {'ContentType': 'application/json'}
    else:
        return jsonify({'success': False, 'reason': 'Failed to provide date and time for appointment'}), 400,  {'ContentType': 'application/json'}


if __name__ == '__main__':
    app.run()
