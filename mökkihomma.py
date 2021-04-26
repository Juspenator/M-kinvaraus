import mysql.connector

yhteys = mysql.connector.connect(user = 'root', password = 'Juuso',
host = '127.0.0.1', database = 'vn')

cursor = yhteys.cursor()

sqlkysely = ("SELECT etunimi, sukunimi, postinro FROM asiakas")

cursor.execute(sqlkysely)

for (etunimi, sukunimi, postinro) in cursor:
    print("henkilön {} {} POSTINUMERO ON {}".format(etunimi, sukunimi, postinro))

yhteys.close()    