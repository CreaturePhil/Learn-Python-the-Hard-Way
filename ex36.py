from sys import exit

def procrastinate():
	print "You fucked up."
	print "Don't worry. You got some pussy. :)"
	print "But then you died. :("
	end("At least you got some pussy in this lifetime.")
	
def assignment():
	print "You finish your assignment. Nice job!"
	print "Now what do you want to do?"
	
	while True:
		input = raw_input("> ")
		
		if input == "sleep":
			end("Good night")
		elif input == "idk":
			end("")
		elif input == "42":
			print "You win!"
			count = 0
			while True:
				for i in ["/","-","|","\\","|"]:
					print "%s\r" % i,
				count += 1
				if count == 1000:
					exit(0)
		else:
			end("Too bad so sad.")

def end(msg):
	print "Game Over!", msg
	exit(0)

def start():
	print "You have an assignment due this Friday."
	print "What do you do?"
	print "\n1.Procrastinate\n2.Finish the Assignment\n3.Sleep"
	
	while True:
		input = raw_input("> ").lower()
		
		if input == "procrastinate":
			procrastinate()
		elif input == "finish the assignment" or input == "assignment":
			assignment()
		elif input == "sleep":
			end("Did you expect something? At least you got some good sleep right?")
		else:
			print "Try again."

start()