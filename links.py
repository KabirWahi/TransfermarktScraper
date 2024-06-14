import networkx as nx
import pickle
import csv

messi = '28003'
marco_reus = '35207'
olise = '566723'
writz = '598577'
mbappe = '342229'
kane = '132098'

players = {}
player_file = 'players.csv'

with open(player_file, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        players[row[1]] = row[2]

with open('graph.gpickle', 'rb') as file:
    G = pickle.load(file)

def print_all_shortest_paths(player1, player2):
    for path in nx.all_shortest_paths(G, source=player1, target=player2):
        for player_id in path:
            print(f'{players[player_id]} ({player_id})')
        print('')

while True:
    player1 = input('Enter player 1 ID: ')
    if player1 not in players:
        print('Invalid player ID')
        continue
    else:
        print(players[player1])
    player2 = input('Enter player 2 ID: ')
    if player2 not in players:
        print('Invalid player ID')
        continue
    else:
        print(players[player2])
    print_all_shortest_paths(str(player1), str(player2))