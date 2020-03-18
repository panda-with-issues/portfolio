import React from 'react'
import './App.css'
import Menu from '../Menu/Menu'
import Player from '../Player/Player'

const Videos = {
  fast: 'https://s3.amazonaws.com/codecademy-content/courses/React/react_video-fast.mp4',
  slow: 'https://s3.amazonaws.com/codecademy-content/courses/React/react_video-slow.mp4',
  cute: 'https://s3.amazonaws.com/codecademy-content/courses/React/react_video-cute.mp4',
  eek: 'https://s3.amazonaws.com/codecademy-content/courses/React/react_video-eek.mp4'
}

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = { src: Videos.fast }
    this.changeVideo = this.changeVideo.bind(this)
  }

  changeVideo (newVideo) {
    this.setState({ src: Videos[newVideo] })
  }

  render () {
    return (
      <main>
        <h1>Video Player</h1>
        <Menu onClick={this.changeVideo} />
        <Player src={this.state.src} />
      </main>
    )
  }
}

export default App
