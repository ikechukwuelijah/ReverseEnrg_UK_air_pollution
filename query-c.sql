"""
Task: Extend the previous query to show these values for all stations in the years 2010 to 2019.
"""

select location.location, AVG(`reading`.`PM2.5`) as "AVG PM2.5" , AVG(`reading`.`VPM2.5`) as "AVG VPM2.5" from  reading,location
where DATE_FORMAT(CAST(`Date Time` AS DATETIME), "%Y") BETWEEN '2010' AND '2019' and DATE_FORMAT(CAST(`Date Time` AS DATETIME), "%H") = 08 and location.site_id = reading.SiteID
group by location.location;
