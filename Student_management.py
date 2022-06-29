#Nhập thông tin học sinh
import math
import info_student

class StudentManagement:
    #List, #Dict
    listStudent = []
    #Xây dựng 1 hàm tự động sinh ra mã hs
    def autogenous_Id(self): #Tìm giá trị lớn nhất trong 1 mảng
        id = 1
        if (self.count_student() > 0):
            id = self.listStudent[0]._id
            for st in self.listStudent:
               if id < st._id:
                  id = st._id
            id = id + 1
        return id
    def count_Student(self):
        return self.listStudent._len_()
    def input_Student(self):
        id_st = self.autogenous_Id()
        full_name_st = input("Nhập họ tên học sinh: ")
        birthday_st = input("Nhập ngày tháng năm sinh: ")
        sex_stt = input("Nhập giới tính: ")
        score_math_st = float(input("Nhập điểm toán: "))
        score_english_st = float(input("Nhập điểm anh: "))
        score_literature_st = float(input("Nhập điểm văn = "))
        st = Info_student.Student(id_st, full_name_st, birthday_st, sex_stt, score_math_st, score_english_st, score_literature_st)
        self.score_Avg(st)
        self.rank_Score(st)
        self.listStudent.append(st)
    def score_Avg(self, st:info_student.Student):
        scoreAvg = (st._score_math + st._score_english + st._score_literature) / 3
    def rank_Score(self, st:info_student.Student):
        if (st._score_Avg >= 8):
            st._rank_Score = "Giỏi"

        elif (st._score_Avg >= 6.5):

            st._rank_Score = "Khá"

        elif (st._score_Avg >= 5):

            st._rank_Score = "Trung Bình"

        else:

            st._rank_Score = "Yếu"

        
def showStudent(self, listStudent):
    print(listStudent)
    print("\n")
    print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
         .format("ID", "Ten", "Gioi tinh", "Tuoi", "Toan", "Van", "Anh"))
    if (listStudent._len_() > 0):
           for st in listStudent:
                print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
                   .format(st._id, st._fullname, st._sex, st._birthday, st._scoremath, st._scoreliterature,
                       st._scoreenglish,st._scoreavg, st._rankscore))

def getListStudent(self):
    return listStudent
    


    
