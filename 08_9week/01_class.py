class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

if __name__ == "__main__":
    ronaldo = SoccerPlayer("Cristiano Ronaldo", "attacker", 7)
    messi = SoccerPlayer("Lionel Messi", "attacker", 10)

    print(ronaldo.name, ronaldo.position, ronaldo.back_number)
    print(messi.name, messi.position, messi.back_number)