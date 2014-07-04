consultation_crowsourcing
=========================

Crowdsource answer to copyright consultation


* Easy test the public dir as webserver
 - to test the basic task interface on http://localhost:8989/task.html
```bash
    cd public
    python -m SimpleHTTPServer 8989
```


* Install and initiate the instance
 - install prerequisite (on debian/ubuntu)
```bash
    sudo apt-get install python-virtualenv libmysqlclient-dev
    sudo apt-get install mysql-server
```


 - create a virtualenv

```bash
    cd install
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt
```

 - Creation of mysql user
Here the password would be 'tester', please change it

```bash
    mysql -uroot -p
    mysql> create database crowdsourcingdb; 
    mysql> grant usage on *.* to cs_user@localhost identified by 'tester';
    mysql> grant all privileges on crowdsourcingdb.* to cs_user@localhost ;
    mysql> exit;
```

 - Set the config file
Copy the template config file and edit it for mysql access

```bash
    cp config.py.template config.py
    nano config.py
```
