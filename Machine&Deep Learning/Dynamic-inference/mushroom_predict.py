import joblib 
import pandas as pd
from flask import Flask,request,jsonify

app=Flask(__name__)

@app.route('/',methods=['POST'])

def ml_inference():
    query_df=pd.DataFrame(request.json)
    df=pd.read_csv('https://labfile.oss.aliyuncs.com/courses/1321/mushrooms.csv')
    X=pd.get_dummies(df.iloc[:,1:])
    query=pd.get_dummies(query_df).reindex(columns=X.columns,fill_value=0)
    
    clf=joblib.load('mushroom_knn.pkl')
    predict=clf.predict(query)
    return jsonify({'result':[predict]})
