class Solution(object):
    def countStudents(self, students, sandwiches):
        while True:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                if len(students) == 0 or len(sandwiches) == 0:
                    break
            else:
                students.append(students[0])
                students.pop(0)
                if sandwiches[0] not in students:
                    break
                
        return len(students)