from collectors.table_collector import TableCollector
import Constants
import ee

class DaymetV4Collector(TableCollector) :
    def __init__(self):
        super().__init__("DaymetV4", "NASA/ORNL/DAYMET_V4")


    def create_table(self):
        self.cursor.execute(f"""
            CREATE TABLE {self.table_name} (
                date text,
                lat text,
                long text,
                prcp real,

                PRIMARY KEY (date, lat, long)
            );
        """)

    def collect_data(self):
        raise NotImplementedError("DaymetV4 collection needs implemented")
        daymetV4 = ee.ImageCollection(self.ee_name).filterDate(Constants.START_DATE, Constants.END_DATE)