from dataclasses import dataclass, field


@dataclass(order=True)
class FootballPlayer:
    name: str = field(compare=False)
    surname: str = field(compare=False)
    value: int = field(repr=False)


@dataclass
class FootballTeam:
    name: str
    players: list = field(default_factory=list, repr=False, compare=False)

    def add_players(self, *args):
        self.players.extend(list(args))

player1 = FootballPlayer('Ronaldo', '', 20000000)
player2 = FootballPlayer('Lothar', 'Matthaus', 250000000)
player3 = FootballPlayer('Xavi', 'Simons', 54000000)
player4 = FootballPlayer('Paolo', 'Maldini', 28000000)
player5 = FootballPlayer('Лев', 'Яшин', 200000000)
player6 = FootballPlayer('Diego', 'Maradona', 305000000)
player7 = FootballPlayer('Lionel', 'Messi', 180000000)
player8 = FootballPlayer('Kristiano','Ronaldo',10000000)

team = FootballTeam('Best')
print(team.name)

team.add_players(player1, player2, player3, player4, player5, player6, player7, player8)
print(team.players)