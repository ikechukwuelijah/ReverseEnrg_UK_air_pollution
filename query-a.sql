"""
Task: Return the date/time, station name and the highest recorded value of nitrogen oxide (NOx) found in the dataset for the year 2019.
"""

select NOX, CAST(`Date Time` AS DATETIME),location.location as Date_Time from reading,location
where NOX = (select max(NOX) from reading  where DATE_FORMAT(CAST(`Date Time` AS DATETIME), "%Y") = '2019') and location.site_id = reading.SiteID;
