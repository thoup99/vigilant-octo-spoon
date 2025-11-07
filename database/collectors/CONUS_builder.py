from collectors.table_builder import TableBuilder
import Constants
import ee
import os

class CONUS_Builder(TableBuilder) :
    def __init__(self):
        super().__init__("CONUS", "GRIDMET/DROUGHT")


    def create_table(self):
        self.cursor.execute(f"""
            CREATE TABLE {self.table_name} (
                date text,
                lat text,
                long text,
                pdsi real,
                PRIMARY KEY (date, lat, long)
            );
        """)

    def collect_data(self):
        conus = ee.ImageCollection(self.ee_name).filterDate(Constants.START_DATE, Constants.END_DATE).select('pdsi')
        info_list = conus.aggregate_array('system:index').getInfo()

        for i, image_id in enumerate(info_list):
            print(f"{i+1}. {image_id}")

        raise NotImplementedError("CONUS collection needs fully implemented")