import pandas as pd
import datetime
import time
import pickle
import numpy as np

class ModelHelper():
    def __init__(self):
        pass

    def makePredictions(self, Family_status, gender, Education_type, Housing_type):
        gender = 0

        family_status_civil_marriage = 0
        family_status_married = 0
        family_status_separated	 = 0
        family_status_single = 0
        family_status_widow = 0
        
        education_academic_degree = 0
        education_higher_education = 0
        education_incomplete_higher = 0
        education_lower_secondary = 0
        education_secondary = 0
        
        housing_type_co_op_apartment = 0
        housing_type_house_apartment = 0
        housing_type_municipal_apartment = 0
        housing_type_office_apartment = 0
        housing_type_rented_apartment = 0
        housing_type_with_parents = 0
        
        # parse gender
        if (gender == "female"):
            gender = 0
        elif (gender == "male"):
            gender = 1
        else:
            pass

        # parse family status
        if (Family_status == "Civil Marriage"):
            family_status_civil_marriage = 1
        elif (Family_status == "Married"):
            family_status_married = 1
        elif (Family_status == "Separated"):
            family_status_separated = 1
        elif (Family_status == "Single"):
            family_status_single = 1
        elif (Family_status == "Widow"):
            family_status_widow = 1
        else:
            pass
        
        # parse education
        if (Education_type == "Academic Degree"):
            education_academic_degree = 1
        elif (Education_type == "Higher Education"):
            education_higher_education = 1
        elif (Education_type == "Incomplete Higher Education"):
            education_incomplete_higher = 1
        elif (Education_type == "Lower Secondary"):
            education_lower_secondary = 1
        elif (Education_type == "Secondary"):
            education_secondary = 1
        else:
            pass
        
        # parse housing type
        if (Housing_type == "Co-op Apartment"):
            housing_type_co_op_apartment = 1
        elif (Housing_type == "House"):
            housing_type_house_apartment = 1
        elif (Housing_type == "Municipal apartment"):
            housing_type_municipal_apartment = 1
        elif (Housing_type == "Office apartment"):
            housing_type_office_apartment = 1
        elif (Housing_type == "Rented apartment"):
            housing_type_rented_apartment = 0
        elif (Housing_type == "Living with parents"):
            housing_type_with_parents = 0
        else:
            pass

        input_pred = [[gender, housing_type_co_op_apartment, housing_type_house_apartment, housing_type_municipal_apartment, housing_type_office_apartment, housing_type_rented_apartment, housing_type_with_parents, family_status_civil_marriage, family_status_married, family_status_separated, family_status_single, family_status_widow, education_academic_degree, education_higher_education, education_incomplete_higher, education_lower_secondary, education_secondary]]


        filename = 'finalized_model.sav'
        lr_load = pickle.load(open(filename, 'rb'))

        X = np.array(input_pred)
        preds = lr_load.predict_proba(X)
        preds_singular = lr_load.predict(X)

        return preds_singular[0]
