var React = require('react');
var Search = require('./Search');
var PropTypes = React.PropTypes;

var Navbar = React.createClass({
  render: function () {
    var search;
    if (this.props.showSearch) {
      search = <Search />;
    }
    return (
      <div className="navbar navbar-fixed-top">
        <div className="navbar-inner">
          <img src="/static/img/nuggets_logo_notext.png" className="pull-left navbar-icon"/>
          <span className="brand">Nuggets</span>
          {this.props.username}
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

{/*}
    <div className="jumbotron col-sm-6 col-sm-offset-3 text-center">
      <h1>{props.header}</h1>
      <div className="col-sm-12">
        <form onSubmit={props.onSubmitUser}>
          <div className="form-group">
            <input
              className='form-control'
              onChange={props.onUpdateUser}
              placeholder='Github Username'
              type='text'
              value={props.username} />
          </div>
          <div className="form-group col-sm-4 col-sm-offset-4">
            <button
              className="btn btn-block btn-success"
              type="submit">
                Continue
            </button>
          </div>
        </form>
      </div>
    </div>
Navbar.propTypes = {
  onSubmitUser: PropTypes.func.isRequired,
  onUpdateUser: PropTypes.func.isRequired,
  header: PropTypes.string.isRequired,
  username: PropTypes.string.isRequired,
}
*/}
module.exports = Navbar;
