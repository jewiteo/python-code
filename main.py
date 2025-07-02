from person import Person
from job.job import Job

if __name__ == "__main__":
    person1 = Person("Mary", 25, Job("Office worker", 5000))
    print("My name is " + person1.name + " and my age is " + str(person1.age))
    print("My job is a " + person1.job.jobName + " and I earn " + str(person1.job.salary))