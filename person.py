from job.job import Job

class Person:
    name = 'John Smith'
    age = 21
    job = ""

    def __init__(self, name, age, job:Job):
        self.name = name
        self.age = age
        self.job = job