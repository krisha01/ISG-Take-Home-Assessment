from flask import Flask
from flask import request
from flask_restful import Resource, Api, reqparse
import pandas as pd


app = Flask(__name__)
api = Api(app)
birds_path = r'..\Wingspan_Birds_data.csv'

class Birds(Resource):
    def get(self):
        data = pd.read_csv(birds_path)
        birds_data = data.to_dict()
        return(birds_data)
api.add_resource(Birds,'/birds')        


@app.route('/search-birds', methods=['GET', 'POST'])
def search_birds():
    # handle the POST request
    if request.method == 'POST':
        power = request.form.get('power')
        habitat = request.form.get('habitat')
        wingspan = request.form.get('wingspan')
        data = pd.read_csv(birds_path)
        sel_data = data.loc[(data['power_type'] == str(power)) & (data['habitat_count'] == int(habitat)) & (data['wingspan']== int(wingspan))]
        sel_data = sel_data.to_dict()
        bird = sel_data['bird_name']
        

        return '''
                  <h1>The power type for the bird is: {}</h1>
                  <h1>The number of habitats for the bird is: {}</h1>
                  <h1>The wingspan of the bird is: {}</h1>
                  <h1>The bird corresponding to this combination is: {}</h1>'''.format(power, habitat, wingspan, bird)

    # otherwise handle the GET request
    return '''
           <form method="POST">
                <p>Choose your Power Type </p>
               <div><label>Activated <input type="radio" name="power", value ="Activated" ></label></div>
               <div><label>Between Turns <input type="radio" name="power", value ="Between turns" ></label></div>
               <div><label>Played <input type="radio" name="power", value ="Played" ></label></div>
               <div><label>Round Ended <input type="radio" name="power", value ="Round Ended" ></label></div>
               <div><label>None <input type="radio" name="power", value ="None" ></label></div>
               <p>Choose your Habitat Count (Select a number from 1 to 3) </p>
               <div><label>Habitat: <input type="text" name="habitat"></label></div>
               <p>Choose your Wingspan value (Select a number from 9 to 276) </p>
               <div><label>Wingspan: <input type="text" name="wingspan"></label></div>
               <input type="submit" value="Submit">
           </form>'''




if __name__ == '__main__':
    app.run(host='localhost', debug=True)