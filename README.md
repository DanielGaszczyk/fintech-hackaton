#SenZen  
##This repository contains back-end part of SenZen application for TH.0 FinTech Hackathon.  
We use development environment based on Heroku, with address floating-woodland-93585.herokuapp.com

Available endpoints:  
**GET** https://floating-woodland-93585.herokuapp.com/stockdata - returns sample stock data (*Apple and Google*)  
**POST** https://floating-woodland-93585.herokuapp.com/login  - *{'login': 'user1', 'password': 'password1'}* - Login  
**POST** https://floating-woodland-93585.herokuapp.com/register - *{'login': 'user1', 'password': 'password1'}* - Creating an account  

Endpoints with calculations:  
**POST** https://floating-woodland-93585.herokuapp.com/vad - Future value with annual deposits  
`curl -X POST -H "Content-Type: application/json" -d '{"c0": 5.0, "r": 2.0, "time": 1}' https://floating-woodland-93585.herokuapp.com/vad` - Sample *curl* command  
Requires:  
* c0  
* r  
* time  

**POST** https://floating-woodland-93585.herokuapp.com/varlog - Variance  
Requires:  
* p  
* initial  
* mu  
* sigma  
* time  

**POST** https://floating-woodland-93585.herokuapp.com/varnormal  - Normal variance  
Requires:  
* p
* initial   
* mu  
* sigma  

**POST**  https://floating-woodland-93585.herokuapp.com/simulatestock - List of predicted future values  
Requires:  
* s0  
* sigma  
* mu  
* time  
