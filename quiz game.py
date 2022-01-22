def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("--------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter your answer (A,B,or C ) - ")
        guess = guess.upper()
        guesses.append(guess)
        
        correct_guesses += check_answer(questions.get(key),guess)

        question_num+=1
    display_score(correct_guesses , guesses)

#####################################################################

def check_answer(answer , guess):
    if answer == guess:
        print("CORRECT!!!!")
        return 1
    else :
        print("WRONG!!!")
        return 0

#####################################################################

def display_score(correct_guesses , guesses):
    print("-----------------------------")
    print("RESULTS - ")
    print("-----------------------------")
    print("Answers are - ",end = " ")
    for i in questions:
        print(questions.get(i),end = " ")
    print()
    print("Guesses Are - ", end = " ")
    for i in guesses:
        print(i,end = " ")
    print()

    score = int((correct_guesses/len(questions)*100))
    print("Your Score Is :- "+str(score)+"%")

###############################################################

def play_again():
    response = input("Do You Want To Play Again ? (Yes/No) - ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

################################################################

questions = {"who created Python ?":"A",
              "what year was python created ":"B",
              "Python is tributed to which comedy group ":"C",
              "Is the Earth Round ?":"A"
            }

options = [["A. Guido Van Rossum","B. Elon MUsk","C. Bill Gates "],
           ["A. 1989","B.1991","C.2000"],
           ["A. Lonely Island","B. Smosh","C. Monty Python"],
           ["A. True","B. False","C. Sometimes"]]

new_game()

while play_again():
    new_game()

print("Byeeeee.....")