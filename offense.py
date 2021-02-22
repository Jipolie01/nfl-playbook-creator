from formations import *
from routes import *

class player():
  def __init__(self):
    self.position = 0
  
  def set_position(self, position):
    self.position = position
  
class receiver(player):
  def __init__(self, route):
    player.__init__(self)
    self.route = route

class quarterback(player):
  def __init__(self):
    player.__init__(self)

class offense():
  def __init__(self, name, quarterback, player1, player2, player3, player4, player5, formation):
    self.player_list = [quarterback, player1, player2, player3, player4, player5]
    self.formation = formation
    self.name = name
    for index in range(len(self.player_list)):
      self.player_list[index].set_position(self.formation.player_list[index])
  
  def get_x_position_of_player(self, player):
    return self.player_list[player].position[0]

  def get_y_position_of_player(self, player):
    return self.player_list[player].position[1]
  
  def get_route_first_x(self, player):
    return self.player_list[player].route.height

  def get_route_second_y(self, player):
    return self.player_list[player].route.top_route
  
  def get_route_second_x(self, player):
    return self.player_list[player].route.x_top_route

  def get_play_name(self):
    return self.name