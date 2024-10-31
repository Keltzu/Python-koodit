from flask import Flask, jsonify
import math

app = Flask(__name__)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

@app.route('/alkuluku/<int:num>', methods=['GET'])
def check_prime(num):
    return jsonify({"Number": num, "isPrime": is_prime(num)})

if __name__ == '__main__':
    app.run(debug=True, port=3000)