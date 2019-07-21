# coding=utf-8

#Default imports
import os
import sys
import sqlite3


class DBManager(object):
    """
    This class manage all operations over DB
    """


    _sql_create_table = """ CREATE TABLE `OompaLoompas` (
                            `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            `name`	TEXT NOT NULL,
                            `age`	INTEGER NOT NULL,
                            `job`	TEXT NOT NULL,
                            `height`	INTEGER NOT NULL,
                            `weight`	INTEGER NOT NULL,
                            `description`	TEXT NOT NULL
                        );"""


    # ========================================
    #               Constructor
    # ========================================

    def __init__(self,path):
        """
        In the beginning, it is checked if the database exists

        """
        self.db_path = os.path.join(os.getcwd(), path)

        if not os.path.exists(self.db_path):
            #If the database does not exist, we proceed to create it and create the necessary tables
            self._createTable()

    # ========================================
    #           Private Methods
    # ========================================

    def _connectDB(self):
        return sqlite3.connect(self.db_path)

    def _createTable(self):
        """
        If Local Db was created on runtime
        create tables needed

        :return: None
        """
        conn = self._connectDB()
        c = conn.cursor()
        c.execute(self._sql_create_table)

    # ========================================
    #           Public Methods
    # ========================================

    def InsertData(self, name, age, job, height, weight, description):
        """
        Try to insert data into a DB and return id primary key
        :return:
        """
        sql = '''INSERT INTO OompaLoompas(name,age,job,height,weight,description) VALUES(?,?,?,?,?,?)'''
        conn = self._connectDB()
        c = conn.cursor()
        c.execute(sql, (name, age, job, height, weight, description,))
        conn.commit()
        return int(c.lastrowid)


    def UpdateData(self, id, name, age, job, height, weight, description):
        """Try update data into DB"""
        sql = '''UPDATE OompaLoompas set name=?, age=?, job=?, height=?, weight=?, description=? where id = ?'''
        conn = self._connectDB()
        c = conn.cursor()
        c.execute(sql, (name, age, job, height, weight, description, id))
        conn.commit()


    def GetData(self, id=None):
        """
        Try to get data from DB

        :return:
        """

        if id is not None:
            sql = '''SELECT * from OompaLoompas where id = ?'''
        else:
            sql = '''SELECT * from OompaLoompas '''
        conn = self._connectDB()
        c = conn.cursor()

        if id is not None:
            query_result = c.execute(sql, (id,))
            for result in query_result.fetchall():
                return result
        else:
            query_result = c.execute(sql,)
            result_dict = []

        for result in query_result.fetchall():
           result_dict.append(result)

        return result_dict





