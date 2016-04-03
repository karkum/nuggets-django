var React = require('react')
var axios = require('axios');
var MainContainer = require('../containers/MainContainer');
var Search = require('../components/Search')
var NuggetCard = require('../components/NuggetCard')

var MyNuggetsContainer = React.createClass({
  getInitialState: function () {
    return {
      my_nuggets: [],
      searchText: ''
    }
  },
  handleSearchUpdate: function (e) {
    this.setState({
      searchText: e.target.value
    });
  },
  componentDidMount: function () {
    axios.get("/api/get-my-nuggets")
      .then(function(json) {
        console.log(json);
        this.setState({
          my_nuggets: json.data
        });
        console.log("success");
      }.bind(this))
      .catch(function(err) {
        console.warn(err);
      })
  },
  render: function () {
    return (
      <MainContainer>
        <div className="row-fluid">
          <div id="profile-header" className="">
            <div className="jumbotron">
              <div className="backgroundOne"> </div>
              <h1><span id="displayname">{window.nuggets.app_state.user.full_name}</span></h1>
              <p><span id="tagline">super user of Nuggets, avid learner</span></p>
            </div>
          </div>
          <Search onSearchUpdate={this.handleSearchUpdate} searchText={this.state.searchText} />
          <div id="my-nuggets-table">
            {this.state.my_nuggets
              .filter(function(nugget) {
                if (!this.state.searchText || (nugget.text + " " + nugget.tags + " " + nugget.source).toLowerCase().indexOf(this.state.searchText.toLowerCase()) >= 0) {
                  return nugget;
                }
              }.bind(this))
              .map(function(nugget) {
                return (<NuggetCard {...nugget} key={nugget.id} />)
              })
            }
          </div>
        </div>
      </MainContainer>
    )
  }
});

            
{/*}            
MyNuggetsContainer.propTypes = {
  shows: React.PropTypes.arrayOf(React.PropTypes.object),
  searchTerm: React.PropTypes.string
}*/}

module.exports = MyNuggetsContainer;
