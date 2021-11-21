import cx_Oracle
import mybatis_mapper2sql
import xml.etree.ElementTree as elemTree

keyXml = elemTree.parse('keys.xml')
db_address = keyXml.find('string[@name="db_address"]').text

class DaoInterview:
    def __init__(self):
        self.conn = cx_Oracle.connect(db_address)
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_interview.xml')[0]
    
    def select_content(self,): # 봇에 질문 뿌리기 용
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_content")
        rs = self.cs.execute(sql)
        list = []
        for record in rs:
            list.append({'intrvw_seq':record[0],'intrvw_content':record[1]})
        return list
    
    def select_list(self,):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_list")
        rs = self.cs.execute(sql)
        list = []
        for record in rs:
            list.append({'intrvw_seq':record[0],'intrvw_content':record[1],'in_date':record[2],'in_user_id':record[3],'up_date':record[4],'up_user_id':record[5]})
        return list
    
    def select(self,intrvw_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select")
        rs = self.cs.execute(sql, (intrvw_seq,))
        obj = None
        for record in rs:
            obj = {'intrvw_seq':record[0],'intrvw_content':record[1],'in_date':record[2],'in_user_id':record[3],'up_date':record[4],'up_user_id':record[5]}
        return obj
    
    def insert(self,intrvw_seq, intrvw_content, in_date, in_user_id, up_date, up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")
        self.cs.execute(sql, (intrvw_content, in_user_id, up_user_id))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
        
    def update(self,intrvw_seq, intrvw_content, in_date, in_user_id, up_date, up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update")        
        self.cs.execute(sql, (intrvw_content, up_user_id, intrvw_seq))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    def delete(self,intrvw_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "delete")  
        self.cs.execute(sql, (intrvw_seq,))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
        
    def __del__(self): 
        self.cs.close()
        self.conn.close()