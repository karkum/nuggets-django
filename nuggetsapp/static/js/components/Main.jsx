var React = require('react');
var Navbar = require('../components/Navbar');
{/*
var ReactCSSTransitionGroup = require('react-addons-css-transition-group');
require('../main.css');
*/}

var Main = React.createClass({
  render: function () {
    return (
      <div className='full-container'>
        <Navbar />
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
