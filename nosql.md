"""
Task: Model the data for a specific monitor (station) to a NoSQL data model (key-value, xml or graph) to implement the selected database type/product & pipe or import the data.

"""
># Introduction to mongodb

The NoSQL also known as ‘Not Only SQL' which allows us to store and retrieve data in the form of collections other than relational format (Rows and Columns). But they can also query languages in their SQL type or form. NoSQL can store data in the form of Key-Value, document columnar and graph.
In this piece of course work, I opted to use the ‘MongoDB’ since it supports data in csv files and BSON. BSON is designed as a binary representation of JSON data. Mongodb uses collections of document and widely integrated with python. The other features include;

NoSQL databases are designed to break away from the rows and columns of the relational database model. But it’s a common mistake to think that NoSQL databases don’t have any sort of data model. A useful description of how the data will be organized is the beginning of a schema. 
From my finding I deduced that Mongodb  does great by storing large amount of data, and can enhance its usefulness if combined with other nosql database systems for example 'redis' compliments mongodb in processing real-time and real-word applications. For example, the online dating application maintains its user profiles in MongoDB, but uses Redis to track user locations over time. In other words, MongoDB is capable of storing a great deal of data, but Redis can help it process that data in real time. 

Like wise when I compare Couchbase with Mongodb there are similarities and differences and so with the other databases listed for us to choose from. 
 > # Advantages of mongodb
> 
- Mongodb is flexible unlike SQL database which can adapt to change in complex process of data migration.
- It supports scalability of data or records.
- It has a powerful support for running analytics natively using the aggregation framework
- Mongodb allows easy modelling and manipulation of any data structure
- Easy to create collections, retrieve, update and drop
- Mongodb is a general purpose database system
- MongoDB stores data in BSON format (binary JSON) but with specific extensions for broader applications 
- its affordable


># Mongodb Syntax

_working with mongosh git bash_
_I created a collection called 'location' in my pollution-db_
```
db.createCollection("location");
```

_inserts site_id and location in my collection_


```
db.location.insertOne({
"_id": 206,
"location": "Rupert Street",
"geo_point": "(51.4554331987,-2.59626237324)"
});
```
{ acknowledged: true, insertedId: 206 }

 
```
pollution_db> db.createCollection("location");
```
{ ok: 1 }

## Model the data for a specific monitor (station) 
```
pollution_db>
db.location.insertOne({
"_id": 206,
"location": "Rupert Street",
"geo_point": "(51.4554331987,-2.59626237324)"
});
```

pollution_db> ... ... ... ...
{ acknowledged: true, insertedId: 206 }
pollution_db>

pollution_db>

pollution_db>


_**find function looks up 'location' in database**_
```
pollution_db> db.location.find().pretty();
[
  {
    _id: 206,
    location: 'Rupert Street',
    geo_point: '(51.4554331987,-2.59626237324)'
  }
]
```

_**create 'reading' collection**_
```
pollution_db> db.createCollection("reading");
```
{ ok: 1 }
pollution_db>





##import reading from site_id
```
SELECT * FROM `reading` where SiteID =206;
```


./mongoimport --db pollution_db --collection reading --type csv --file reading.csv --headerline
2022-04-12T08:54:22.531+0100    connected to: mongodb://localhost/
2022-04-12T08:54:24.351+0100    52584 document(s) imported successfully. 0 document(s) failed to import.





##Joining the two collections using Site_id readings as foreign key 

```db.location.aggregate([
  {
    $lookup: {
      from: "reading",
      localField: "_id",
      foreignField: "SiteID",
      as: "reading"
    }
  },
{$project : {
         "_id": 1,
         "location": 1,
         "geo_point": 1,
         "reading": {
            "$slice":["$reading", 2]
         }
       }
}
])
```

###The output which is limited to 2 readings for selected station

[
  {
    _id: 206,
    location: 'Rupert Street',
    geo_point: '(51.4554331987,-2.59626237324)',
    reading: [
      {
        _id: ObjectId("625533b342660aa10ac5b9f3"),
        id: 1,
        'Date Time': '2014-08-22T06:00:00+00:00',
        NOx: 249.5,
        NO2: 26.75,
        NO: 145,
        SiteID: 206,
        PM10: 'NULL',
        NVPM10: 'NULL',
        VPM10: 'NULL',
        NVPM25: 'NULL',
        PM25: 'NULL',
        VPM25: 'NULL',
        CO: 'NULL',
        O3: 'NULL',
        SO2: 'NULL',
        Temperature: 'NULL',
        RH: 'NULL',
        'Air Pressure': 'NULL',
        DateStart: '2003-01-01T00:00:00+00:00',
        DateEnd: '2015-12-31T00:00:00+00:00',
        Current: 0,
        'Instrument Type': 'Continuous (Reference)'
      },
      {
        _id: ObjectId("625533b342660aa10ac5b9f4"),
        id: 15,
        'Date Time': '2014-08-21T08:00:00+00:00',
        NOx: 861.25,
        NO2: 139,
        NO: 470.75,
        SiteID: 206,
        PM10: 'NULL',
        NVPM10: 'NULL',
        VPM10: 'NULL',
        NVPM25: 'NULL',
        PM25: 'NULL',
        VPM25: 'NULL',
        CO: 'NULL',
        O3: 'NULL',
        SO2: 'NULL',
        Temperature: 'NULL',
        RH: 'NULL',
        'Air Pressure': 'NULL',
        DateStart: '2003-01-01T00:00:00+00:00',
        DateEnd: '2015-12-31T00:00:00+00:00',
        Current: 0,
        'Instrument Type': 'Continuous (Reference)'
      }
    ]
  }
]

 #Challenges I encountered
1. Coping with the sudden change from tables to collections
2. Joining my two collections site_id and location
3. Importing all the reading for my selected location hence limited to two readings
4. Boring terminal with limited functions. unless with git bash
5. Schema definition is challenging
6. I couldnt copy from mongodb terminal hence I used git bash

**REFERENCES**
* www.mongodb.com
* https://fetstudy.uwe.ac.uk/~p-chatterjee/2021-22/modules/dmf-jan/assignment/
* https://www.w3schools.in/benefits-of-using-nosql
* https://www.youtube.com/watch?v=WBUN_4NWHYI
