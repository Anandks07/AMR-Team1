# AMR-Team1

The application allows user to analyse the OHLC time series for the entire period as well as has the ability to filter the OHLC time-series on the basis of symbols and the data pertaining to year and month. An option to view the history of the filtering requests is also provided. The history is stored in an array.

The application primarily uses the Dash framework in python.

## Prerequisites

It is neccessary that dash has to be installed in the system. Dash can be installed using:    
` pip3 install dash`

For further queries regarding installation, click [here](https://dash.plotly.com/installation)

The app reads the data from a .csv file. The given json file was converted to a .csv file and the same can be found as NT.csv in the repository.

## Instructions to run the solution
- Install dash from the link given above or using command line.
- Download the app.py and NT.csv file. 
- Make sure that the NT.csv file as well as app.py are in the same directory, else add the path to NT.csv in line 10 of app.py
- Run the python script.
