import QtQuick 2.0

Image{
  id: lineman
  property alias px: lineman.x
  property alias py: lineman.y
  
  width: 25; height: 25
  source: "pictures/player.png"
}