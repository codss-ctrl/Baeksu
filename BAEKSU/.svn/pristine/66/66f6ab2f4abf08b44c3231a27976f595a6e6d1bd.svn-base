import cx_Oracle
import mybatis_mapper2sql  

class MyDaoMemo:
    def __init__(self):
        self.conn = cx_Oracle.connect('team3/java@192.168.41.24:1521/xe')
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_memo.xml')[0]
        
    def myselect_list(self, in_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "myselect_list")
        rs = self.cs.execute(sql,(in_user_id,))
        list = []
        for record in rs:
            list.append({'memo_seq':record[0],'memo_content':record[1],'memo_yn':record[2],'in_date':record[3][0:8],'in_user_id':record[4],'up_date':record[5],'up_user_id':record[6]})
        return list
    
    def myselect(self, memo_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "myselect")
        rs = self.cs.execute(sql,(memo_seq,))
        obj = None;
        for record in rs:
            obj = {'memo_yn':record[0]}
        return obj
    
    def myinsert(self,memo_content,in_user_id, up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")
        self.cs.execute(sql, (memo_content, in_user_id, up_user_id))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt

        
    def myupdate(self,memo_yn, memo_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update")        
        self.cs.execute(sql, (memo_yn, memo_seq))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt


    def mydelete(self,memo_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "delete")  
        self.cs.execute(sql, (memo_seq,))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    
        
    def __del__(self): 
        self.cs.close()
        self.conn.close()
        
        
if __name__ == "__main__":
    dao = MyDaoMemo()
    cnt = dao.myselect('3')
    
#     cnt = dao.myinsert('2', '2', '2', '2', '2', '2')
    
#     cnt = dao.myupdate('1', 5, 5, 5, 5, 5, 5)


#     cnt = dao.mydelete(2)
    print(cnt)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    