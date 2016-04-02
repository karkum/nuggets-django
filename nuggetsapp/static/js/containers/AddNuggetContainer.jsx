var React = require('react')
var axios = require('axios');
var MainContainer = require('../containers/MainContainer');

var AddNuggetContainer = React.createClass({
  getInitialState: function () {
    return {
      text: '',
      tags: '',
      source: ''
    }
  },
  handleChange: function (key) {
    return function (e) {
      var state = {};
      state[key] = e.target.value;
      this.setState(state);
    }.bind(this);
  },
  onSubmitForm: function () {
    axios.post("/api/add-nugget",
      {
        text: this.state.text,
        tags: this.state.tags,
        source: this.state.source
      })
      .then(function(json) {
        console.log(json);
        window.location.href = '/react#/myNuggets';
      })
      .catch(function(err) {
        console.warn(err);
      })
  },
  render: function () {
    return (
      <MainContainer>
        <div className="row-fluid">
          <form onSubmit={this.onSubmitForm}>
            What did you learn?:
            <textarea name="text" rows={4} cols={50} value={this.state.text} onChange={this.handleChange('text')} />
            <br></br>
            Tags:
            <input type="text" value={this.state.tags} onChange={this.handleChange('tags')} />
            <br></br>
            Source:
            <input type="text" value={this.state.source} onChange={this.handleChange('source')} />
            <br></br>
            <input type="submit" value="Add Nugget" />
          </form>
        </div>
      </MainContainer>
    )
  }
});

{/*         
AddNuggetContainer.propTypes = {
  shows: React.PropTypes.arrayOf(React.PropTypes.object),
  searchTerm: React.PropTypes.string
}*/}

module.exports = AddNuggetContainer;
