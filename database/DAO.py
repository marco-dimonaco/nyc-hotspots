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
                SELECT nwhl1.Location l1, nwhl2.Location l2, avg(nwhl1.Latitude) as lat1, avg(nwhl1.Longitude) as lon1, 
                avg(nwhl2.Latitude) as lat2, avg(nwhl2.Longitude) as lon2 
                FROM nyc_wifi_hotspot_locations nwhl1, nyc_wifi_hotspot_locations nwhl2 
                WHERE nwhl1.Provider = nwhl2.Provider and nwhl1.Provider = %s and nwhl1.Location < nwhl2.Location
                GROUP BY nwhl1.Location, nwhl2.Location
                """
        cursor.execute(query, (provider,))
        for row in cursor:
            result.append(Connessione(**row))
        cursor.close()
        conn.close()
        return result

    """
    SELECT n1.Location as n1Loc, n2.Location as n2Loc, avg(n1.Latitude) as n1Lat, avg(n1.Longitude) as n1Long, 
    avg(n2.Latitude) as n2Lat, avg(n2.Longitude) as n2Long
    FROM nyc_wifi_hotspot_locations n1, nyc_wifi_hotspot_locations n2
    WHERE n1.Provider = n2.Provider
    and n1.Provider = %s
    and n1.Location < n2.Location
    GROUP by n1.Location, n2.Location
    """
