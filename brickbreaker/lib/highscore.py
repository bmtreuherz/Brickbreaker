
import level
class HighScore(object):
	def check_highscore(self):
		highscore = open("data/highscore.txt")
		number = highscore.read()
		number_int = int(number)
		highscore.close()
		self.highscore = number_int
		
		if level.start.level_number > self.highscore:
			self.highscore = level.start.level_number - 1
			score = open("data/highscore.txt", 'w')
			score.write(str(self.highscore))
			score.close()
		
		
High_score = HighScore()