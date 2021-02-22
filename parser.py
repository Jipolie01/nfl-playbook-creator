from formations import * 
from routes import *
from offense import *

class parser():
  
  def parse_formation(self, formation):
    play_dictionary = {
      "I_FORMATION" : i_formation(), "SINGLE_BACK_SET": single_back_set(),
      "PRO_SET": pro_set(), "SHOTGUN_STANDARD": shotgun_standard(),
      "SHOTGUN_TRIPS": shotgun_trips(), "SPREAD": spread()}
    return play_dictionary.get(formation)

  def parse_receiver(self, receiver):
    receiver_parsing = receiver.split("=")
    route_direction = False
    #print(receiver_parsing)
    if(receiver_parsing[1] == "T"):
      route_direction = True

    receiver_dictionary = {
      "SLANT" : slant(route_direction), "FLAT": flat(route_direction),
      "CURL" : curl(), "COMEBACK": comeback(route_direction),
      "QUICK_OUT": quick_out(route_direction), "MEDIUM_OUT": medium_out(route_direction),
      "DEEP_OUT": deep_out(route_direction), "CORNER" : corner(route_direction),
      "POST": post(route_direction), "SKINNY_POST" : skinny_post(route_direction),
      "GO": go(), "FADE": fade(route_direction),
      "SHOOT": shoot(route_direction)
    }
    return receiver_dictionary.get(receiver_parsing[0])

  def parse_play(self, single_line):
    single_line = single_line.replace("\n", "")
    play_indicators = single_line.split(";")
    play_formation = self.parse_formation(play_indicators[1])
    receiver_list = []
    for i in range(2, 7):
      receiver_list.append(self.parse_receiver(play_indicators[i]))
    #print(receiver_list)
    return offense(play_indicators[0], quarterback(), receiver(receiver_list[0]), receiver(receiver_list[1]),
            receiver(receiver_list[2]), receiver(receiver_list[3]), receiver(receiver_list[4]), 
            play_formation)

#Example: {"SUPER_PLAY" : offense object}
class playbook_file():
  def __init__(self, play_dict):
    self.offense_plays_dict = play_dict

  def get_full_playbook_play(self, play_name):
    return self.offense_plays_dict.get(play_name)
  
  def get_number_of_plays(self):
    return len(self.offense_plays_dict)


class playbook():
  def __init__(self, path):
    self.factory_parsing = parser()
    self.offensive_playbook = self.convert_lines_to_playbook(self.read_file(path))
  
  def convert_lines_to_playbook(self, lines):
    plays = []
    for i in range(0, len(lines)):
      plays.append(self.factory_parsing.parse_play(lines[i]))
    
    return plays
  
  def read_file(self, path):
    line_list = []
    with open(path, 'r') as file:
      line_list = file.readlines()

    return line_list

  def get_number_of_plays(self):
    return len(self.offensive_playbook)

  def get_play(self, index):
    return self.offensive_playbook[index]

