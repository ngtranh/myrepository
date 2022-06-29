import Student_management
st_management = Student_management.StudentManagement()

while 2==2:
    print("1. Nhập thông tin học sinh\n")
    print("2. Hiển thị thông tin học sinh\n")
    key = int(input("Chọn chức năng quản lí: "))
    if key == 1:
         print("Thêm thông tin học sinh")
    st_management.input_student()
    if key == 2:
         print("Hiển thị thông tin học sinh")
         st_management.showStudent(Student_management.StudentManagement.getlistStudent)

        
