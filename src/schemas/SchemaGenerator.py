import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

class SchemaGenerator :
  def __init__ (self, **kwargs):
    self.name = ""
    self.tables = {}


    if "name" in kwargs:
      self.name = kwargs["name"]
    
    return self
  
  def addTable (self, name):
    # add table if not exists
    if not name in self.tables:
      self.tables[name] = {}
      self.tables[name]['columns'] = {}
      self.tables[name]['indexes'] = {}
      self.tables[name]['properties'] = {
        'auto_increment'  : 0,
        'rows'  : 0
      }
    
    return self
  
  def addIndex (self, name, indexName, choice, column, cardinality = 0):
    # create new index
    index = {
      'name'        : indexName,
      'type'        : 'btree',
      'choice'      : choice,
      'column'      : column,
      'cardinality' : cardinality,  
    }

    self.tables[name]['indexes'][indexName] = index

    return self
  
  def updateCardinality (self, name, cardinalityName, cardinality):
    if self.tables[name]['indexes'] in cardinalityName:
      self.tables[name]['indexes'][cardinalityName]  = cardinality
    
    return self

  def addColumn (self, tableName, name, type, nullable = False):
    if tableName in self.tables:
      self.tables[tableName]['columns'][name] = {}
      self.tables[tableName]['columns'][name]['name'] = name
      self.tables[tableName]['columns'][name]['type'] = type
      self.tables[tableName]['columns'][name]['nullable'] = nullable
      
    return self

  def addColumns (self, tableName, columns):
    for column in columns:
      nullable = False
      
      # set nullable
      if 'nullable' in column:
        if column['nullable'] == True or column['nullable'] == 'true':
          nullable = True

      # add each entry    
      self.addColumn (tableName, column['name'], column['type'], nullable)

    return self
  
  def getColumns (self, tableName):
    if tableName in self.tables:
      return self.tables[tableName]['columns']
    
  def getColumnType (self, tableName, columnName):
    if columnName in self.tables[tableName]['columns']:
      return self.tables[tableName]['columns'][columnName]['type']
    return None

  def getColumnDetails (self, tableName, columnName):
    if columnName in self.tables[tableName]['columns']:
      return self.tables[tableName]['columns'][columnName]
    return None
  
  def isTableExists (self, tableName):
    if tableName in self.tables:
      return True
    return False

  def isColumnExists (self ,tableName, columnName):
    if columnName in self.tables[tableName]['columns']:
      return True
    return False
  
  def getDatabaseName (self):
    return self.name

  def getTables (self):
    return self.tables
  
  def info (self):
    return self