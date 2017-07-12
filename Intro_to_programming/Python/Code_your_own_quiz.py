def main():
    vaild = False
    while not vaild:
        print_instructions()

def print_instructions():
    print 'sup mother fuckers, this is a game. pick one of the 3 difficulties: easy, medium or hard'
    try:
        mode_choice = raw_input("choose something....")
        if (mode_choice == "easy"):
            print ("man, yur weak for choosing this... :(")
            easy_board(0)
        elif (mode_choice == "medium"):
            print ("your ok, man..")
        elif (mode_choice == "hard"):
            print ("ohhh fancy.")
        else:
            print "nah son"
    except Exception as e:
        print user + " yoh dog.. that word not valid yoh.."
def easy_board(counter_limit):
    print "What's 1 + 1?"
    input_Easy = raw_input()
    if(input_Easy == str(2)):
        print "nice job u bitc"
        def easy_board_round2(0)

    else:
        print "nice try, but u rong"
        if (counter_limit >= 2):
            print "fuck you"
        else:
            easy_board(counter_limit + 1)
def easy_board_round2(counter_limit):

if __name__=="__main__":
    main()
