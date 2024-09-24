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
    
    return self

  def addColumn (self, tableName, name, type):
    if tableName in self.tables:
      self.tables[tableName]['columns'][name] = type
      
    return self

  def addColumns (self, tableName, columns):
    for column in columns:
      for col in column :
        self.addColumn (tableName, col , column[col])

    return self
  
  def getColumns (self, tableName):
    if tableName in self.tables:
      return self.tables[tableName]['columns']
    
  def getColumnType (self, tableName, columnName):
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
