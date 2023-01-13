from flask import Flask
from flask import request,jsonify
from werkzeug.utils import secure_filename      
from keras.models import load_model
from os import remove



app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to cancer prediction API'


def initiate_model(model:str):
    model = load_model(path_to_model)

#write the code for removeing the image after classiciation 
#remove(os.path.join(CURRENT_DIR,image_name))
@app.route('/predict',methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({
            "error":"No such file in the request !"
            }),400
    file = request.files['file']
    curr_filename = file.filename
    if curr_filename == '':
        return jsonify({
            "error":"No file selected !"
            }),400
    if file and allowed_files(file.filename):
        filename =  secure_filename(file.filename)
        file.save(filename)
        return jsonify({
            "message":"File save successfully !"
            })
    else:
        return jsonify(
                {"error":"Invalid file type !"}
                ),400


def allowed_files(filename):
    ALLOWED_EXTENSIONS = {"png","jpeg","jpg","tiff","gif"}
    return '.' in filename and \
            filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == "__main__":
    app.run(debug=True)

