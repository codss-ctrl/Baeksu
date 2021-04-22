from openpyxl import Workbook

class Excel:
    def __init__(self):
        self.temp_list = []

    def import_excel(self, user_id, answer_list):
        write_wb = Workbook()
         
        write_ws = write_wb.active
        write_ws['A1'] = '순번'
        write_ws['B1'] = '제목'
        write_ws['C1'] = '답변'
        write_ws['D1'] = '등록일'
        
        for i in answer_list:
            print(i)
            write_ws.append([i['answer_seq'],i['intrvw_content'],i['answer_content'],i['in_date']])

        write_wb.save('X:/My_answer_'+user_id+'.xlsx')
        write_wb.close()