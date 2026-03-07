# 文件读写
class FileIO:
    @staticmethod
    def save_students(filename, student_list):
        try:
            with open(filename, "w", encoding="utf-8") as f:
                for s in student_list:
                    f.write(f"{s.student_id},{s.name},{s.score}\n")
        except Exception as e:
            raise IOError(f"Failed to save：{e}")

    @staticmethod
    def load_students(filename):
        students = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(",")
                    sid = parts[0]
                    name = parts[1]
                    score = int(parts[2])
                    from student import Student
                    students.append(Student(sid, name, score))
            return students
        except FileNotFoundError:
            return []
        except Exception as e:
            raise IOError(f"Failed to read：{e}")