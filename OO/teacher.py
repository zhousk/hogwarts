from OO.human import Human


class Teacher(Human):
    def work(self):
        print("The work is teach student")

    # 这里有点类似于多肽，初中学生和高中学生都有study的方法，这样子就不至于写为"教初中学生"和“教高中学生”两种方法
    def teach(self, student):
        student.study()
