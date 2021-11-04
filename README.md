# movie-api
API using Python Backend with React Frontend

Building this out based on the tutorial by Pretty Printed and Ben Awad [1] [2]

In order to run Flask backend-    
1. Run the following commands to run flask app-    
    a. export FLASK_APP=api   
    b. export FLASK_DEBUG=1 #For running app in debug mode   
2. Create a test db   
    a. In api directory, start a python shell
    b. Use the following commands to create db-  
        i. from api.models import Movie   
        ii. from api import db, create_app 
        iii. db.create_all(app=create_app())      
3. Test routes using POSTMAN  

In order to run React frontend-
1. Download semantic UI using the following-    
    i. npm i semantic-ui-react semantic-ui-css    
2. Start app using the following-    
    i. npm start    

References
[1] Ben Awad, React Frontend https://www.youtube.com/watch?v=06pWsB_hoD4
[2] Pretty Printed, Flask Backend https://www.youtube.com/watch?v=Urx8Kj00zsI&t=0s


