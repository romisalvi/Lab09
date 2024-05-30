from database.DB_connect import DBConnect
from model.airport import Airport
from model.flight import Flight


class DAO():
    def __init__(self):
        pass

    def getAllFlights(self):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT f.*
                           FROM flights f
                           """

        cursor.execute(query)

        for row in cursor:
            result.append(
                Flight(row["ID"],
                       row["AIRLINE_ID"],
                       row["FLIGHT_NUMBER"],
                       row["TAIL_NUMBER"],
                       row["ORIGIN_AIRPORT_ID"],
                       row["DESTINATION_AIRPORT_ID"],
                       row["SCHEDULED_DEPARTURE_DATE"],
                       row["DEPARTURE_DELAY"],
                       row["ELAPSED_TIME"],
                       row["DISTANCE"],
                       row["ARRIVAL_DATE"],
                       row["ARRIVAL_DELAY"]
                       )
            )

        cursor.close()
        conn.close()
        return result

    def getAllAirports(self):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT a.*
                           FROM airports a
                           """

        cursor.execute(query)

        for row in cursor:
            result.append(
                Airport(row["ID"],
                       row["IATA_CODE"],
                       row["AIRPORT"],
                       row["CITY"],
                       row["STATE"],
                       row["COUNTRY"],
                       row["LATITUDE"],
                       row["LONGITUDE"],
                       row["TIMEZONE_OFFSET"]
                       )
            )

        cursor.close()
        conn.close()
        return result