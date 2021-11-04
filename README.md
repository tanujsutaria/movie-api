# movie-api
API using Python Backend with React Frontend

Building this out based on the tutorial by Pretty Printed and Ben Awad [1] [2]

In order to run flask backend-
1. Run the following commands to run flask app-
    a. export FLASK_APP=api
    b. export FLASK_DEBUG=1 #For running app in debug mode
2. Create a test db
    a. In api directory, start a python shell
    b. Use the following commands to create db-
        i. from api.models import Movie
        ii. from api import db, create_app
        iii. db.create_all(app=create_app())

References
[1] Ben Awad, React Frontend https://www.youtube.com/watch?v=06pWsB_hoD4
[2] Pretty Printed, Flask Backend https://www.youtube.com/watch?v=Urx8Kj00zsI&t=0s


