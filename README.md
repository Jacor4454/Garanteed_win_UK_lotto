# Garanteed_win_UK_lotto
a program to generate 27 random tickets that guarantee a win in the national lottery UK[^1]

this code is based on [this paper](https://arxiv.org/abs/2307.12430) and this [Matt Parker video](https://www.youtube.com/watch?v=zYkmIxS4ksA)

##generate_ticket.py
generate_ticket.py will shuffle the national lotto numbers, then generate 5 hypergraphs (as per the paper) to make 27 tickets. The code with stop after every step and wait for the user to press enter to continue so you cna see the maths too. The results are also saved to a file (tickets.txt).

##test_ticket.py
test_tickets.py will make a list of the tickets in tickets.txt and generate a given number of lotto draws, calculating total and percentage wins, total and percentage of time you'd make a profit, total revenu and total profit

tickets.txt does not have to be 27 tickets long for test_tickets.py so feel free to make your own ticket or tickets (following the format "xx,xx,xx,xx,xx,xx") and see how oftern you'd win

##tickets.txt
I have added a default tickets.txt, it isn't neccisary as generate_ticket.py will generate tickets too but there it is if you're only wanting to test lottery tickets


[^1]: disclaimer: I know the maths is there, but even so I am saying nothing is garanteed, computers go wrong, so if you don't win cos the code bugged out, don't complain to me
