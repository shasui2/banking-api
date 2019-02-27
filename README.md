## Python Bank App
#### Overview
A bank app which satisfies the following acceptance criteria:
```
Given a client makes a deposit of 1000 on 10-01-2012
And a deposit of 2000 on 13-01-2012
And a withdrawal of 500 on 14-01-2012
When she prints her bank statement
Then she would see
date || credit || debit || balance
14/01/2012 || || 500.00 || 2500.00
13/01/2012 || 2000.00 || || 3000.00
10/01/2012 || 1000.00 || || 1000.00
```
#### My Thoughts and Processes
My prior experience with python, serverless and dynamodb was almost nonexistent before doing this 
project. As a result, a lot of the issues I faced were simply to to unfamiliarity with the language.
For example, the code not being as dry as I would like it to be (see parsers in endpoints.py etc.).

After reading through versions 1, 2 and 3 I immediately set out to create an api rather than 
a console application. I employed the use of flask-restless to do this and an sqlite3 database. 
After doing this I dockerised the application to ensure that it would run under the same conditions 
anywhere. I created unit tests using tavern which provided an easy to read and maintainable 
structure.

It was at this point that I then started to look into serverless and dynamodb and realised that 
my existing structure would not really play nice with either of them. So I created the 
serverless_endpoints directory to utilise existing DB_Helper logic but in a serverless style.
My attempt to implement this was purely local and not via aws. It is only intended to be proof
of concept rather than a fully working implementation i.e. dynamodb is not actually used. 
This was done due to time constraints as I have limited availability going forward. 


#### Flask Api Pre-requisites
```
docker-compose up --build
```

The container can be accessed via ```localhost:5000/<endpoint>```.

Endpoints available:
- /account
- /deposit
- /withdraw
- /transactions

To run the unit tests:
```
docker-compose up -d
cd tests/
pytest
```

#### Serverless Pre-requisites
I managed to get serverless to run locally by doing the following:
```
npm install serverless-offline --save-dev
npm install --save serverless-dynamodb-local@0.2.35
sls dynamodb install
```

To start the server:
```
npm run dev
```

End point address: ```http://127.0.0.1:3000/<endpoint>```
