import QtQuick 2.15

Rectangle{
  id: play
  width: 150; height: 40
  x: 0
  color: "gold"
  border.color: "black"
  border.width: 2

  property alias txt: text_play.text
  property alias py: play.y
  property int play_id: 0

  Text{
    id: text_play
    color: "black"
    font.pointSize: 10
    topPadding: 10; leftPadding: 15
  }

  MouseArea{
    anchors.fill: parent
    onClicked: {
      con.set_new_play_to_preview(play.play_id)
      playloader.source = ""
      playloader.source = "VisualPlay.qml"
    }
  }
}