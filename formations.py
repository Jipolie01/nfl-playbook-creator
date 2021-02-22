class formation():
  # WR1, WR2, TE, WR3, HB
  def __init__(self, quarterback, player1, player2, player3, player4, player5):
    self.player_list = [quarterback, player1, player2, player3, player4, player5]

class i_formation(formation):
  def __init__(self):
    formation.__init__(self, [330,530], [220,500], [480, 520], [420,500], [330,560], [330, 590])

class single_back_set(formation):
  def __init__(self):
    formation.__init__(self, [330,530], [150,520], [180,500], [420,500], [480,520], [330,590])

class pro_set(formation):
  def __init__(self):
    formation.__init__(self, [330, 530], [200,500], [480,520], [420,500], [360,560], [300,560])

class shotgun_standard(formation):
  def __init__(self):
    formation.__init__(self, [330, 560], [200,500], [480,520], [420,500], [170,520], [360,545])

class shotgun_trips(formation):
  def __init__(self):
    formation.__init__(self, [330,560], [500, 520], [530,520], [240,500], [210,520], [470,500])

class spread(formation):
  def __init__(self):
    formation.__init__(self,[330,530], [570,500], [470,520], [150,520], [110,500], [330, 590])