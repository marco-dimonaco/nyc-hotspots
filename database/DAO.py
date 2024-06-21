from database.DB_connect import DBConnect
from model.connessione import Connessione


class DAO:
    @staticmethod
    def getAllProviders():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT distinct nwhl.Provider as p
                FROM nyc_wifi_hotspot_locations nwhl
                ORDER BY nwhl.Provider asc 
                """
        cursor.execute(query)
        for row in cursor:
            if row is not None:
                result.append(row['p'])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllLocations(provider):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT distinct nwhl.Location  as l
                FROM nyc_wifi_hotspot_locations nwhl
                WHERE  nwhl.Provider = %s
                """
        cursor.execute(query, (provider,))
        for row in cursor:
            result.append(row['l'])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnessioni(provider):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT DISTINCT nwhl.Location, AVG(nwhl.Latitude) as Latitude, AVG(nwhl.Longitude) as Longitude 
                FROM nyc_wifi_hotspot_locations nwhl
                WHERE nwhl.Provider = %s
                GROUP BY nwhl.Location
                """
        cursor.execute(query, (provider,))
        for row in cursor:
            result.append(Connessione(row['Location'], row['Latitude'], row['Longitude']))
        cursor.close()
        conn.close()
        return result
