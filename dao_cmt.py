import cx_Oracle
import mybatis_mapper2sql

class DaoCmt:
    def __init__(self):
        self.conn = cx_Oracle.connect('team3/java@192.168.41.24:1521/xe')
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_cmt.xml')[0]

    def select_list(self,board_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_list")
        rs = self.cs.execute(sql,(board_seq,))
        
        list = []
        for record in rs:
            list.append({'cmt_seq':record[0],'cmt_content':record[1],'in_date':record[2],'in_user_id':record[3],'up_date':record[4],'up_user_id':record[5],'board_seq':record[6]})
        return list
    
    def insert(self, cmt_content, in_user_id,board_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")
        self.cs.execute(sql, (cmt_content,in_user_id,in_user_id,board_seq))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt

    def delete(self, cmt_seq, board_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "delete")  
        self.cs.execute(sql,(cmt_seq,board_seq))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    def del_boardcmt(self,board_seq,):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "del_boardcmt")  
        self.cs.execute(sql, (board_seq,))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
        
    def __del__(self): 
        self.cs.close()
        self.conn.close()