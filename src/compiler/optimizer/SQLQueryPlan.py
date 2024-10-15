import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

class SQLQueryPlan:
    def __init__ (self, tree):
        self.steps         =      []
        self.tree          =      tree
    
    def create (self):
        return self.__parse(self.tree)
    
    def __parse (self, nodes):
        if '__x__' in nodes:
            self.__parseCrossJoin (nodes)
        
        if '__Ω__' in nodes:
            self.__parseSelect (nodes, nodes['operators'])
        
        if '__π__' in nodes:
            self.__parseProject (nodes)

        return self.steps
    
    def __parseChildren (self, nodes):
        if 'nodes' in nodes:
            if not nodes['nodes'] == None: self.__parse (nodes['nodes'])
        
        return self
    
    def __addStep (self, step):
        self.steps.append (step)

        return self
    
    def __parseSelect (self, nodes, operatorNodes = None):

        conditions          =    []
        nodeIndex           =    0
        scanNodes           =   True
        selectNodes         =   nodes['__Ω__']
        selectNodesLength   =   len (nodes['__Ω__'])
        
        while (scanNodes):
            try:
                tempNodes = []
                tempNodes.append(selectNodes[nodeIndex])
                
                # add operator in between conditions
                if not operatorNodes == None:
                    if nodeIndex < len(operatorNodes):
                        tempNodes.append (operatorNodes[nodeIndex])

                # get the next condition if it has
                if (nodeIndex + 1) < selectNodesLength:
                    tempNodes.append(selectNodes[nodeIndex])
                    
                    # skip next node
                    nodeIndex = nodeIndex + 1

                # join array and push to condition list
                tempNodeString = " ".join(tempNodes)
                conditions.append(tempNodeString)
                nodeIndex = nodeIndex + 1

                if nodeIndex > selectNodesLength:
                    scanNodes = False
            except Exception as e:
                scanNodes = False
        
        step = {
            'name'          :   'filter',
            'conditions'    :   conditions,
            'cost'          :   0    
        }
        
        # add to step
        self.__addStep (step)

        # parse children
        self.__parseChildren(nodes)

        return self
    
    def __parseProject (self, nodes):

        columns = []

        for node in nodes['__π__']:
            columns.append(node)
        
        step = {
            'name'      :   'project',
            'columns'   :   columns,
            'cost'      :   0
        }

        self.__addStep(step)
        self.__parseChildren (nodes)

        return self
    
    def __parseCrossJoin (self, nodes):
        tables = []
        merge_algorithms = []

        for node in nodes['__x__']:
            if '__r__' in node:
                tables.append({
                    'name'  :   node['__r__'],
                    'rows'  :   0,
                    'cols'  :   0
                })
        
        # algorithims to be used on all the tables
        merge_algorithms.append({
            'hash'      :   { 'cost'  :   0 },
            'merge'     :   { 'cost'  :   0 },
            'nested'    :   { 'cost'  :   0 }
        })

        step = {
            'name'          :   'join',
            'tables'        :   tables,
            'algorithims'   :   merge_algorithms
        }

        # add to step
        self.__addStep (step)
        
        # parse children
        self.__parseChildren(nodes)

        return self