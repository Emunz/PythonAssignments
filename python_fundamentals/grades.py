from random import randint

def scores_and_grades():
    for num in range(0,10):
        score = randint(60,100)
        if(score >= 90):
            print 'Score: ' + str(score) + '; Your grade is A'
        elif(score >= 80):
            print 'Score: ' + str(score) + '; Your grade is B'
        elif(score >=70):
            print 'Score: ' + str(score) + '; Your grade is C'
        else:
            print 'Score: ' + str(score) + '; Your grade is D'
    print 'End of the program. Bye!'

scores_and_grades()