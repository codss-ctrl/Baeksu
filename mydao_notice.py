import cx_Oracle
import mybatis_mapper2sql

class MyDaonotice:
    def __init__(self):
        self.conn = cx_Oracle.connect('team3/java@192.168.41.24:1521/xe')
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_notice.xml')[0]
        
    def counter(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "notice_cnt")
        rs = self.cs.execute(sql)
        list = []
        for record in rs:
            return record[0]
        
    def myselect_list(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_list")
        rs = self.cs.execute(sql)
        list = []
        for record in rs:
            list.append({'notice_seq':record[0],'notice_title':record[1],'notice_content':record[2],'in_date':record[3][0:8],'in_user_id':record[4],'up_date':record[5],'up_user_id':record[6],'rnum':record[7]})
        return list
    
    def myselect(self,notice_seq): 
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select")
        rs = self.cs.execute(sql, (notice_seq,) )
        obj = None
        for record in rs:
            obj = {'notice_seq':record[0],'notice_title':record[1],'notice_content':record[2],'in_date':record[3][0:8],'in_user_id':record[4],'up_date':record[5],'up_user_id':record[6]}
        return obj
    
    def myinsert(self,notice_title, notice_content, in_date, in_user_id, up_date, up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")
        self.cs.execute(sql, (notice_title, notice_content, in_user_id, up_user_id,))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
        
    def myupdate(self,notice_seq,notice_title, notice_content, in_date, in_user_id, up_date, up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update")        
        self.cs.execute(sql, (notice_title, notice_content, up_user_id, notice_seq))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt

    def mydelete(self,notice_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "delete")  
        self.cs.execute(sql, (notice_seq,))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    def __del__(self): 
        self.cs.close()
        self.conn.close()