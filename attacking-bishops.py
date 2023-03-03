#Attacking Bishops
#
#
#Problem Description
#On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.
#
#You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).
#
#For example, given M = 5 and the list of bishops:
#
#(0, 0)
#(1, 2)
#(2, 2)
#(4, 0)
#The board would look like this:
#
#[b 0 0 0 0]
#[0 0 b 0 0]
#[0 0 b 0 0]
#[0 0 0 0 0]
#[b 0 0 0 0]
#You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.


#Explanation:
#This problem is relatively straightforward since all we need to do is return how many bishops are attacking each other. 
#If the prompt asked us to return which bishop is attacking which then we would need to keep track of more data.
#Since the simpler is the case, the simplest way to do this is to cycle through the list of bishops and see if the slope between them is 1 or -1.
#If this is true then they are attacking each other, otherwise they are not.
#Since we are simply cycling through the bishops, it is necessarily true that we will get exatly double the number of attacks.
#The reason why is because we only care about whether an attack is happening not which side it is coming from.

chessboard_w
chessboard_l
num_bishops = 0
bishop_locations = [num_bishops]

def draw_board(bishop_locations, chessboard_w, chessboard_l):
  

def count_attacks(bishop_locations):
  for i in bishop_locations:
    
