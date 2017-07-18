import sys

def main():
    """ Intended: Have a start point and an ordered path: no input, no output """
    vaild = False
    while vaild == False:
        print_instructions ()
        game_start ()

def print_instructions ():
    """ Intended: Print instructions to console: no input, no output """
    print "this is a game. pick one of the 3 difficulties: easy, medium or hard. And then follow the prompts. All answers will be in lower case form"
def game_start ():
    """ Intended: Have user pick a mode, and call the next function: no input, no output, but opens next order of function """
    mode_choice = raw_input("choose something....")
    try:
        if (mode_choice == "easy"):
            print ('\n' + "weak sauce" + '\n' )
            game_board("easy")
        elif (mode_choice == "medium"):
            print '\n' + "Not too hot, not too cold. Goldilocks"+ '\n'
            game_board("medium")
        elif (mode_choice == "hard"):
            print ('\n' + "hardest thing you'll ever do"+ '\n')
            game_board("hard")
        else:
            print "nah son, be real"
    except Exception as e:
        print ("invalid input")

def game_end ():
    """ Intended: Print prompts and exit the program : No input, No output"""
    print "Congratulations! You've won!" + '\n'
    sys.exit( "you're done here, reload and try a different difficulty" )

def true_end ():
    """Intended: fun ending to the hardest level"""
    print "Congratulations! You've won!" + '\n'
    sys.exit( "you're done here, I have no further questions for you." )

def game_board(mode_choice):
    """Intended: take the input and choose what set of questions and answers. Input: mode_choice. Output: none, but prompts template function"""
    if (mode_choice == "easy"):
        questions = ["What is 1 + 1? ","What is answer 1 multiplied by 3? ", "What is answer 2 squared? ","Answer 3 divided by 2? " ]
        answer_Key = ['2','6','36','18']
        template(questions, answer_Key,mode_choice)

    elif (mode_choice == "medium"):
        questions = ["What letter comes after?: {a, b, c}? ","What animal has stripes and looks like a donkey? ", "What sport is called the American Pasttime ? ","What sport is the modern American Pasttime ? "]
        answer_Key = ['d','zebra','baseball','football']
        template(questions, answer_Key,mode_choice)
    elif (mode_choice == "hard"):
        questions = ["Spinach is high in which mineral? ","What's the total number of dots on a pair of dice? ","Which planet is the closest to Earth? ","What is the tallest mammal?"]
        answer_Key = ['iron','42','venus','giraffe']
        template(questions, answer_Key,mode_choice)
    else:
        print 'something went wrong'

        #questions for medium and hard are from http://laffgaff.com/easy-trivia-questions-and-answers/
def template(questions,answer_Key,mode_choice):
    """ Inteded: Guide users through questions for accurate answers, within a certain number of tries and finish the game : Input mode_choice, questions and answer_Key : No output, but opens endings"""
    counter_limit, index = 0,0
    placement_holder = ['Answer 1','Answer 2','Answer 3','Answer 4']
    #while loop to go through the prompts to update answers and run the meat of the game
    #this gives the user 5 tries
    while(counter_limit < 4):
        text = questions[0] + placement_holder[0] + '\n' + questions[1] + placement_holder[1] + '\n' + questions[2] + placement_holder[2] + '\n' + questions[3] + placement_holder[3]
        print text
        input_answer = raw_input('\n' + "Your answer for  " + placement_holder[index]+ ' ')
        if(input_answer == answer_Key[index]):
            #Last answer, so you can end after this one
            if(index == 3):
                #Decided to give hard a different ending
                if(mode_choice == "hard"):
                    placement_holder[index] = answer_Key[index]
                    true_end()
                else:
                    placement_holder[index] = answer_Key[index]
                    game_end()

            else:
                placement_holder[index] = answer_Key[index]
                index += 1
                counter_limit = 0
        else:
            counter_limit +=1
            #let's the user know the number of attempts left.
            print '\n' + "Wrong, try again you have " + str(4 - counter_limit) + " try(ies) left" + '\n'

if __name__=="__main__":
    main()
