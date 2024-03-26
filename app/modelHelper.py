import pandas as pd
import datetime
import time
import pickle
import numpy as np

class ModelHelper():
    def __init__(self):
        pass

    def makePredictions(self, Gender, Own_car, Own_property, Unemployed, Num_children,
                       Num_family, Account_length, Total_income, Age, Years_employed, Income_type, 
                        Education_type, Family_status, Housing_type, Occupation_type):

        income_type_commercial_associate = 0
        income_type_pensioner = 0
        income_type_state_servant = 0
        income_type_student = 0
        income_type_working = 0
        
        education_academic_degree = 0
        education_higher_education = 0
        education_incomplete_higher = 0
        education_lower_secondary = 0
        education_secondary = 0
        
        family_status_civil_marriage = 0
        family_status_married = 0
        family_status_separated	 = 0
        family_status_single = 0
        family_status_widow = 0
        
        housing_type_co_op_apartment = 0
        housing_type_house_apartment = 0
        housing_type_municipal_apartment = 0
        housing_type_office_apartment = 0
        housing_type_rented_apartment = 0
        housing_type_with_parents = 0
        
        occupation_type_accountants = 0
        occupation_type_cleaning_staff = 0
        occupation_type_cooking_staff = 0
        occupation_type_core_staff = 0
        occupation_type_drivers = 0
        occupation_type_high_skill_tech_staff = 0
        occupation_type_laborers = 0
        occupation_type_managers = 0
        occupation_type_medicine_staff = 0
        occupation_type_other = 0
        occupation_type_sales_staff = 0
        occupation_type_security_staff = 0
        
        # parse income type
        if (Income_type == "Commercial Associate"):
            income_type_commercial_associate = 1
        elif (Income_type == "Pensioner"):    
            income_type_pensioner = 1
        elif (Income_type == "State Servant"):    
            income_type_state_servant = 1
        elif (Income_type == "Student"):  
            income_type_student = 1
        elif (Income_type == "Working"):    
            income_type_working = 1
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
            housing_type_rented_apartment = 1
        elif (Housing_type == "Living with parents"):
            housing_type_with_parents = 1
        else:
            pass
        
        #parse occupation type
        if (Occupation_type == "Accountant"):
            occupation_type_accountants = 1
        elif (Occupation_type == "Cleaner"):
            occupation_type_cleaning_staff = 1
        elif (Occupation_type == "Cooking"):
            occupation_type_cooking_staff = 1
        elif (Occupation_type == "Core Staff"):
            occupation_type_core_staff = 1
        elif (Occupation_type == "Driver"):
            occupation_type_drivers = 1
        elif (Occupation_type == "High Skill Tech"):
            occupation_type_high_skill_tech_staff = 1
        elif (Occupation_type == "Laborer"):
            occupation_type_laborers = 1
        elif (Occupation_type == "Manager"):
            occupation_type_managers = 1
        elif (Occupation_type == "Medicine"):
            occupation_type_medicine_staff = 1
        elif (Occupation_type == "Other"):
            occupation_type_other = 1
        elif (Occupation_type == "Sales"):
            occupation_type_sales_staff = 1
        elif (Occupation_type == "Security"):
            occupation_type_security_staff = 1
        else:
            pass

        input_pred = [[Gender, Own_car, Own_property, Unemployed, Num_children, Num_family, Account_length, 
                       Total_income, Age, Years_employed, income_type_commercial_associate, income_type_pensioner, 
                       income_type_state_servant, income_type_student, income_type_working, education_academic_degree, 
                       education_higher_education, education_incomplete_higher, education_lower_secondary, education_secondary, 
                       family_status_civil_marriage, family_status_married, family_status_separated, family_status_single,
                       family_status_widow, housing_type_co_op_apartment, housing_type_house_apartment, housing_type_municipal_apartment, 
                       housing_type_office_apartment, housing_type_rented_apartment, housing_type_with_parents, occupation_type_accountants,
                       occupation_type_cleaning_staff, occupation_type_cooking_staff, occupation_type_core_staff, occupation_type_drivers,
                       occupation_type_high_skill_tech_staff, occupation_type_laborers, occupation_type_managers, occupation_type_medicine_staff,
                       occupation_type_other, occupation_type_sales_staff, occupation_type_security_staff]]

        filename = 'final_model.h5'
        lr_load = pickle.load(open(filename, 'rb'))

        X = np.array(input_pred)
        preds = lr_load.predict_proba(X)[0]
        preds_singular = lr_load.predict(X)

        rtn = {"prob_low_risk": preds[0],
          "prob_high_risk": preds[1],
          "loan_pred": "high_risk" if preds_singular[0] == 1 else "low_risk"}
        
        return rtn
