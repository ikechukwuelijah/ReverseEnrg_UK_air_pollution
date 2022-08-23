"""
@author: 21076682
Task 3a. Design, write, & test a PYTHON script (populate.py) that takes the cleaned CSV file as input and creates a new database instance (pollution-db2) and populates it.
"""
# import lib
import mysql.connector
import pandas as pd  # pip install pandas
from sqlalchemy import create_engine

# df['Date Time'].iloc[:5]

host = "localhost"
password = ""
user = "root"
try:
    # Connecting to mysql instance using parameters
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )

    mycursor = mydb.cursor()

    # check if database already exist and delete it. Recreate database
    mycursor.execute("DROP DATABASE IF EXISTS `pollution-db2` ;")
    mycursor.execute("CREATE DATABASE `pollution-db2`;")

except mysql.connector.Error as err:
    print("An error occurred creating database: %s" % err)

engine = create_engine(
    "mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=host, user=user, pw=password, db="pollution-db2"))

columns = ["Date Time", "NOx", "NO2", "NO", "SiteID", "PM10", "NVPM10", "VPM10", "NVPM2.5",
           "PM2.5", "VPM2.5", "CO", "O3", "SO2", "Temperature", "RH", "Air Pressure", "Location",
           "geo_point_2d", "DateStart", "DateEnd", "Current", "Instrument Type"]

# create stations as a pandas dataframe
df_site = pd.DataFrame([
    [188, 'AURN Bristol Centre', ""],
    [203, 'Brislington Depot', "51.4417471802,-2.55995583224"],
    [206, 'Rupert Street', "51.4554331987,-2.59626237324"],
    [209, 'IKEA M32', ""],
    [213, 'Old Market', "51.4560189999,-2.58348949026"],
    [215, 'Parson Street School', "51.432675707,-2.60495665673"],
    [228, 'Temple Meads Station', ""],
    [270, 'Wells Road', "51.4278638883,-2.56374153315"],
    [271, 'Trailer Portway P&R', ""],
    [375, 'Newfoundland Road Police Station', "51.4606738207,-2.58225341824"],
    [395, "Shiner's Garage", "51.4577930324,-2.56271419977"],
    [452, 'AURN St Pauls', "51.4628294172,-2.58454081635"],
    [447, 'Bath Road', "51.4425372726,-2.57137536073"],
    [459, 'Cheltenham Road \ Station Road', "51.4689385901,-2.5927241667"],
    [463, 'Fishponds Road', "51.4780449714,-2.53523027459"],
    [481, 'CREATE Centre Roof', "51.447213417,-2.62247405516"],
    [500, 'Temple Way', "51.4579497129,-2.58398909033"],
    [501, 'Colston Avenue', "51.4552693825,-2.59664882861"]

], columns=('site_id', 'location', "geo_point"))

connection = mysql.connector.connect(host='localhost',
                                     database='pollution-db2',
                                     user='root',
                                     password='',
                                     port=3306)
# df.fillna(0, inplace=True)


try:

    cursor = connection.cursor()

    # delete table before running populate station code
    drop_table_loc_query = "DROP TABLE IF EXISTS `pollution-db2`.`location` ;"
    cursor.execute(drop_table_loc_query)
    connection.commit()

    # populate the location table with the station name, station id and geo point using pandas
    df_site.to_sql("location", con=engine, index=False, index_label="site_id", if_exists="replace")

    # delete table before running populate reading code
    drop_table_loc_query = "DROP TABLE IF EXISTS `pollution-db2`.`reading` ;"
    cursor.execute(drop_table_loc_query)
    connection.commit()

    # read data from the clean csv file into a dataframe
    df_reading = pd.read_csv("clean.csv", sep=";", low_memory=False)

    # Drop columns which are already in the location table
    df_reading.drop(columns=["Location", "geo_point_2d"], axis=1, inplace=True)

    # populate the reading with the csv data using pandas dataframe
    df_reading.to_sql("reading", con=engine, index=True, index_label="id", if_exists="replace")


# print(failed to insert record into MySQL table, if it failed to insert)
except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
