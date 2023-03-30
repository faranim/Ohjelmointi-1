from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/alkuluku/<int:n>', methods=['GET'])
def check_prime(n):
    return jsonify({'Number': n, 'isPrime': is_prime(n)})

if __name__ == '__main__':
    app.run(port=3000)
