import cx_Oracle
import mybatis_mapper2sql

class DaoAfter:
    def __init__(self):
        self.conn = cx_Oracle.connect('team3/java@192.168.41.24:1521/xe')
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_after.xml')[0]
    
    def select_search(self, search):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_search")
        rs = self.cs.execute(sql, (search,))
        list = []
        for record in rs:
            list.append({'after_seq':record[0],'after_title':record[1],'after_content':record[2],'attach_file':record[3],'attach_path':record[4],'in_date':record[5][0:8],'in_user_id':record[6],'up_date':record[7],'up_user_id':record[8]})
        return list
    
    def select_list(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_list")
        rs = self.cs.execute(sql)
        list = []
        for record in rs:
            list.append({'after_seq':record[0],'after_title':record[1],'after_content':record[2],'attach_file':record[3],'attach_path':record[4],'in_date':record[5][0:8],'in_user_id':record[6],'up_date':record[7],'up_user_id':record[8]})
        return list
    
    def select(self,after_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select")
        rs = self.cs.execute(sql, (after_seq,))
        obj = None
        for record in rs:
            obj = {'after_seq':record[0],'after_title':record[1],'after_content':record[2],'attach_file':record[3],'attach_path':record[4],'in_date':record[5][0:8],'in_user_id':record[6],'up_date':record[7],'up_user_id':record[8]}
        return obj
    
    def insert(self,after_seq, after_title, after_content,attach_file,attach_path, in_date, in_user_id, up_date, up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")
        self.cs.execute(sql, (after_title, after_content, attach_file,attach_path, in_user_id, up_user_id))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt

    def update(self,after_seq, after_title, after_content, attach_file, attach_path, up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update")        
        self.cs.execute(sql, (after_title, after_content, attach_file, attach_path, up_user_id, after_seq))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    def del_img(self,after_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "del_img")  
        self.cs.execute(sql, (after_seq,))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    
    def delete(self,after_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "delete")  
        self.cs.execute(sql, (after_seq,))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
        
    def __del__(self): 
        self.cs.close()
        self.conn.close()