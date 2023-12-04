import json
import pickle
import numpy as np

# global var to store data from artifacts sub-dir , json file
__locations = None
__model = None
__data_columns = None



def load_saved_artifacts() : # loading the columns json file ( that has locations)
    print("Loading artifacts like loc and model params")
    global __locations
    global __data_columns
    global __model

    with open("./artifacts of ML model/column.json" , "r") as f :
        __data_columns = json.load(f)["data_columns "] # now , json will load here a dictionary of columns and acees that dict key using dict[key]
        # the value associated with "data columns" key is a list of values where from index=3 , loc name start .
        __locations = __data_columns[3:] # all the location features loaded

        # load model params
    with open("./artifacts of ML model/code.pickle" , "rb") as f :
        __model = pickle.load(f)
    #print(__model)
    #print(__locations)
# to get predicted value from model , unpickle the file of model and call .predict method on it model.predict(2D numpy array)
def predicted_price(location , total_sqft , bhk , bath) :
    try :

        loc_index = __data_columns.index(location.lower())
    except :
        loc_index = -1
    # make a sample data point from gven input same form as X
    x = np.zeros(len(__data_columns))
    x[0] = total_sqft
    x[1] = bath
    x[2] = bhk
     # this wre a doing because we have one-hot encoding where all location are colummns of df where correct loc = 1
    # and rest are 0 , so search that loc from loc_columns and put it at 1 (if index>0)  and pass this whole data column size data point
    # as a feature for prediction .
    if loc_index>=0 :
        x[loc_index] =1
    return round(__model.predict([x])[0] , 2)  # prediction done only when given input is 2D array

# to use a global var inside fucnt , first define outside normally and inside function using 'global' keyword
def get_location_name() :
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == "__main__" :
    load_saved_artifacts()
    get_location_name()
    print(predicted_price('2nd stage nagarbhavi' , 1000 , 2 , 2))
    print(get_location_name())

    print("util is running")


# in python , the order in which functions are defined , does not matter
