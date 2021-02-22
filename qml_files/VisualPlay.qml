import QtQuick 2.15

Rectangle{
  id: visual_play

  width: 800; height: 700
  x: 150
  color: "white"

  Lineman{px: 270; py: 500}
  Lineman{px: 300; py: 500}
  Lineman{px: 330; py: 500}
  Lineman{px: 360; py: 500}
  Lineman{px: 390; py: 500}

  Quarterback{px: con.get_x_position_of_player(0); py: con.get_y_position_of_player(0)}

  SkillPlayer{
    px: con.get_x_position_of_player(1); py: con.get_y_position_of_player(1) 
    rfx: con.get_route_first_x(1); rsy: con.get_route_second_y(1)   
    rsx: con.get_route_second_x(1) 
  }

  SkillPlayer{
    px: con.get_x_position_of_player(2); py: con.get_y_position_of_player(2) 
    rfx: con.get_route_first_x(2); rsy: con.get_route_second_y(2)   
    rsx: con.get_route_second_x(2) 
  }
    
  SkillPlayer{
    px: con.get_x_position_of_player(3); py: con.get_y_position_of_player(3) 
    rfx: con.get_route_first_x(3); rsy: con.get_route_second_y(3)   
    rsx: con.get_route_second_x(3) 
  }

  SkillPlayer{
    px: con.get_x_position_of_player(4); py: con.get_y_position_of_player(4) 
    rfx: con.get_route_first_x(4); rsy: con.get_route_second_y(4)   
    rsx: con.get_route_second_x(4) 
  }

  SkillPlayer{
    px: con.get_x_position_of_player(5); py: con.get_y_position_of_player(5) 
    rfx: con.get_route_first_x(5); rsy: con.get_route_second_y(5)   
    rsx: con.get_route_second_x(5) 
  }
}