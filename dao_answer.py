import cx_Oracle
import mybatis_mapper2sql

class DaoAnswer:
    def __init__(self):
        self.conn = cx_Oracle.connect('team3/java@192.168.41.24:1521/xe')
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_answer.xml')[0]
    
    def select_search(self, user_id, search):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_search")
        rs = self.cs.execute(sql, (user_id, search))
        list = []
        for record in rs:
            list.append({'answer_seq':record[0],'intrvw_content':record[1],'answer_content':record[2],'in_date':record[3][0:8]})
        return list
    
    def select_list(self, user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_list")
        rs = self.cs.execute(sql,(user_id,))
        list = []
        for record in rs:
            list.append({'answer_seq':record[0],'intrvw_content':record[1],'answer_content':record[2],'in_date':record[3][0:8]})
        return list

    def select(self, answer_seq,in_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select")
        rs = self.cs.execute(sql, (answer_seq,in_user_id))
        obj = None
        for record in rs:
            obj = {'answer_seq':record[0],'intrvw_content':record[1],'answer_content':record[2],'in_date':record[3][0:8]}
        return obj
    
    def insert(self, user_id, my_answer, bot_question_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")
        self.cs.execute(sql, (bot_question_seq, my_answer, user_id))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt

    def update(self, answer_seq, answer_content,):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update")        
        self.cs.execute(sql, (answer_content, answer_seq))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    def delete(self,answer_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "delete")  
        self.cs.execute(sql, (answer_seq,))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
        
    def __del__(self): 
        self.cs.close()
        self.conn.close()