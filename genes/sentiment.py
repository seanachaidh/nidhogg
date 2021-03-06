#Gene for analyzing sentiment in a text
#parameters: Story: A nested list with lists for each chunk of analyzable data with each chunk split up in tokens
#			 Lexicon: A lexicon of negative and positive words

class Sentiment:
	
	def _calculate_stats(self, scores, col):
		
		sumpos = 0
		countneg = 0
		sumneg = 0
		countpos = 0
		sumobj = 0
		countobj = 0
		
		for i in range(len(scores)):
			current = scores[i]
			sumpos += current[0]
			sumneg += current[1]
			sumobj += current[2]
			
			if current[0] > current[1]:
				countpos += 1
			elif current[0] < current[1]:
				countneg += 1
			else:
				#Ik verwacht niet dat dit veel gaat voorkomen
				countobj += 1
		#Geen een zestupel terug
		return (sumpos, countpos, sumneg, countneg, sumobj, countobj)
	
	
	def _mark_words(self):
		retval = []
		for chunk in self.story:
			scores = []
			for token in chunk:
				foundscore = self.scores[token]
				scores.append(foundscore)
			retval.append(scores)
		return retval
	
	def _parse_lexicon(self):
		retval = dict()
		with open(self.lexicon, 'r') as f:
			for line in f:
				if not line.startswith('#'):
					cols = line.split('\t') # Split the lines at tabulation
					names = cols[4].split(' ')
					pos_score = cols[2]
					neg_score = cols[3]
					obj_score = 1 - (pos_score + neg_score)
					
					# Add all names
					for n in names:
						actual_name = n.split('#')[0]
						retval[actual_name] = (pos_score, neg_score, obj_score)
		return retval
	# Hiervan moet ik een abstracte methode maken!
	def get_statistics(self):
		retval = dict()
		
#		totalwords = self.stats[1] + self.stats[3] + self.stats[5]
		
		retval['Positive sum'] = self.stats[0]
		retval['Positive count'] = self.stats[1]
		retval['Postive mean'] = self.stats[0] / self.stats[1]
		retval['Negative sum'] = self.stats[2]
		retval['Negative count'] = self.stats[3]
		retval['Negative mean'] = self.stats[2] / self.stats[3]
		
		return retval
		
		
	def __init__(self, story, lexicon):
		self.lexicon = lexicon
		self.parsed_lexicon = self._parse_lexicon()
		self.marked_words = self._mark_words()
		self.stats = self._calculate_stats()
		   