from collectors.table_builder import TableBuilder
import Constants
import ee
import os

class FIRMS_Builder(TableBuilder) :
    def __init__(self):
        super().__init__("FIRMS", "FIRMS")


    def create_table(self):
        self.cursor.execute(f"""
            CREATE TABLE {self.table_name} (
                date text,
                lat text,
                long text,
                confidence int,
                brightness real,
                frp real,
                PRIMARY KEY (date, lat, long)
            );
        """)

    def collect_data(self):
        raise NotImplementedError("FIRMS collection needs implemented")
        #firms = ee.ImageCollection(self.ee_name).filterDate(Constants.START_DATE, Constants.END_DATE)
