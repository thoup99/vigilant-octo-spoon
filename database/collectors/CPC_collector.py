from collectors.table_collector import TableCollector
import Constants
import ee

class CPCCollector(TableCollector) :
    def __init__(self):
        super().__init__("CPC", "NOAA/CPC/Precipitation")


    def create_table(self):
        self.cursor.execute(f"""
            CREATE TABLE {self.table_name} (
                date text,
                lat text,
                long text,
                precipitation real,
                
                PRIMARY KEY (date, lat, long)
            );
        """)

    def collect_data(self):
        raise NotImplementedError("CPC collection needs implemented")
        cpc = ee.ImageCollection(self.ee_name).filterDate(Constants.START_DATE, Constants.END_DATE)