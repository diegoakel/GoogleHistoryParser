# -*- coding: utf-8 -*-

import pandas as pd
import json
import csv
from datetime import datetime
from urllib.parse import urlparse


def toCSV (data): 
    file_name = "output.csv"
    with open (file_name, "w", newline="") as File:
        csv_file = csv.writer(File)
        csv_file.writerow(["Page transition", "Title", "Domain","Year", "Month", "Day", "Hour", "Minute", "Second"])
        for item in data["Browser History"]:

            domain = urlparse(item["url"]).netloc

            time = pd.to_datetime(item["time_usec"],unit='us',utc=True).tz_convert("Etc/GMT+4")
           
            year  = time.year
            month = time.month
            day  = time.day
            hour  = time.hour
            minute = time.minute
            second  = time.second

            csv_file.writerow([item["page_transition"], item["title"].encode('utf-8'), domain, year, month, day, hour, minute, second])

with open("BrowserHistory.json", "r", encoding="utf-8") as json_file:
  data = json.load(json_file)
  toCSV(data)