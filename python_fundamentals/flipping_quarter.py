import random



def coin_flip():
    tails = 0
    heads = 0
    for flip in range(1,5001):
        random_num = random.random()
        rounded_num = round(random_num)
        if(rounded_num == 1.0):
            tails += 1
            print 'Attemp #' + str(flip) + ': Throwing a coin... It\'s tails! ... Got ' + str(tails) + ' tail(s) so far and ' + str(heads) + ' head(s) so far'
        if(rounded_num == 0.0):
            heads += 1
            print 'Attemp #' + str(flip) + ': Throwing a coin... It\'s heads! ... Got ' + str(tails) + ' tail(s) so far and ' + str(heads) + ' head(s) so far'
        

coin_flip()

