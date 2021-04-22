import cx_Oracle
import mybatis_mapper2sql

class DaoMember:
    def __init__(self):
        self.conn = cx_Oracle.connect('team3/java@192.168.41.24:1521/xe')
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_member.xml')[0]
            
    def kakao_join(self, mem_id, mem_name, mem_mail, mem_job, dday_title):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "kakao_merge")        
        self.cs.execute(sql, (mem_id, mem_name, mem_id, mem_id, mem_name, mem_mail, mem_job, dday_title, mem_id))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
        
    def counter(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "member_cnt")
        rs = self.cs.execute(sql)
        list = []
        for record in rs:
            return record[0]
        
    def dupl_id(self,mem_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_dupl_id")
        rs = self.cs.execute(sql, (mem_id,))
        list = []
        for record in rs:
            list.append({'mem_id':record[0],'mem_pass':record[1],'mem_mail':record[2]})
        return list
    
    def dupl_email(self, mem_mail):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_dupl_email")
        rs = self.cs.execute(sql, (mem_mail,))
        list = []
        for record in rs:
            list.append({'mem_id':record[0],'mem_name':record[1],'mem_mail':record[2]})
        return list

    def login(self, mem_id, mem_pass):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_login")
        rs = self.cs.execute(sql, (mem_id, mem_pass))
        list = []
        for record in rs:
            list.append({'mem_id':record[0],'mem_name':record[1],'mem_pass':record[2],'mem_mail':record[3],'mem_job':record[4],'dday_title':record[5],'dday_date':record[6],'del_yn':record[7]})
        return list
    
    def select_mypage(self, mem_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_mypage")
        rs = self.cs.execute(sql,(mem_id,))
        list = []
        for record in rs:
            list.append({'mem_id':record[0],'mem_name':record[1],'mem_pass':record[2],'mem_mail':record[3],'mem_job':record[4],'dday_title':record[5],'dday_date':record[6],'in_date':record[7]})
        return list
    
    def select_mydday_title(self, mem_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_mydday_title")
        rs = self.cs.execute(sql, (mem_id,))
        obj = None
        for record in rs:
            obj = {record[0]}
        return obj
    
    def select_mydday_date(self, mem_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_mydday_date")
        rs = self.cs.execute(sql, (mem_id,))
        obj = None
        for record in rs:
            obj = {record[0]}
        return obj
    
    def select(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select")
        rs = self.cs.execute(sql)
        list = []
        for record in rs:
            list.append({'mem_id':record[0],'mem_name':record[1],'mem_mail':record[3],'mem_job':record[4],'dday_title':record[5],'dday_date':record[6],'del_yn':record[7],'in_date':record[8]})
        return list
 
    def set_temp_pass(self, temp_pass, mem_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "set_temp_pass")
        self.cs.execute(sql, (temp_pass, mem_id, mem_id))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt

    def insert(self, mem_id, mem_name, mem_pass, mem_mail, mem_job, dday_title, dday_date):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")
        self.cs.execute(sql, (mem_id, mem_name, mem_pass, mem_mail, mem_job, dday_title, dday_date, mem_id, mem_id))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt

    def update(self, mem_id, mem_name, mem_pass, mem_mail, mem_job, dday_title, dday_date):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update")        
        self.cs.execute(sql, (mem_name, mem_pass, mem_mail, mem_job, dday_title, dday_date, mem_id, mem_id))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    def update_mod(self, mem_id, mem_name, mem_mail, mem_job):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update_mod")        
        self.cs.execute(sql, (mem_name, mem_mail, mem_job, mem_id))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    def delete(self,mem_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "delete")  
        self.cs.execute(sql, (mem_id,))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    def user_yn(self,mem_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "user_yn")  
        self.cs.execute(sql, (mem_id,))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    def user_act(self,mem_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "user_act")  
        self.cs.execute(sql, (mem_id,))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
        
    def __del__(self): 
        self.cs.close()
        self.conn.close()