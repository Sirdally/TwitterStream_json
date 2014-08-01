import sys
import json

def prepsentidict(senti_file, sentiscores):
	for line in senti_file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		sentiscores[term] = int(score)  # Convert the score to an integer.

def main():
	## Open the files
	senti_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2]) 
	
	## Prepare the scores dictionary
	scores = {} # initialize an empty dictionary
	prepsentidict(senti_file, scores)
	print scores.items() # Print every (term, score) pair in the dictionary

if __name__ == '__main__':
    main()
