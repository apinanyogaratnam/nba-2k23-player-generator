import random
import argparse


def players() -> set:
    return set([
        'Fred VanVleet',
        'Kyle Lowry',
        'Devin Booker',
        'Stephen Curry',
        'James Harden',
        'Luka Doncic',
        'Damian Lillard',
        'Gianis Antetokounmpo',
        'Lebron James',
        'Klay Thompson',
        'Kevin Durant',
        'Michael Jordan',
        'Kobe Bryant',
        'Steve Nash',
        'Boban Marjanovic',
        'Kawhi Leonard',
        'MP',
        "Shaquille O'Neal",
    ])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--player_1', type=int, default=1)
    parser.add_argument('--player_2', type=int, default=1)
    args = parser.parse_args()

    generated_players = random.sample(list(players()), args.player_1 + args.player_2)
    player_1 = generated_players[:args.player_1]
    player_2 = generated_players[args.player_1:]

    print(f'Player 1: {player_1}')
    print(f'Player 2: {player_2}')


if __name__ == '__main__':
    main()
