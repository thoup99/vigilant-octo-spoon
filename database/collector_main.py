import ee
import os
from dotenv import load_dotenv
from collectors.FIRMS_collector import FIRMSCollector
from collectors.CONUS_collector import CONUSCollector
from collectors.CFSR_collector import CFSRCollector
from collectors.DaymetV4_collector import DaymetV4Collector
from collectors.CPC_collector import CPCCollector

class Collector():
    def __init__(self):
        load_dotenv()
        ee.Authenticate()
        ee.Initialize(project=os.getenv("EE_PROJECT"))
        print("Google Earth Engine initialized successfully!")

    def collect_all(self):
        self.collect_FIRMS()
        self.collect_CONUS()
        self.collect_CFSR()
        self.collect_DaymetV4()
        self.collect_CPC_Precipitation

    def collect_FIRMS(self):
        fc =  FIRMSCollector()
        fc.collect_data()

    def collect_CONUS(self):
        coc = CONUSCollector()
        coc.collect_data()

    def collect_CFSR(self):
        cfc = CFSRCollector()
        cfc.collect_data()

    def collect_DaymetV4(self):
        d4c = DaymetV4Collector()
        d4c.collect_data()

    def collect_CPC_Precipitation(self):
        cpc = CPCCollector()
        cpc.collect_data()



if (__name__ == "__main__"):
    collector = Collector()
    functions = [collector.collect_FIRMS, collector.collect_CONUS, collector.collect_CFSR,  
                 collector.collect_DaymetV4, collector.collect_CPC_Precipitation, collector.collect_all]
    
    choice = int(input("" +
    "1) FIRMS\n" +
    "2) CONUS\n" +
    "3) CFSR\n" +
    "4) DaymetV4\n" +
    "5) CPC Preciptitation\n" +
    "6) All\n" +
    "Enter Database to Collect: "
    ))
    
    
    functions[choice - 1]()