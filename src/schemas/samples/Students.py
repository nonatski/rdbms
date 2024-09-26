import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

from SchemaGenerator import SchemaGenerator

class Students (SchemaGenerator):
  def __init__(self):
    super().__init__(name = "students_database")
    
    # student information
    self.addTable ('student_info')
    self.addColumns ('student_info', [
      {
        'name'  : 'name',
        'type'  : 'string'
      },
      {
        'name'      :   'age',
        'type'      :   'integer',

      }
    ])

    # student enrollment
    self.addTable ('student_enrollment')
    self.addColumns ('student_enrollment', [
      {
        'name'  : 'name',
        'type'  : 'string'
      },
      {
        'name'      :   'year',
        'type'      :   'integer',
      }
    ])

