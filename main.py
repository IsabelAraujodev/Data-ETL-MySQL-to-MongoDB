

from sqlalchemy import Text
from Extract.mysql_connection import MySQLConnection, QUERY
from Load.mongodb_connection import MongoDBConnection
from Transformation.data_transformation import transforming_data

if __name__ == "__main__":

    #In Step 1 --> connecting and retrieving the data

    instance_mysql = MySQLConnection(user='root', 
                                     password='senha',
                                     database='classicmodels')
    
    instance_mysql.set_mysql_engine()
    engine = instance_mysql.engine

    sql_query = text(QUERY)
    query_result = engine.execute(sql_query)

    print('Closing the MySQL connection...')
    engine.disponse()

    #In Step 2 --> Data Transformation

    posts = transforming_data(data = query_result.mappings().all())
    print('Total of docs:', len(posts))

    #In Step 3 --> Connection and data insertion into MongoDB

    instance_mongodb = MongoDBConnection(
                            domain='cluster0.2nj1fc2.mongodb.net/?retryWrites=true&w=majority',
                            user='pymongo',
                            passwd='chave'
    )

    client = instance_mongodb.connection()
    #db = client['dio_analytics']
    db = client.get_database('dio_analytics')
    print('Coleções:\n', db.list_collection_names())

    collection = db.get_collecttion('orders')
    for doc in posts:
        result = collection.insert_one(doc)
        print(result.inserted_id)

    print("Closing the MongoDB connection!")
    client.close()


                                     