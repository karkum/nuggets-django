var React = require('react');

function MainContainer (props) {
  return (
    <div className="jumbotron col-sm-12 text-center main-container">
      {props.children}
    </div>
  )
}

module.exports = MainContainer;
