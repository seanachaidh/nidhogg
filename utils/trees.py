#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 19:33:49 2018

@author: pieter
"""

import uuid

# Dit bestand bevat onder andere manieren om dna te encoderen via bomen

class GraphNode:
	def __init__(self, children, data):
		self.children = children
		self.data = data
		self.id = uuid.uuid1()
	def __eq__(self, other):
		return self.id == other.id
	

class Graph: 
	def __init__(self):
		self.nodes = []
	def add_node(self, parentnode, toadd):
		for n in self.nodes:
			if n.id == toadd.id:
				n.children.append(toadd)
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
					
		
		