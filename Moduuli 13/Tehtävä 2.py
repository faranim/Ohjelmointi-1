import json
from flask import Flask, Response
import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='hanna',
         password='nimohanna',
         autocommit=True
         )

app = Flask(__name__)
@app.route('/kenttä/<icaokoodi>')
def haku(icaokoodi):
    sql= "select name, municipality from airport where ident = %"
    kursori = yhteys.curos()
    kursori.execute(sql,(icaokoodi,))

    tulos = kursori.fetchone()

    if tulos is not None:
        vastaus = {
            "ICAO": icaokoodi,
            "Name": tulos[0],
            "Municipality": tulos [1]
        }
        jsonvast = json.dump(vastaus)
        return Response(response=jsonvast, status=200, mimetype="application/json")
    else:
        vastaus = {
            "status": "404",
            "teksti": "Vastaus ei löydy"
        }
        jsonvast = json.dump(vastaus)
        return Response(response=jsonvast, status=200, mimetype="application/json")


if __name__== '__main__':
    app.run(use_reloader=True, host ='127.0.0.1', port=3306)


