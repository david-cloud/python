import pymysql

# 告诉Django 用pymysql代替默认的MysqlDB
pymysql.install_as_MySQLdb()