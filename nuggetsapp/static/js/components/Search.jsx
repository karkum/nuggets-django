const React = require('react')

function Search (props) {
  return (
    <div id="my-nuggets-search-div">
      <div className="row">   
        <span id="my-nuggets-search-icon"><i className="icon-search"></i></span>
        <input id="my-nuggets-search" type="text" placeholder="Search" onChange={props.onSearchUpdate} value={props.searchText} />
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
