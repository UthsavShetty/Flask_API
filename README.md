### Objective
1. To modify the given API to handle exceptions and to ensure that unreasonable inputs are handled appropriately
2. Given a list of houses with (x,y) coordinates of their respective plots, add a query API method to the script above that returns all houses whose plots are contained entirely with an input polygon

### Directions
1. Clone this repo

2. Run requirements.txt file 
> pip install -r requirements.txt

3. Run app.py script so both modules gets loaded 
> app>python app.py

4. Post the link on POSTMAN with valid JSON inputs
> GET - http://localhost:5000/houseprice

> {

    "GrLivArea" : "0",
    
    "TotalBsmtSF" : "0",
    
    "GarageArea" : "0",
    
    "YearBuilt" : "0"
> }

5. Post the link on POSTMAN with valid JSON inputs
> GET -  http://localhost:5000/houselookup

> {
    "x1" : "50",
    "y1" : "30",
    "x2" : "57.50",
    "y2" : "34",
    "x3" : "62",
    "y3" : "39",
    "x4" : "65.5",
    "y4" : "31.5",
    "x5" : "60.25",
    "y5" : "27.5",
    "x6" : "58",
    "y6" : "24.87",
    "x7" : "50",
    "y7" : "30"
}
