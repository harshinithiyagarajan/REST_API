from flask_pymongo import pymongo
from flask import request
import pandas as pd

db_string="mongodb+srv://harshini:harshini@cluster0.cy2fxe9.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(db_string)
db=client.get_database('collection')
user_collection=pymongo.collection.Collection(db,'sample')
print("Mongodb connected successfully")

def rest_api(endpoint):
    @endpoint.route('/print_user',methods=['GET'])
    def print_user():
        res = 'Hello world'
        print("Hello world")
        return res
        # res={}
        # try:
        #     users=user_collection.find({})
        #     print(users)
        #     users=list(users)
        #     status={
        #         "status code":"200",
        #         "status message":"User data successfully retrieved from the database"
        #     }
        #     output=[{'Name':user['name'],'DOB':user['dob']} for user in users]
        #     res['data']=output
        # except Exception as e:
        #     print(e)
        #     status={
        #         "status code":"400",
        #         "status message":str(e)
        #     }    
        # res["status"]=status
        # return res    

    @endpoint.route('/update_user',methods=['PUT'])    
    def update_user():
        res={}
        try:
            req=request.json
            user_collection.update_one({"name":req['id']}, {"dob": req['updated_user_body']})
            print("User data successfully updated")
            status={
                "statusCode":"200",
                "statusMessage":"User Data Updated Successfully in the Database."
            }
        except Exception as e:
            print(e)
            status = {
                "statusCode":"400",
                "statusMessage":str(e)
            }
        res["status"]=status
        return res

    @endpoint.route('/delete_user',methods=['DELETE'])  
    def delete_user():
        res={}
        try:
            del_id=request.args.get('del_id')
            user_collection.delete_one({"id":del_id})
            status = {
                "statusCode":"200",
                "statusMessage":"User Data Deleted Successfully in the Database."
            }
        except Exception as e:
            print(e)
            status = {
                "statusCode":"400",
                "statusMessage":str(e)
            }
        res["status"]=status
        return res

    @endpoint.route('/upload_user',methods=['POST'])
    def upload_user():
        res={}
        try:
            req=request.form
            file=request.files.get('file')
            df=pd.read_csv(file)
            print(df)
            print(df.head)
            print(df.columns())
            status = {
                "status Code":"200",
                "status Message":"File uploaded Successfully."
            }
        except Exception as e:
            print(e)
            status = {
                "status Code":"400",
                "status Message":str(e)
            }
        res["status"]=status
        return res

    return endpoint

    
