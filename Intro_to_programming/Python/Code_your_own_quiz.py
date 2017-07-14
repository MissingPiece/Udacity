import sys

def main():
    """ Intended: Have a start point and an ordered path: no input, no output """
    vaild = False
    while vaild == False:
        print_instructions ()
        game_start ()

def print_instructions ():
        """ Intended: Print instructions to console: no input, no output """
    print "this is a game. pick one of the 3 difficulties: easy, medium or hard. And then follow the prompts."

def game_start ():
            """ Intended: Have user pick a mode, and call the next function: no input, no output """
    mode_choice = raw_input("choose something....")
    try:
        if (mode_choice == "easy"):
            print ("weak sauce")
            easy_board()
        elif (mode_choice == "medium"):
            print ("mild.")
            #medium_board(0)
        elif (mode_choice == "hard"):
            print ("diablo 3 on hardcore")
            #hard_board(0)
        else:
            print "nah son, be real"
    except Exception as e:
        print ("invalid input")

def game_end ():
    """ Intended: Print a prompt and exit the program : No input, No output"""
    print "Congratulations! You've won!" + '\n'
    sys.exit( "you're done here, reload and try a different difficulty" )

def easy_board ():
    """ Inteded: Guide users through questions for accurate answers, within a certain number of tries and finish the game : No input, no output"""
    counter_limit, index = 0,0
    placement_holder = ['Answer 1','Answer 2','Answer 3','Answer 4']
    answer_Key = ['2','6','36','18']

    text = "What is 1 + 1? " + placement_holder[0] + '\n' + "What is answer 1 multiplied by 3? " + placement_holder[1] + '\n' + "What is answer 2 squared? " + placement_holder[2] + '\n' + "Answer 3 divided by 2? " + placement_holder[3]

    while(counter_limit < 2):
        text = "What is 1 + 1? " + placement_holder[0] + '\n' + "What is answer 1 multiplied by 3? " + placement_holder[1] + '\n' + "What is answer 2 squared? " + placement_holder[2] + '\n' + "Answer 3 divided by 2? " + placement_holder[3]+ '\n'
        print text

        input_Easy = raw_input("Your answer for  " + placement_holder[index])
        if(input_Easy == answer_Key[index]):
            if(index == 3):
                placement_holder[index] = answer_Key[index]
                game_end()

            else:
                placement_holder[index] = answer_Key[index]
                index += 1
                counter_limit = 0
        else:
            counter_limit +=1
            print "Wrong, try again you have " + str(3 - counter_limit) + " try(ies) left"

if __name__=="__main__":
    main()
