var HtmlWebpackPlugin = require('html-webpack-plugin')
var HTMLWebpackPluginConfig = new HtmlWebpackPlugin({
  template: __dirname + '/templates/nuggetsapp/index.html',
  filename: 'index.html',
  inject: 'body'
});

module.exports = {
  entry: [
    './static/js/index.jsx'
  ],
  output: {
    path: __dirname + '/static/js',
    filename: "index_bundle.js"
  },
  resolve: {
    extensions: ['', '.js', '.jsx']
  },
  module: {
    loaders: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        loader: "babel-loader"
      },
    ]
  },
  plugins: [HTMLWebpackPluginConfig]
};
