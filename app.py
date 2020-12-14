from flask import *
import pickle
import numpy as np
import pickle
import pandas as pd

app=Flask(__name__)
model=pickle.load(open('flight.pkl','rb'))
@app.route('/')

def Home():
	return render_template('index.html')

@app.route("/predict", methods = ["POST"])

def predict():

        # Date_of_Journey
    date_dep = request.form["departure_date"]
    Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
    Journey_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
    Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
    Dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
    date_arr = request.form["arrival_date"]
    Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
    Arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
    dur_hour = abs(Arrival_hour - Dep_hour)
    dur_min = abs(Arrival_min - Dep_min)
    Total_stops = int(request.form["stops"])
    Airline=request.form['airline']
    if(Airline=='Jet Airways'):
         Jet_Airways = 1
         IndiGo = 0
         Air_India = 0
         Multiple_carriers = 0
         SpiceJet = 0
         Vistara = 0
         GoAir = 0
         Multiple_carriers_Premium_economy = 0
         Jet_Airways_Business = 0
         Vistara_Premium_economy = 0
         Trujet = 0 

    elif (Airline=='IndiGo'):
        Jet_Airways = 0
        IndiGo = 1
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0 

    elif (Airline=='Air India'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 1
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0 
            
    elif (Airline=='Multiple carriers'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 1
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0 
            
    elif (Airline=='SpiceJet'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 1
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0 
            
    elif (Airline=='Vistara'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 1
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (Airline=='GoAir'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 1
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (Airline=='Multiple carriers Premium economy'):
        Jet_Airways = 0
        IndiGo = 0 
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 1
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (Airline=='Jet Airways Business'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 1
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (Airline=='Vistara Premium economy'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 1
        Trujet = 0
            
    elif (airline=='Trujet'):
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 1

    else:
        Jet_Airways = 0
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Jet_Airways_Business = 0
        Vistara_Premium_economy = 0
        Trujet = 0

        # print(Jet_Airways,
        #     IndiGo,
        #     Air_India,
        #     Multiple_carriers,
        #     SpiceJet,
        #     Vistara,
        #     GoAir,
        #     Multiple_carriers_Premium_economy,
        #     Jet_Airways_Business,
        #     Vistara_Premium_economy,
        #     Trujet)


        # Source
        # Banglore = 0 (not in column)
    Source = request.form["Source"]
    if (Source == 'Delhi'):
        Delhi = 1
        Kolkata = 0
        Mumbai = 0
        Chennai = 0

    elif (Source == 'Kolkata'):
        Delhi = 0
        Kolkata = 1
        Mumbai = 0
        Chennai = 0

    elif (Source == 'Mumbai'):
        Delhi = 0
        Kolkata = 0
        Mumbai = 1
        Chennai = 0

    elif (Source == 'Chennai'):
        Delhi = 0
        Kolkata = 0
        Mumbai = 0
        Chennai = 1

    else:
        Delhi = 0
        Kolkata = 0
        Mumbai = 0
        Chennai = 0

        # print(s_Delhi,
        #     s_Kolkata,
        #     s_Mumbai,
        #     s_Chennai)

        # Destination
        # Banglore = 0 (not in column)
    Destination = request.form["Destination"]
    if (Destination == 'Cochin'):
        Cochin = 1
        Delhi = 0
        New_Delhi = 0
        Hyderabad = 0
        Kolkata = 0
        
    elif (Destination == 'Delhi'):
        Cochin = 0
        Delhi = 1
        New_Delhi = 0
        Hyderabad = 0
        Kolkata = 0

    elif (Destination == 'New_Delhi'):
        Cochin = 0
        Delhi = 0
        New_Delhi = 1
        Hyderabad = 0
        Kolkata = 0

    elif (Destination == 'Hyderabad'):
        Cochin = 0
        Delhi = 0
        New_Delhi = 0
        Hyderabad = 1
        Kolkata = 0

    elif (Destination == 'Kolkata'):
        Cochin = 0
        Delhi = 0
        New_Delhi = 0
        Hyderabad = 0
        Kolkata = 1

    else:
        Cochin = 0
        Delhi = 0
        New_Delhi = 0
        Hyderabad = 0
        Kolkata = 0

        # print(
        #     d_Cochin,
        #     d_Delhi,
        #     d_New_Delhi,
        #     d_Hyderabad,
        #     d_Kolkata
        # )
        

    #     ['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour',
    #    'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours',
    #    'Duration_mins', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
    #    'Airline_Jet Airways', 'Airline_Jet Airways Business',
    #    'Airline_Multiple carriers',
    #    'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
    #    'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
    #    'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
    #    'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
    #    'Destination_Kolkata', 'Destination_New Delhi']
        
    prediction=model.predict([[
        Total_stops,
        Journey_day,
        Journey_month,
        Dep_hour,
        Dep_min,
        Arrival_hour,
        Arrival_min,
        dur_hour,
        dur_min,
        Air_India,
        GoAir,
        IndiGo,
        Jet_Airways,
        Jet_Airways_Business,
        Multiple_carriers,
        Multiple_carriers_Premium_economy,
        SpiceJet,
        Trujet,
        Vistara,
        Vistara_Premium_economy,
        Chennai,
        Delhi,
        Kolkata,
        Mumbai,
        Cochin,
        Delhi,
        Hyderabad,
        Kolkata,
        New_Delhi
        ]])

    output=round(prediction[0],2)

    return render_template("index.html",result="Your Flight price is Rs. {}".format(output))




if __name__ == "__main__":
    app.run(debug=True)