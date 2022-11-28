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
    parser.add_argument('--players', type=int, default=1)
    args = parser.parse_args()
    print(random.sample(players(), args.players))


if __name__ == '__main__':
    main()
