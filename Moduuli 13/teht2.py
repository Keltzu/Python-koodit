from flask import Flask, jsonify

app = Flask(__name__)

airports = {
    "EFHK": {"Name": "Helsinki Vantaa Airport", "Municipality": "Helsinki"},
    "EFKK": {"Name": "Kokkola-Pietarsaari Airport", "Municipality": "Kokkola"},
    "ESSA": {"Name": "Stockholm Arlanda Airport", "Municipality": "Stockholm"}
}

@app.route('/kenttä/<icao>', methods=['GET'])
def get_airport(icao):
    airport = airports.get(icao)
    if airport:
        return jsonify({"ICAO": icao, **airport})
    return jsonify({"error": "Lentokenttää ei löytynyt"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=3000)