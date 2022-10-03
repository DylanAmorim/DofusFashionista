# Prerequisites

## Python 2.7.18

````bash
sudo apt-get update
sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

cd /usr/src
wget https://www.python.org/ftp/python/2.7.18/Python-2.7.18.tgz

sudo tar xzf Python-2.7.18.tgz

cd Python-2.7.18
sudo ./configure --enable-optimizations
sudo make install 
````
(make altinstall can be used to prevent replacing the default python binary file /usr/bin/python instead)

## pip 20.3.4

You can get get-pip.py for a specific version of pip.

I did :

````bash
curl https://bootstrap.pypa.io/pip/3.4/get-pip.py -o get-pip.py 
````

but I let the file inside my project if needed, then use this command :

````bash
python ./get-pip.py
````
## Mysql

````bash
sudo apt install mysql-server
sudo service mysql start
````

## Other packages you can be missing
```bash
sudo apt-get install libmysqlclient-dev
sudo apt-get install sqlite3 libsqlite3-dev
# sudo apt-get install python-dev -> if fatal error: Python.h: No such file or directory
# sudo wget https://raw.githubusercontent.com/paulfitz/mysql-connector-c/master/include/my_config.h -O /usr/include/mysql/my_config.h -> if fatal error: my_config.h: No such file or directory
```

# dofusfashionista
The Dofus Fashionista, an equipment advisor for Dofus

## Install and Run Fashionista:
````bash
git clone https://github.com/DylanAmorim/DofusFashionista.git fashionista  
eval echo 'export PYTHONPATH=$(pwd)/fashionista/fashionistapulp' >> ~/.bashrc  
chmod 777 fashionista  
chmod 777 fashionista/fashionistapulp/fashionistapulp  
cd fashionista  
sudo ./configure_fashionista_root.py -i -s -d  
sudo ./configure_fashionista.py  
sudo ./run_fashionista.sh  
````

Caution : No capital letter in PYHTONPATH value

# Reference

This is a fork of https://github.com/PiwiSlayer/DofusFashionista.git