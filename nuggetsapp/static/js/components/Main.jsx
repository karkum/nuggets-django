var React = require('react');
var NavbarContainer = require('../containers/NavbarContainer');
{/*
var ReactCSSTransitionGroup = require('react-addons-css-transition-group');
require('../main.css');
*/}

var Main = React.createClass({
  render: function () {
    console.log(window.nuggets.app_state.user.username + " " + window.nuggets.app_state.user.email);
    return (
      <div className='full-container'>
        <NavbarContainer/>
      {/*        <ReactCSSTransitionGroup
          transitionName="appear"
          transitionEnterTimeout={500}
          transitionLeaveTimeout={500}>
        </ReactCSSTransitionGroup>
        */}
        {React.cloneElement(this.props.children, {key: this.props.location.pathname})}
      </div>
    )
  }
});

module.exports = Main;
