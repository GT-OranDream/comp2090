#sorting strategy base class
class SortStrategy:
    def sort(self, student_list):
        pass

# ascending order
class ShellSortAsc(SortStrategy):
    def sort(self, student_list):
        if not student_list:
            return []
        students = student_list.copy()
        n = len(students)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = students[i]
                j = i
                while j >= gap and students[j - gap].score > temp.score:
                    students[j] = students[j - gap]
                    j -= gap
                students[j] = temp
            gap //= 2
        return students

# descending order
class ShellSortDesc(SortStrategy):
    def sort(self, student_list):
        if not student_list:
            return []
        students = student_list.copy()
        n = len(students)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = students[i]
                j = i
                while j >= gap and students[j - gap].score < temp.score:
                    students[j] = students[j - gap]
                    j -= gap
                students[j] = temp
            gap //= 2
        return students
