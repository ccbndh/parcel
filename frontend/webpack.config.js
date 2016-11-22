const path = require('path');
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');

const VENDOR = [
    'history',
    'react',
    'react-dom',
    'react-router',
    'jquery',
];

module.exports = {
  entry: {
    app: './index.js',
    vendor: VENDOR,
  },

  output: {
        filename: '[name].js',
        path: 'dist',
        publicPath: '/'
    },

  plugins: [
        new HtmlWebpackPlugin({
            template: path.join(__dirname, '/index.html'),
            hash: true,
            filename: 'index.html',
            inject: 'body'
        }),
        new webpack.ProvidePlugin({
            '$': 'jquery',
            'jQuery': 'jquery',
            'window.jQuery': 'jquery'
        }),
    ],

  module: {
    loaders: [
      { test: /\.js$/, exclude: /node_modules/, loader: 'babel-loader?presets[]=es2015&presets[]=react' }
    ]
  }
};