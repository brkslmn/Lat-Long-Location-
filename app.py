from flask import Flask, request, jsonify
from tablib import Dataset
from geopy.geocoders import Nominatim
import pandas as pd

app = Flask(__name__)
geolocator = Nominatim(user_agent="geoapiExercises")
app.config['JSON_AS_ASCII'] = False

@app.route("/python/", methods=['GET', 'POST'])
def upload_filee():
    
    return ''' <!doctype html>
    <style>
    a.button {
    -webkit-appearance: button;
    -moz-appearance: button;
    appearance: button;
    text-decoration: none;
    color: initial;
    }</style>
   
    <form action="post" method="get">
      <label for="lat">Latitude:</label>
      <input type="text" id="lat" name="lat"><br><br>
      <label for="long">Longtide:</label>
      <input type="text" id="long" name="long"><br><br>
      <input type="submit" value="Adres Bul">
    </form>
    <title>Upload an excel file</title>
    <button><a href="upload" class="button">Dosya Yükle</a></button>
     
    '''


@app.route("/python/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # class adresses: 
        #     def __init__(self, adress, machine): 
        #         self.adress = adress
        #         self.machine = machine
        adress = []
        machines = []
        df = pd.read_excel(request.files['file'])
        for index, row in df.iterrows():
            adress.append((str(geolocator.reverse(str(row['Latitude'])+","+str(row['Longtide'])))))
            machines.append(str(row['Machine No']))
          
        
       
        return jsonify({'machine':machines ,'adress':adress})
    return ''' <!doctype html>
    <title>Upload an excel file</title>
    <h1>Excel file upload (csv, tsv, csvz, tsvz only)</h1>
    <form action="" method=post enctype=multipart/form-data>
    <p><input type=file name=file><input type=submit value=Upload>
    </form>'''

@app.route('/python/post')
def show_post():
    lat = str(request.args.get('lat'))
    long = str(request.args.get('long'))
    
    adress = str(geolocator.reverse(lat+","+long))
    return jsonify({'adress':adress})

    

if __name__ == "__main__":
    app.run()
