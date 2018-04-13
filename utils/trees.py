#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 19:33:49 2018

@author: pieter
"""

import uuid, unittest
# Dit bestand bevat onder andere manieren om dna te encoderen via bomen

class GraphNode:
	def __init__(self, data, children = []):
		self.children = children
		self.data = data
		self.id = uuid.uuid1()
		
	def __repr__(self):
		return "Node with data: " + str(self.data)
	def __eq__(self, other):
		return self.id == other.id
	

#Vorlopig ondersteunt deze implementatie alleen bomen!
class Graph: 
	def __init__(self):
		self.nodes = []
	def add_node(self, toadd, parentnode = None):
		if parentnode is None:
			self.nodes.append(toadd)
			return True
		else:
			for n in self.nodes:
				if n.id == parentnode.id:
					n.children.append(toadd)
					#Dit moet slimmer
					self.nodes.append(toadd)
					return True
		return False
	# Data wordt hier gezien als het doel
	def depth_first_data(self, data):
		visited = []
		stack = []
		
		stack.append(self.nodes[0]) # initialiseer de stack met het eerste knooppunt
		
		while stack:
			current = stack.pop()
			visited.append(current)
			if current.data == data:
				return current
			else:
				for c in current.children:
					# Oneindige lussen voorkomen
					if not c in visited:	
						stack.append(c)


# FUNCTIES VOOR HET MAKEN VAN BOMEN!
						
                        
class TestTree(unittest.TestCase):
	
	def setUp(self):
		mytree = Graph()
		testdata = 5
		rootnode = GraphNode(1)
		mytree.add_node(rootnode)
		
		firstchild = GraphNode(2)
		secondchild = GraphNode(3)
		self.datachild = GraphNode(testdata)
		
		mytree.add_node(firstchild, rootnode)
		mytree.add_node(secondchild, rootnode)
		mytree.add_node(self.datachild, secondchild)
		
		self.mytree = mytree
		
	def test_tree_create(self):
		retval = self.mytree.depth_first_data(5)
		self.assertEqual(retval, self.datachild, msg='boomtest niet gelukt')
		
		
if __name__ == '__main__':
	unittest.main()
        