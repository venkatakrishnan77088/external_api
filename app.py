from flask import Flask, render_template,request
import templates
import requests

 
app = Flask(__name__)

new_post = []
l = [120185, 139619, 148921, 149383, 148404, 119354]
# @app.route('/')
# def sample():
#     for i in range(len(l)):
#         url ="https://api.mfapi.in/mf/"+str(l[0])
#         resp = requests.get(url)
#         # print(resp)
#         return render_template('sample.html', data=resp.json().get('meta').get('fund_house') .get('data')[0].get('nav'))
i=0
@app.route("/", methods=["POST","GET"])
def api():
    for i in range(0,len(l)):
        url = "https://api.mfapi.in/mf/" + str(l[i])
        # print(url)
        resp = requests.get(url)
        # print(resp)
       
        fund_house = resp.json().get("meta").get("fund_house")
        nav = resp.json().get("data")[0].get("nav")
        temp_dic = {"id": l[i], "fund_house": fund_house, "nav": nav}
        #new_post.append(temp_dic)
        #if i<len(l):
        new_post.append(temp_dic)
             #i += 1
    outputlist=new_post
       
    return render_template("index.html", data=outputlist)  
    
if __name__ == "__main__":
    app.run(debug=True) 
    
    
    