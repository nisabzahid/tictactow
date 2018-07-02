# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 03:13:43 2018

@author: nisabbinzabid
"""

board = { 'top-l':'','top-m':'','top-r':'',
             'mid-l':'','mid-m':'','mid-r':'',
             'low-l':'','low-m':'','low-r':''
           }

def printboard(board):
    print(board['top-l']+' |'+board['top-m']+' |'+board['top-r'])
    print('-+-+-')
    print(board['mid-l']+' |'+board['mid-m']+' |'+board['mid-r'])
    print('-+-+-')
    print(board['low-l']+' |'+board['low-m']+' |'+board['low-r'])
    
printboard(board)    
turn ='X'
for i in range(9):
    printboard(board)
    print('Turn for '+turn+'. Move on which space?')
    move =input()
    board[move]= turn
    if turn =='X':
        turn = 'O'
    else :
        turn = 'X'
    printboard(board) 
            
    
    