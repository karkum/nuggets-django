var React = require('react');
var ReactRouter = require('react-router');
var Router = ReactRouter.Router;
var Route = ReactRouter.Route;
var hashHistory = ReactRouter.hashHistory;
var IndexRoute = ReactRouter.IndexRoute;
var Main = require('./components/Main');
var Home = require("./components/Home");
var MyNuggetsContainer = require('./containers/MyNuggetsContainer');
var AddNuggetContainer = require('./containers/AddNuggetContainer');

var routes = (
  <Router history={hashHistory}>
    <Route path='/' component={Main}>
      <IndexRoute component={Home} />
      <Route path='myNuggets' component={MyNuggetsContainer} />
      <Route path='addNugget' component={AddNuggetContainer} />
    </Route>
  </Router>
);

module.exports = routes;
