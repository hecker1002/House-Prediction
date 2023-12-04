# Here , we build the backend ( deployment server) for our web app using Flask
# for server - make 2 files (server.py) and (utils.py)
# server.py - takes http request and defines what function to run at diff path
# utils.py - working part , which unpickles the model and does actual predictions
# and use utils inside server by importing it as , import util -> util.function(x) -> jsonify({response from util })
from flask import Flask , request , jsonify , render_template , url_for
import util

# make an instance of the class Flask

app = Flask(__name__)

# Use @app.route(pathWITHBACKSLASH) - to decide a path  requested by user (url) , what info should be sent back to user (on client browser)
# and below it , write the function which runs after http req has been accepted .
# Path we give (as user) is combined with domain name by defaut , so write code corresponding to path ONLY .

# in flask , jsonify function - takes a Python dict. and converts it into a JSON formatted object and
# #( to be used easily across all web broswers) sends it as a response back to user on client side web browser .
@app.route("/get_location_name" , methods = ['GET'])
def get_location_name() :
    response = jsonify({
        'location' : util.get_location_name()
    }) # util.py is a file that loads the model params. and name of locations
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/predict_home_price" , methods = ['GET' , 'POST']) # post method helps to do a form submission to flask server
def prediction() :
    # take the inputs FORM (from user) - use request.form[var]

    total_sqft =float(request.form['total_sqft']) #form contains incoming info. from user to flask server , so categorise it .
    location = request.form['location']
    bhk =int(request.form['bhk'])
    bath =int(request.form['bath'])

    data = jsonify({
        "estimated_price" : util.predicted_price(location , total_sqft ,bhk , bath)
    })
    data.headers.add('Access-Control-Allow-Origin', '*')
    return data # from flask server in form of JSON obj (which takes a dict)


# run the flask file (server) when user gives a url (route)

# In flask file , run all the functions (required) to do the job , which are unpickling and storing data .
if __name__ == "__main__" :
    print("Flask deployment server is running for House prediction model .")
    util.load_saved_artifacts()
    x = util.get_location_name()
    print(x)
    app.run(debug = True )

# AFter running , take the url ( domain name) and attach with it the path you want to go to .
# Flask will combine the (domain name + path)
# and send you to correct posn .

# Now , make a UI application based software for user through which they can send info. to server .
