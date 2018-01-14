import random
import operator

total_questions = 0
counter_correct = 0
counter_incorrect = 0
wrong_number_1 = []
wrong_op = []
wrong_number_2 = []
correct_answer = []
wrong_answer = []


want_play = True

while (want_play):
    number_1 = random.randint(1,12)
    number_2 = random.randint(1,12)
    
    my_operators = {'+':operator.add,
           '-':operator.sub,
           '*':operator.mul}
    ops = random.choice(list(my_operators.keys()))

    answer = my_operators.get(ops)(number_1, number_2)
    print str(number_1) + " " + str(ops) + " " + str(number_2) + " = ?"

    valid_input = False
    while (valid_input == False):
        user_answer = raw_input("")

        try: 
            user_answer = int(user_answer)
            total_questions += 1
            valid_input = True
        except ValueError:
            valid_input = False
            print "Please type a valid input."

        
    if int(user_answer) == answer:
        counter_correct += 1
        print "Correct! Great job!"
    elif int(user_answer) != answer:
        print "That answer is incorrect."
        wrong_number_1.append(number_1)
        wrong_op.append(ops)
        wrong_number_2.append(number_2)
        wrong_answer.append(user_answer)
        correct_answer.append(answer)

    no_continue = True
    while (no_continue):
        end_game_yes = ["yes", "Yes", "y", "Y"]
        end_game_no = ["no", "No", "n", "N", ""]
        end_game_question = raw_input("Do you want to continue playing? ")
        if end_game_question in end_game_yes:
            want_play = True
            no_continue = False
        elif end_game_question in end_game_no:
            want_play = False
            percent_score = (float(counter_correct)/total_questions) * 100
            print "Thanks for playing!"
            print "You had a total of " + str(total_questions) + " questions and you answered " + str(counter_correct) + " correctly. That leaves your grade at: " + str(percent_score) + "%"
            print "Here is a list of the questions answered incorrectly: "
            for x in range(len(wrong_answer)):
                print str(wrong_number_1[x]) + " " + str(wrong_op[x]) + " " + str(wrong_number_2[x]) + " = " + str(wrong_answer[x]) + " / correct answer: " + str(correct_answer[x])
            no_continue = False
        else:
            print "Please enter a valid response."

    




