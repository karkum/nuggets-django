var React = require('react');
var ReactRouter = require('react-router');
var Link = ReactRouter.Link
var MainContainer = require('../containers/MainContainer');

function Home () {
  return (
    <MainContainer>
      <h1>Welcome to Nuggets</h1>
      <p className='lead'>Remember everything you learn</p>
      <Link to='/myNuggets'>
        <button type='button' className='btn btn-lg btn-success'>See my nuggets</button>
      </Link>
    </MainContainer>
  )
}

module.exports = Home;
