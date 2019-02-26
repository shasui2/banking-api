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

#### Flask Api Pre-requisites
```
pip install flask
pip install flask-restful
```


#### Serverless Pre-requisites
```
npm install serverless-offline --save-dev
npm install --save serverless-dynamodb-local@0.2.35
sls dynamodb install
```
