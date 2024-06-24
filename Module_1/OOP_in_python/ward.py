from abc import ABC, abstractmethod


class Ward:
    def __init__(self):
        self.__persons = []

    def add_person(self, person):
        self.__persons.append(person)

    def count_doctor(self):
        count = 0
        for person in self.__persons:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_age(self):
        self.__persons.sort(key=lambda x: x._yob, reverse=True)

    def compute_average(self):
        sum = 0
        count = 0
        for person in self.__persons:
            if isinstance(person, Teacher):
                sum += person._yob
                count += 1
        return sum / count


class Person:
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.__grade = grade

    def describe(self):
        print(
            f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self.__grade}.")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.__subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self.__subject}.")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.__specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialization: {self.__specialist}.")


if __name__ == "__main__":

    ward = Ward()

    ward.add_person(Doctor("Dr. Alice", 1975, "Cardiologist"))
    ward.add_person(Student("Bob", 2001, "A"))
    ward.add_person(Teacher("Mr. Clark", 1980, "Mathematics"))
    ward.add_person(Doctor("Dr. Eve", 1985, "Neurologist"))
    ward.add_person(Teacher("Dr. Dain", 1988, "Computer Science"))

    print("Number of doctors in the ward:", ward.count_doctor())

    print("Teacher Average YoB:", ward.compute_average())

    ward.sort_age()

    for person in ward._Ward__persons:
        person.describe()
