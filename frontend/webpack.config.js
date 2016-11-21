const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: './frontend/index.js',

  output: {
    filename: 'static/bundle.js',
    publicPath: ''
  },

  plugins: [
        new HtmlWebpackPlugin({
            template: path.join(__dirname, '/frontend/index.html'),
            hash: true,
            filename: 'static/index.html',
            inject: 'body'
        }),
    ],

  module: {
    loaders: [
      { test: /\.js$/, exclude: /node_modules/, loader: 'babel-loader?presets[]=es2015&presets[]=react' }
    ]
  }
}