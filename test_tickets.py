import random
import time

def makeList(file):
    output = []

    for line in file:
        output.append(line.rstrip())

    return output

def makeTicket(string):
    strings = string.split(',')

    output = [int(s) for s in strings]

    return output

def generateRndTicket():
    #get 6 different numbers (cheap and dirty version)
    output = [random.randint(1, 59) for _ in range (0, 6)]

    for i in range (0, 6):
        while(output.count(output[i]) > 1):
            output[i] = random.randint(1, 59)


    return output



if __name__ == "__main__":
    #set random number seed
    random.seed(int(time.time()))

    #read tickets from file and make int list
    f = open("tickets.txt", 'r')
    asalist = makeList(f)
    tickets = [makeTicket(t) for t in asalist]
    ticket_len = len(tickets)

    #establish prizes
    prizes = [0, 0, 5, 30, 140, 1750, 4000000]

    #threshold for profit
    profit_threshold = ticket_len*2

    #set itterations and winnings
    itter = 100
    winnings = [0 for i in range (0, itter)]

    #compair against random lotto result
    for i in range (0, itter):
        total_win = [0 for _ in range (0, ticket_len)]
        rnd_lotto = generateRndTicket()
        for j in range (0, 6):
            for k in range (0, ticket_len):
                if(rnd_lotto[j] in tickets[k]):
                    total_win[k] += 1
        
        for tot in total_win:
            winnings[i] += prizes[tot]

    #output variables
    total_earnings = 0
    total_times_profiting = 0
    total_wins = 0

    #total winnings
    for win in winnings:
        total_earnings += win
        if win > 0:
            total_wins += 1
        if win > profit_threshold:
            total_times_profiting += 1

    #print results
    print("number of wins:", total_wins)
    print("percentage wins:", (total_wins/itter)*100)
    print("number of times profiting:", total_times_profiting)
    print("percentage profiting:", (total_times_profiting/itter)*100)
    print("total earnings:", total_earnings)
    if(total_earnings < profit_threshold * itter):
        print("total LOSS:", profit_threshold * itter - total_earnings)
        print("better luck next time")
    elif(total_earnings == profit_threshold * itter):
        print("you BROKE EVEN")
        print("in the circumstances, well done")
    else:
        print("total PROFIT:", total_earnings - profit_threshold * itter)
        print("well done")
