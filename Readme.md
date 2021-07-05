# Chronicle

database and migrations inside the project, to speed up the review


before start application install dependencies with command:

`pip install -r requirements.txt`


after that configure flask:


`$ export FLASK_APP=api`

`$ export FLASK_ENV=development`

`$ flask run`

now you can visit apps url :
 _**http://127.0.0.1:5000/**_


response preview:
`
  

    {
    "chronicle_events": [
      0, 
      1, 
      1, 
      1
    ], 
    "max_timestamp": "Sun, 25 Jul 2021 17:32:47 GMT", 
    "min_timestamp": "Mon, 05 Jul 2021 14:57:01 GMT", 
    "source": "440ASi", 
    "status": "Open", 
    "unique_id": 1
    }
  `