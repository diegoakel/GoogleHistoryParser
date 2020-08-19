import pandas as pd
import json
import csv
from datetime import datetime
import tldextract


def toCSV (data): 
    file_name = "output.csv"
    with open (file_name, "w", newline="") as File:
        csv_file = csv.writer(File)
        csv_file.writerow(["Page transition", "Title", "Domain","Year", "Month", "Day", "Hour", "Minute", "Second"])
        for item in data["Browser History"]:

            domain = tldextract.extract(item["url"])[1]

            time = pd.to_datetime(item["time_usec"],unit='us',utc=True).tz_convert("Etc/GMT+4")
           
            year  = time.year
            month = time.month
            day  = time.day
            hour  = time.hour
            minute = time.minute
            second  = time.second

            csv_file.writerow([item["page_transition"], item["title"], domain, year, month, day, hour, minute, second])

with open("BrowserHistory.json") as json_file:
  data = json.load(json_file)
  toCSV(data)