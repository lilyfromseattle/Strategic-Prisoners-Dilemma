playerscore = 0
# The player's score 
compscore = 0
# The computer's score
actionlist = 0
# This variable will be used as an index to access the items in the list below 
anlist = ["No"]
# The first action using 'Tit for Tat' strategy is to cooperate; in this case, not confessing 
print "Welcome to the Prisoner's Dilemma"
print "You and your partner have been caught on a bank robbing spree. You are sequestered in separate interogation rooms. You will each be given the chance to confess to or deny each individual robbery on your 30-bank spree. If you both deny a crime you will each receive one year added to your sentences. If you both confess to a crime you will each receive 2 years added to your sentences. If one of you confesses and the other does not the confessor will have 0 years added to his sentence while his partner receives 3 more years."
# The backstory
print " "
for turn in range(1, 31):
    print "Crime #" + str(actionlist + 1)
    playeraction = raw_input("Do you confess to this crime?")
# This is the player's action based on their input
    anlist.append(playeraction)
# This will add the player's action to the list anslist
    compaction = anlist[actionlist]
# This will make the computer's move the same as the player's last move
    if playeraction == "Yes" or playeraction == "yes" or playeraction == "No" or playeraction == "no":
        if (compaction == "Yes" or compaction == "yes") and (playeraction == "Yes" or playeraction == "yes"):
            playerscore = playerscore + 2
            compscore = compscore + 2
            actionlist = actionlist + 1
            print " "
            print "Both you and your partner confessed. You both receive 2 year sentences."
            print " "
            print "Your Sentence: " + str(playerscore)
            print "Partner's Sentence: " + str(compscore)
            print " "
            
        elif (compaction == "Yes" or compaction == "yes") and (playeraction == "No" or playeraction == "no"):
            playerscore = playerscore + 2
            compscore = compscore + 2
            actionlist = actionlist + 1
            print " "
            print "Your opponent has confessed. You receive 3 years. He receives no sentence."
            print " "
            print "Your Sentence: " + str(playerscore)
            print "Partner's Sentence: " + str(compscore)
            print " "
                
        elif (compaction == "No" or compaction == "no") and (playeraction == "Yes" or playeraction == "yes"):
            playerscore = playerscore + 0
            compscore = compscore + 3
            actionlist = actionlist + 1
            print " "
            print "You confessed and your partner denied the crime. He receives 3 years. You receive no sentence."
            print " "
            print "Your Sentence: " + str(playerscore)
            print "Partner's Sentence: " + str(compscore)
            print " "
                
        elif (compaction == "No" or compaction == "no") and (playeraction == "No" or playeraction == "no"):
            playerscore = playerscore + 1
            compscore = compscore + 1
            actionlist = actionlist + 1
            print " "
            print "Both you and your opponent denied the crime. You each receive 1 year."
            print " "
            print "Your Sentence: " + str(playerscore)
            print "Partner's Sentence: " + str(compscore)
            print " "
    else:
        print "Please enter Yes or No."#!/usr/bin/env python#!/usr/bin/env python

if turn == 31:
    print " "
    print "Game Over"
    print " "
    print "Your Final Sentence: " + str(playerscore) + " years"
    print "Partner's Final Sentence: " + str(compscore) + " years"
    # Ends the game after 30 turns