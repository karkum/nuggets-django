var webpack = require('webpack');

module.exports = {
  entry: [
    './static/js/index.jsx'
  ],
  output: {
    path: __dirname + '/static/build/',
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
  plugins: [
    new webpack.optimize.UglifyJsPlugin({
      compress: {
        warnings: false
      }
    })
  ]
};
