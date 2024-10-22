import sys
import os
import copy

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(os.path.join(dir_path, os.pardir)))

class SQLQueryPlan:
    def __init__ (self, tree):
        self.steps           =      []
        self.tree            =      tree
        self.parsedTree      =      []
        self.steps           =      0
        self.debug           =      False
    
    def create (self):
        return self.__parse(self.tree)
    
    def setDebug (self, debug = False):
        self.debug      =   debug
        return self
    
    def __getLastChild (self, node):
        # get all children's children
        if not node == None:
            if 'children' in node:
                if not node['children'] == None: 
                    return self.__getLastChild (node['children'])
        return node
    
    def __getParentNode (self, childNode, parentNode = None):
        # get all children's children
        if not childNode == None:
            if 'children' in childNode:
                if not childNode['children'] == None: 
                    return self.__getParentNode(childNode['children'], childNode)
    
        return parentNode
    
    def __getNodeType (self, node):
        nodeType        =   None
        nodeValue       =   None
        nodeChildren    =   None

        if not node == None:
            if '__π__' in node: nodeType = '__π__'
            if '__Ω__' in node: nodeType = '__Ω__'
            if '__x__' in node: nodeType = '__x__'
            if '__θ__' in node: nodeType = '__θ__'

            if not nodeType == None:
                nodeValue = node[nodeType]

                if 'children' in node:
                    if not node['children'] == None: nodeChildren = node['children']

        return { 
            'nodeType'      :   nodeType, 
            'nodeValue'     :   nodeValue,
            'nodeChildren'  :   nodeChildren 
        }
    
    def __processNodes (self, nodes, rootNode = [], addToParsedTree = True):
        
        nodeType    =   self.__getNodeType (nodes)

        if nodeType['nodeType'] in ['__x__']:

            if self.debug:
                print('--pushing to parsed tree--')
                print(rootNode)

            # process the children of '__x__'
            self.steps += 1

            # add to parsedTree
            if addToParsedTree:  self.parsedTree.insert(0, {f'__SEQUENCE__:step {self.steps}:' : rootNode})

            # temporarily holds all the children of ['__x__']
            mergedNodes = []

            for i in range(len(nodes['__x__'])-1, -1, -1):                
                if i < len(nodes['__x__']):
                    # traverse all the children and return in reversed order
                    children = self.__processNodes(nodes['__x__'][i], [], False)

                    if self.debug:
                        print('\r\n-----TRAVERSING JOIN NODES-----')
                        print(nodes['__x__'][i])
                        print('--------------------------\r\n')

                        print ('\r\n------AFTER TRAVERSING-----')
                        print(children)
                        print('-----------END AFTER------------\r\n')
                    
                    # merge to the temporary nodes after reading the branch of [__x__]
                    if 'rootNode' in children: mergedNodes.insert(0, children['rootNode'])

            # always add the mergedNodes in front of the list after reading all its branches
            self.steps += 1
            self.parsedTree.insert(0, {f'__MERGE__:step {self.steps}:' : mergedNodes})
           
        else:
            if self.debug: print('\r\n---current node--', nodes, '-----\r\n')

            # ensures that we are visiting a valid node
            if not nodes == None:
                nextChildren = None
                if 'children' in nodes:
                    # save a copy the children of the current node
                    # this ensures that we can still visit the next node even after removing the the children from its parent 
                    nextChildren = copy.deepcopy (nodes['children'])

                    # remove children of the node before pushing
                    nodes['children'] = None

                    # prepend to the root node
                    rootNode.insert(0, nodes)

                    if self.debug:
                        print('--processing next node---')
                        print('--root--', rootNode)
                        print('--children--', nextChildren, '\r\n')

                    if not nextChildren == None:
                        return self.__processNodes(nextChildren, rootNode, addToParsedTree)
                    else:
                        # if addToParsedTree == true, add the rootNode after visiting the last node
                        if addToParsedTree:
                            self.steps += 1
                            n = {f'__MERGE__:step {self.steps}:' : rootNode} 
                            self.parsedTree.insert(0, n)
                else:
                    if self.debug:
                        print('--node without children--')
                        print(nodes, '\r\n')

                    # append the node if there is no children
                    # then add the node to rootNode if necessary   
                    rootNode.insert(0, nodes)
                    if addToParsedTree: 
                        self.steps += 1
                        self.parsedTree.insert(0, {f'__SEQUENCE__:step {self.steps}:' : rootNode})
                
            else:
                if self.debug: print('\r\n---END TRAVERSING---\r\n')
                pass
                
        return {'nodes' : nodes, 'rootNode' : rootNode}
    

    def __parse (self, nodes):
        # start parsing nodes
        self.__processNodes (nodes, [])
        if self.debug:
            print('\r\n---------RESULTS-------')
            print(self.parsedTree)
            print('\r\n-------END RESULTS------\r\n')

        # return the parsed tree in list
        return self.parsedTree

        



                
                