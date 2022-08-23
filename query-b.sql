"""
@author: 21076682
Task 4b. Return the mean values of PM2.5 (particulate matter <2.5 micron diameter) & VPM2.5 (volatile particulate matter <2.5 micron diameter) by each station for the year 2019 for readings taken on or near 08:00 hours (peak traffic intensity)
"""

select location.location, AVG(`reading`.`PM2.5`) , AVG(`reading`.`VPM2.5`) from  reading,location
where DATE_FORMAT(CAST(`Date Time` AS DATETIME), "%Y") = '2019' and DATE_FORMAT(CAST(`Date Time` AS DATETIME), "%H") = 08 and location.site_id = reading.SiteID
group by location.location ;