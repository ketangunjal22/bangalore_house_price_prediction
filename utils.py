import pandas as pd
import numpy as np
import pickle
import json
import config


class HousePricePrediction:

    def __init__(self):
        print("Init Function")

    def load_saved_data(self):
        with open(config.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)
            
        with open(config.JSON_FILE_PATH, 'r') as f:
            self.column_names = json.load(f)['data_columns']
        
    def get_location_names(self):
        self.load_saved_data()
        
        locations = self.column_names[3:]
        print("locations :",locations)

        return locations


    def get_house_price(self,location, sqft, bath, bhk):
        self.load_saved_data()
        test_array = np.zeros(self.model.n_features_in_, int)

        index = self.column_names.index(location)
        print("Index is :",index)
        test_array[0] = sqft
        test_array[1] = bath
        test_array[2] = bhk
        test_array[index] = 1

        price = np.around(self.model.predict([test_array])[0],3)
        print(f"Predicted House price is : {price} Lakh")
        return price


if __name__ == "__main__":
    hpp = HousePricePrediction()
    hpp.get_location_names()