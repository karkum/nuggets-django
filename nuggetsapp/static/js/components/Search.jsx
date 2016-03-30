const React = require('react')

function Search (props) {
  return (
    <div id="my-nuggets-search-div" className="pull-right" style={{display: 'block'}}>
      <div className="span4">   
        <span id="my-nuggets-search-icon"><i className="icon-search"></i></span>
        <input id="my-nuggets-search" type="text" placeholder="Search"/>
        <span id="my-nuggets-search-clear"><i className="icon-remove"></i></span>
      </div>
    </div>
  )
}

{/*}
Search.propTypes = {
  shows: React.PropTypes.arrayOf(React.PropTypes.object),
  searchTerm: React.PropTypes.string
}*/}

module.exports = Search;
