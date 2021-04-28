class School:
    def __init__(self):
        self.students_data = {}

    def add_student(self, name, grade):
        '''Added data are stored in this format:
        {
            1: ["studentA", "studentB"],
            2: ["studentX],
            etc..
        }
        The int set as keys represents the grade of students'''
        if grade not in self.students_data:
            self.students_data[grade] = []
        self.students_data[grade].append(name)
        return self.students_data[grade].sort()  # Name's data is sorted alphabetically

    def roster(self):
        '''Get all student data, sorted by the grade'''
        students_roster = []
        grade_recorded = list(self.students_data.keys())
        grade_recorded.sort()
        for i in grade_recorded:
            for j in self.students_data[i]:
                students_roster.append(j)
        return students_roster

    def grade(self, grade_number):
        '''Get all student data in a class'''
        if grade_number in self.students_data:
            return self.students_data[grade_number]
        return []
