class SchoolMember:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def present_yourself(self):
        return f'My name in {self.name},i am {self.age} old'

    @classmethod
    def get_older(cls):
        return f'My name in {cls.name},i am {cls.age + 1} old'

    @staticmethod
    def able_to_drive(self, age):
        answer = {True: 'YES', False: 'NO'}
        return f'Able to drive:{answer[age >= 16]}'


