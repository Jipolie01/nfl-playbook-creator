import QtQuick 2.0 
import QtQuick.Shapes 1.15

Item{
  property alias px : receiver.x
  property alias py : receiver.y
  property alias rfx : before_break.relativeY
  property alias rsy : after_break.relativeY
  property alias rsx : after_break.relativeX
 
  Image{
    id: receiver
    width: 23; height: 23
    source: "pictures/receiving_player.png"
  }

  Shape{
    ShapePath{
      strokeColor: "black"
      strokeWidth: 4
      fillColor: "transparent"
      startX: receiver.x + 12; startY: receiver.y - 7

      PathLine{ id: before_break; relativeX: 0}
      PathLine{ id: after_break}
    }
  }
}