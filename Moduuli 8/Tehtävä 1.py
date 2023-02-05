import mysql.connector
kursori = yhteys.kursori()
icao.koodi = input("Anna lentoaseman ICAO-koodi: ")
kursori.execute("Select name, city FROM airport WHERE ident=?")
tulos = kursori.fetchall()
if result:
    print("Lentokentän nimi:", result [0])

import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='nimo',
         password='nimohanna',
         autocommit=True
         )