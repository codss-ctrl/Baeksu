import cx_Oracle
import mybatis_mapper2sql
import xml.etree.ElementTree as elemTree

keyXml = elemTree.parse('keys.xml')
db_address = keyXml.find('string[@name="db_address"]').text
class DaoGraph:
    def __init__(self):
        self.conn = cx_Oracle.connect(db_address)
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_member.xml')[0]
        
    def counter(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "member_cnt")
        rs = self.cs.execute(sql)
        list = []
        for record in rs:
            return record[0]
        
    def __del__(self): 
        self.cs.close()
        self.conn.close()