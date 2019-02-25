## Python Bank App
#### Overview
Create a bank app which satisfies the following acceptance criteria:
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


```
$ python
Python 3.6.7 (default, Nov 26 2018, 15:05:20) 
[GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.10.44.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> bank = Bank(100)
>>> bank.deposit(50)
```


*Note: This is only for illustrating how you can have an interactive python console.*
*Please feel free to use different names for Classes/objects/functions* 

#### Some of the tools we use
- AWS https://aws.amazon.com/  (EC2, S3, RDS, Lambda, DynamoDB)
- Cloudformation https://aws.amazon.com/cloudformation/
- Python https://www.python.org/
- Docker https://www.docker.com/
- Ansible http://docs.ansible.com/
- Serverless https://serverless.com/

Notes: 
- Fork this project and make it as a private repo while you are working on it.
- Make sure we can access your repo by adding us as collaborators to your project. 
- You will have the opportunity to tell us about your reasoning, process and choice of tools during your interview. We are as interested in what you’ve built as we are in how you built it and why!

Good luck!
