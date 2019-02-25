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

#### Pre-requisites
```
pip install flask
pip install flask-restful
```

#### Some of the tools in use:
- AWS https://aws.amazon.com/  (EC2, S3, RDS, Lambda, DynamoDB)
- Cloudformation https://aws.amazon.com/cloudformation/
- Python https://www.python.org/
- Docker https://www.docker.com/
- Ansible http://docs.ansible.com/
- Serverless https://serverless.com/

