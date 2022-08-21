from flask import Flask,request,jsonify
import pymongo
app=Flask(__name__)
client=pymongo.MongoClient("mongodb://localhost:27017")
db=client['taskdb']
collection=db['taskcollection']


@app.route('/insert/mongo',methods=['POST'])
def insert():
    if request.method=='POST':
        name=request.json['name']
        number=request.json['number']
        collection.insert_one({name:number})
    return jsonify(str('Successfully inserted'))


@app.route('/update/mongo',methods=['POST'])
def update():
    if request.method=='POST':
        t_name=request.json['t_name']
        collection.update_one({'name':t_name},{"$set":{'number':161}})
    return jsonify(str('Successfully updated'))



if __name__ == '__main__':
    app.run(port=5001)