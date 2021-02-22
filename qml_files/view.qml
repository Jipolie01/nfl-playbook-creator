import QtQuick 2.15
import QtQuick.Window 2.0

Window{
    width: 950; height:700 
    visible: true
    title: "Play drawer"

    PlaySelector{number_of_plays: con.get_number_of_plays()}

    Loader{
      id: playloader
    }
}