class Student:
  def __init__(self,name,degree,student_id):
    if not name:
      raise ValueError("Name should not be empty")
    if degree not in ["ECE","BIO","MECH","EEE"]:
      raise ValueError("Degree not valid")
    if len(student_id) < 6 or len(student_id) > 6:
      raise ValueError("Not valid id.")
    self.name = name 
    self.degree = degree 
    self.student_id = student_id
    
def main():
  student = get_student()
  print(f"{student.name} - ID:{student.student_id} - from {student.degree}")

def get_student():
  name = input("Name: ").strip()
  degree = input("Degree: ").capitalize()
  student_id = input("ID:")
  return Student(name,degree,student_id)

@property
def degree(self):
  return self._degree

@degree.setter
def degree(self,degree):
  if degree not in ["ECE","BIO","MECH","EEE"]:
    raise ValueError("Degree not valid")
  self._degree = degree

if __name__ == "__main__":
  main()
