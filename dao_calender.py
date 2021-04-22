import cx_Oracle
import mybatis_mapper2sql

class DaoCalender:
    def __init__(self):
        self.conn = cx_Oracle.connect('team3/java@192.168.41.24:1521/xe')
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_calender.xml')[0]
    
    def select_myplan(self, mem_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_myplan")
        rs = self.cs.execute(sql,(mem_id,))
        list = []
        for record in rs:
            list.append({'plan_seq':record[0],'plan_title':record[1],'plan_content':record[2],'plan_date':record[3][0:8],'in_user_id':record[4]})
        return list
    
    def select_detail(self, plan_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_detail")
        rs = self.cs.execute(sql,(plan_seq,))
        list = []
        for record in rs:
            list.append({'plan_seq':record[0],'plan_title':record[1],'plan_content':record[2],'plan_date':record[3][0:8],'in_user_id':record[4]})
        return list
 
    def insert(self, plan_title, plan_content, plan_date, in_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")
        self.cs.execute(sql, (plan_title, plan_content, plan_date, in_user_id, in_user_id))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
 
    def update(self, mem_id, plan_seq, plan_title, plan_content):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update")        
        self.cs.execute(sql, (plan_title, plan_content, mem_id, plan_seq, mem_id))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    def delete(self, plan_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "delete")  
        self.cs.execute(sql, (plan_seq,))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
        
    def __del__(self): 
        self.cs.close()
        self.conn.close()