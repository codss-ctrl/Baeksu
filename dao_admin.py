import cx_Oracle
import mybatis_mapper2sql

class DaoAdmin:
    def __init__(self):
        self.conn = cx_Oracle.connect('team3/java@192.168.41.24:1521/xe')
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_admin.xml')[0]
    
    def login(self, admin_id, admin_pass):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_login")
        rs = self.cs.execute(sql, (admin_id, admin_pass))
        list = []
        for record in rs:
            list.append({'admin_id':record[0],'admin_pass':record[1]})
        return list

    def select(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select")
        rs = self.cs.execute(sql)
        list = []
        for record in rs:
            list.append({'admin_id':record[0],'admin_pass':record[1]})
        return list
        
    def __del__(self): 
        self.cs.close()
        self.conn.close()