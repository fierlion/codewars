import math

def movie_generator(card, ticket, perc):
    total = card
    print ("total: %d" % total)
    times = 1
    systema_total = 0
    while systema_total <= math.ceil(total):
        perc_total = math.pow(perc, times)
        new_result = ticket * perc_total
        yield new_result
        systema_total += ticket
        total += new_result
        times += 1

def movie(card, ticket, perc):
    mg = movie_generator(card, ticket, perc)
    return sum(1 for x in mg)

if __name__=='__main__':
    print (movie(500, 15, 0.9))
    print ("should be 43")
    print (movie(100, 10, 0.95))
    print ("should be 24")
    print (movie(0, 10, 0.95))
