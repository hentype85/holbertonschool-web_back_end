# NoSQL

## MongoDB

[Official installation guide](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/ "Official installation guide")


Potential issue if documents creation doesn’t work or this error: Data directory /data/db not found., terminating (source and source)
```
$ sudo mkdir -p /data/db
```

start server:
```
mongod
```

other tab:
```
mongo
```

```
cat 0-list_databases | mongo
cat 2-insert | mongo my_db
cat 3-all | mongo my_db
cat 4-match | mongo my_db
cat 5-count | mongo my_db
cat 6-update | mongo my_db
cat 7-delete | mongo my_db
```
```
./8-main.py
./9-main.py
./10-main.py
./11-main.py
```
```
curl -o dump.zip -s "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-webstack/411/dump.zip"
unzip dump.zip
mongorestore dump
./12-log_stats.py
```