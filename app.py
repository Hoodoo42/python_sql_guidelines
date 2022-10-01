
import mariadb
import dbhelpers as dbh

def choose_rooms():
    user_choice = input('how many rooms ')
    results = dbh.execute_statement('CALL room_check(?)', [user_choice])


def choose_city():
    city = input('how many rooms ')
    results = dbh.execute_statement('CALL city_check(?)', [city])