import cx_Oracle
import mybatis_mapper2sql
import xml.etree.ElementTree as elemTree

keyXml = elemTree.parse('../keys.xml')
db_address = keyXml.find('string[@name="db_address"]').text

class MyDaoBoard:
    def __init__(self):
        self.conn = cx_Oracle.connect(db_address)
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mapper/mybatis_board.xml')[0]
        
    def counter(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "board_cnt")
        rs = self.cs.execute(sql)
        list = []
        for record in rs:
            return record[0]
        
    def myselect_list_admin(self,search):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_list_admin")
        rs = self.cs.execute(sql,(search,))
        list = []
        for record in rs:
            list.append({'board_seq':record[0],'board_title':record[1],'board_content':record[2],'attach_file':record[3],'attach_path':record[4], 'in_date':record[5][0:8],'in_user_id':record[6],'up_date':record[7],'up_user_id':record[8],'rnum':record[9]})
        return list
        
    def select_all_list(self,search):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_all_list")
        rs = self.cs.execute(sql,(search,))
        list = []
        for record in rs:
            list.append({'board_seq':record[0],'board_title':record[1],'board_content':record[2],'attach_file':record[3],'attach_path':record[4], 'in_date':record[5][0:8],'in_user_id':record[6]})
        return list

    def myselect(self,board_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select")
        rs = self.cs.execute(sql,(board_seq,))
        obj= None
        for record in rs:
            obj ={'board_seq':record[0],'board_title':record[1],'board_content':record[2],'attach_file':record[3],'attach_path':record[4], 'in_date':record[5][0:8],'in_user_id':record[6],'up_date':record[7],'up_user_id':record[8],'board_pass':record[9]}
        return obj
    
    def myinsert(self,board_title, board_content, attach_file, attach_path, in_date, in_user_id, up_date, up_user_id,board_pass):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")
        self.cs.execute(sql, (board_title, board_content, attach_file, attach_path, in_user_id, up_user_id,board_pass))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
        
    def myupdate(self,board_seq, board_title, board_content, attach_file, attach_path, in_date, in_user_id, up_date, up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update")        
        self.cs.execute(sql, (board_title, board_content, attach_file, attach_path, up_user_id,board_seq))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    ##########################################################################
    def del_img(self, board_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "del_img")  
        self.cs.execute(sql, (board_seq,))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt

    def mydelete(self, board_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "delete")  
        self.cs.execute(sql, (board_seq,))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
        
    def __del__(self): 
        self.cs.close()
        self.conn.close()