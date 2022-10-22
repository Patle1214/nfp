import os                                           #allows code to access computer files
from flask import Flask, request, jsonify, abort    #the base of the server
import json                                         #a container of key-info pairs
import yolo
# import classifier
app = Flask(__name__)
app.config["UPLOAD_EXTENSIONS"] = [".jpg",".jpeg",".png"]
@app.route('/analyze/', methods=['GET', 'POST']) # www.whatever.com/hello/


def cnt():
    userimg = request.files.getlist("image")[0] #specific for flask for file request
    f = userimg.filename
    if(f != ""):
        root_ext = os.path.splitext(f)

        if root_ext[1] not in app.config["UPLOAD_EXTENSIONS"]:
            abort(400)  #stops the program
        else:
            userimg.save(f) # save the img into the code the directory
            items = yolo.count(f)
            os.remove(f)
    
    return jsonify(items)

if __name__ == '__main__':
    app.run(host='0.0.0.0')


'''
'''