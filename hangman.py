import random
import turtle
		
def check(random_word):
	user = []
	for k in range(len(random_word)):
		user.append("_")
	#user = "_"* len(random_word)
	i, j = 0, 0
	while (j<6):
		if j==1:
			t = turtle.Turtle()
			t.circle(75,360)
		elif j==2:
			t.forward(100)
		elif j==3:
			t.backward(200)
			t.forward(100)
			t.right(90)
		elif j==4:
			t.forward(100)
		elif j== 5:
			t.right(45)
			t.forward(75)
			t.backward(75)
			t.left(90)
		if "".join(user) == random_word:
			print "You Win"
			exit(0)
		user_ip = raw_input("Guess a letter")
		for i in range(len(random_word)):
			if user_ip == random_word[i]:
				user[i] = random_word[i]
		display(user)
		if user_ip not in random_word:
			j+=1
	t.forward(75)
	print "you lose"
			#if user_ip in random_word:
def random_word():
	list1 = []
	i = random.randint(1,25)
	with open("words.txt") as fo:
				
		for line in fo:
			list1.append(line.strip())
	
	return list1[i]
	

def display(user):
	list_ = []
	for i in range(len(user)):
		list_.append(user[i] + " ")
	print "".join(list_)

def main():
	r = random_word().lower()
	print "_ " * len(r)
	check(r)

main()