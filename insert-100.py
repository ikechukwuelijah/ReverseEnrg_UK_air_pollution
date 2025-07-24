"""
Task: Create a PYTHON script (insert-100.py) that generates a SQL file (insert-100.sql) that holds the first 100 inserts to the main data table.
"""

import sys

import pymysql as pm

try:
    # I connected to mysql
    conn = pm.connect(host='localhost', user='root', passwd="", database="pollution-db2")

    # I created the cursor
    cur = conn.cursor()


    # I imported 100-data
    sql_query = "SELECT * FROM `reading` LIMIT 100;"

    # I carried out the cursor with the sql string
    cur.execute(sql_query)

    # fetched indexed list
    result = cur.fetchall()

    # Create an insert-100.sql File to write insert statements
    insert_file = open("insert-100.sql", "w")

    # Looping through the results and SQL insert statement

    for res in result:
        print(res)
        sql_insert = """
                 INSERT INTO `pollution-db2`.`reading`
                (`Date Time`, `NOx`, `NO2`, `NO`, `SiteID`, `PM10`, `NVPM10`, `VPM10`, `NVPM2.5`, `PM2.5`, `VPM2.5`,
                `CO`, `O3`, `SO2`, `Temperature`, `RH`, `Air Pressure`, `DateStart`, `DateEnd`, `Current`, `Instrument Type`)
                VALUES('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},'{}');
                """.format(
            res[1],
            res[2],
            res[3],
            res[4],
            res[5],
            res[6],
            res[7],
            res[8],
            res[9],
            res[10],
            res[11],
            res[12],
            res[13],
            res[14],
            res[15],
            res[16],
            res[17],
            res[18],
            res[19],
            bool(res[20]),
            res[21])
        # insert mysql records
        insert_file.write(sql_insert)

        # close database connection
    conn.close()
    insert_file.close()


# print(failed to insert record into MySQL table, if it failed to insert)
except BaseException as err:
    print(f"Database Error occured: {err}")
    sys.exit(1)
