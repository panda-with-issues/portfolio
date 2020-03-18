import React from 'react'
import './Player.css'

class Player extends React.Component {
  render () {
    return <video src={this.props.src} controls autostart autoPlay />
  }
}

export default Player
