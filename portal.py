class CoursePortal:

    def __init__(self, student_name):
        self.student_name = student_name
        self.__is_locked = False

    def lock_portal(self):
        self.__is_locked = True
        print("Deadline passed. Portal locked.")

    def accept_submission(self):
        if self.__is_locked == True:
            print(ValueError("Error: Deadline has passed. Submission rejected"))
        elif self.__is_locked == False:
            print(f"Submission accepted for {self.student_name}")