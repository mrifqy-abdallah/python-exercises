class Garden:
    def __init__(self, diagram, students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.students = students
        self.students.sort()  # Students' name needs to be sorted alphabetically
        self.diagram = diagram.split()
        self.plant_dict = {
            "G": "Grass",
            "C": "Clover",
            "R": "Radishes",
            "V": "Violets"
        }

    def plants(self, a_student):
        student_index = self.students.index(a_student)
        student_index *= 2
        initial_plants = ""
        actual_plants = []
        # Get the student's plants in initial alphabet
        for i in self.diagram:
            initial_plants += i[student_index:student_index+2]
        # Translate the alphabet initial to actual name and store it as a list
        for initial in initial_plants:
            actual_plants.append(self.plant_dict[initial])
        return actual_plants
