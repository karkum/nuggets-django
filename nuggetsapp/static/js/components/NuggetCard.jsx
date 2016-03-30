var React = require('react')
var ReactRouter = require('react-router')
var Link = ReactRouter.Link;

var NuggetCard = React.createClass({
  render: function () {
    return (
      <div className="span4">
        <div className="row-fluid f2">
          <div className="nugget-wrapper" id="g3">
            <Link to='/playerOne'>
              <div id="mGGDs6QBxS" className="nugget-content">
                <p>{this.props.text}</p>
                <div className="nugget-tag-section">{this.props.tags}</div>
                <div className="row-fluid nugget-time-ago">
                  <span>{this.props.created_at}</span>
                </div>
              </div>
            </Link>
            <div className="nugget-toolbar">
              <span className="span1 fa nugget-action-icons">
                <span className="nugget-action-icons-left">
                  <a className="fa-link nugget-action-icon" target="_blank" href="{this.props.url}"></a>
                  <a className="fa-twitter nugget-action-icon" target="_blank" href="www.twitter.com"></a>
                </span>
              </span>
            </div>
          </div>
        </div>
      </div>
    )
  }
});

{/*
NuggetCard.propTypes = {
  year: React.PropTypes.string.isRequired,
  poster: React.PropTypes.string.isRequired,
  description: React.PropTypes.string.isRequired,
  title: React.PropTypes.string.isRequired,
  id: React.PropTypes.number.isRequired
}*/}

module.exports = NuggetCard;
