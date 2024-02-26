from pymongo import MongoClient
from Mynextfilm.Utilities.commonMethods import format_date


class MongoDBConnector:
    def __init__(self, db_url, db_name):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
    def find_documents_date_desc(self, table_name, query={}, sort_field="created_at", sort_order=-1):
        collection = self.db[table_name]
        results = collection.find(query).sort({sort_field: sort_order})

        matching_documents = []
        for result in results:
            matching_documents.append(result)

        #self.client.close()
        return matching_documents

    def find_documents_likes_desc(self, table_name, query={}, sort_field1="likes", sort_order1=-1, sort_field2="created_at", sort_order2=-1):
        collection = self.db[table_name]
        results = collection.find(query).sort({sort_field1: sort_order1, sort_field2: sort_order2})

        matching_documents = []
        for result in results:
            matching_documents.append(result)

        #self.client.close()
        return matching_documents

    def find_documents_date_asce(self, table_name, query={}, sort_field="created_at", sort_order=1):
        collection = self.db[table_name]
        results = collection.find(query).sort({sort_field: sort_order})

        matching_documents = []
        for result in results:
            matching_documents.append(result)

        #self.client.close()
        return matching_documents

    def find_documents_likes_asce(self, table_name, query={}, sort_field1="likes", sort_order1=1, sort_field2="created_at", sort_order2=1):
        collection = self.db[table_name]
        results = collection.find(query).sort({sort_field1: sort_order1, sort_field2: sort_order2})

        matching_documents = []
        for result in results:
            matching_documents.append(result)

        #self.client.close()
        return matching_documents


if __name__ == "__main__":
    dbURL = "mongodb+srv://MNF:root@cluster0.gbkxi.gcp.mongodb.net/DB?retryWrites=true&w=majority"
    myDB = "DB"
    myTable = "ideamall2_premise"

    connector = MongoDBConnector(dbURL, myDB)
    find = "hawala@gmail.com"
    query = {}

    matching_document = connector.find_documents_likes_desc(myTable, query)    # , sort_field="created_at", sort_order=-1

    print("Matching Documents:")
    a = 0
    for a, result in enumerate(matching_document, start=1):
        user = result.get("created_by_id", "")
        date = result.get("created_at", "")
        dbpremise = result.get("text", "")
        date, time = format_date(date)
        like = result.get("likes", "")
        premise = dbpremise.split("+", 1)[1].strip()
        # # if a % 12 == 1:
        print(f"Premise: {premise}, Likes: {like}")
        # # print(f"{date}...{time}")
        # print(result)
