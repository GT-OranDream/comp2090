from student import Student
from student_manager import StudentManager
from sorting_algorithm import ShellSortAsc, ShellSortDesc
from file_io import FileIO

def main():
    manager = StudentManager()
    filename = "students.txt"
    # 加载
    students = FileIO.load_students(filename)
    for s in students:
        try:
            manager.add_student(s)
        except ValueError:
            pass

    while True:
        print("\n=====--- Student grade sorting system ---=====")
        print("1. Increase student（add）")#增加学生
        print("2. Delete student")#删除学生
        print("3. Show all student ")#显示全部
        print("4. Ascending order the mark")#成绩升序
        print("5. Descending order the mark ")#成绩降序
        print("6. Save to the document")#保存到文件
        print("0. LEAVE")#退出
        choice = input("Please enter the options：")

        try:
            if choice == "1":
                sid = input("Student ID：")
                name = input("Student name：")
                score = int(input("MARK："))
                manager.add_student(Student(sid, name, score))
                print("Add successfully！")
            elif choice == "2":
                sid = input("input what you what to delate the student ID：")
                manager.delete_by_id(sid)
                print("delate successfully！")
            elif choice == "3":
                for s in manager.get_all():
                    print(s)
            elif choice == "4":
                res = manager.sort_students(ShellSortAsc())
                for s in res:
                    print(s)
            elif choice == "5":
                res = manager.sort_students(ShellSortDesc())
                for s in res:
                    print(s)
            elif choice == "6":
                FileIO.save_students(filename, manager.get_all())
                print("save successfully！")
            elif choice == "0":
                break
            else:
                print("error 404")
        except ValueError as e:
            print("input error：", e)
        except IOError as e:
            print("ddocument error：", e)

if __name__ == "__main__":
    main()