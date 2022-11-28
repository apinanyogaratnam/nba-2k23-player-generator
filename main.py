import random


def players():
    return [
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
    ]

def main():
    random_player = random.choice(players())
    print(random_player)
