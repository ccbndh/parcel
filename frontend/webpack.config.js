const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: './index.js',

  output: {
    path: 'dist',
    filename: '/bundle.js',
  },

  plugins: [
        new HtmlWebpackPlugin({
            template: path.join(__dirname, '/index.html'),
            hash: true,
            filename: 'index.html',
            inject: 'body'
        }),
    ],

  module: {
    loaders: [
      { test: /\.js$/, exclude: /node_modules/, loader: 'babel-loader?presets[]=es2015&presets[]=react' }
    ]
  }
}