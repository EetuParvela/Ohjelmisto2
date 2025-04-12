from flask import Flask, Response
import json

app = Flask(__name__)


@app.route('/alkuluku/<number>')
def is_prime_number(number):
    try:
        number = int(number)
        is_prime = True
        if number <= 1:
            is_prime = False
        else:
            for num in range(2, int(number ** 0.5) + 1):
                if number % num == 0:
                    is_prime = False
                    break
            else:
                is_prime = True

        result = {
            "Number": number,
            "isPrime": is_prime
        }

    except ValueError:
        status_code = 400
        result = {
            "status_code": status_code,
            "text": "Virheellinen syöte"
        }

    json_result = json.dumps(result)
    return Response(response=json_result, status=404, mimetype="application/json")


@app.errorhandler(404)
def page_not_found(error_code):
    result = {
        "status": "404",
        "text": "Virheellinen päätepiste"
    }

    json_result = json.dumps(result)
    return Response(response=json_result, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
