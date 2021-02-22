import QtQuick 2.15

Rectangle{
  id: sidebar
  width: 150; height: 700
  color: "gray"

  property int number_of_plays: 0
  property var plays : []

  Component.onCompleted:{
    var y_position = 0
    for(var i = 0; i < number_of_plays; i++){
      var component = Qt.createComponent("Play.qml")
      plays.push(component.createObject(parent, {txt:  con.get_playname(i), py : y_position, play_id: i }))
      y_position += 40
    }

  }

}