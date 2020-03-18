import React from 'react'
import './Menu.css'

const buttons = ['fast', 'slow', 'cute', 'eek']

class Menu extends React.Component {
  constructor (props) {
    super(props)
    this.handleClick = this.handleClick.bind(this)
  }

  renderButtons () {
    return buttons.map(button => {
      return <p onClick={this.handleClick}>{button}</p>
    })
  }

  handleClick (e) {
    this.props.onClick(e.target.innerHTML)
  }

  render () {
    return (
      <div className='menu'>
        {this.renderButtons()}
      </div>
    )
  }
}

export default Menu
