var React = require('react');
var Search = require('./Search');
var PropTypes = React.PropTypes;

var Navbar = React.createClass({
  render: function () {
    var search;
    if (this.props.showSearch) {
      search = <Search onSearchUpdate={this.props.onSearchUpdate} />;
    }
    return (
      <div className="navbar navbar-fixed-top">
        <div className="navbar-inner">
          <img src="/static/img/nuggets_logo_notext.png" className="pull-left navbar-icon"/>
          <span className="brand">Nuggets</span>
          
          DJANGO: &nbsp;
          <a href="/">Home/Login</a> | &nbsp;
          <a href="/my-nuggets">My Nuggets</a> | &nbsp;
          <a href="/add-nugget">Add Nugget</a> | &nbsp;
          <a href="/logout">Logout</a> | &nbsp;
          <br></br>
          REACT: &nbsp;
          <a href="/react">Home</a> | &nbsp;
          <a href="/react#/myNuggets">My Nuggets</a> | &nbsp;
          <a href="/react#/addNugget">Add Nugget</a> | &nbsp;
          <br></br>
          (Logged in as {window.nuggets.app_state.user.username})

          <div className="navbar-dropdown">
            <div className="btn-group pull-right">
              <button className="btn btn-small dropdown-toggle" data-toggle="dropdown" tabIndex="-1"><i className="icon-th-list"></i></button>
              <ul className="dropdown-menu pull-right">
                <li><a href="create">Create a nugget</a></li>
                <li className="divider"></li>
                <li><a id="logout-button" href="#">Logout</a></li>
              </ul>
            </div>
          </div>
          {search}
        </div>
      </div>
    )
  }
});

module.exports = Navbar;
