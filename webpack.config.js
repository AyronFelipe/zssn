const path = require('path');
const webpack = require('webpack');

module.exports = {
    entry: './static/js/App.js',
    output: {
        path: path.resolve('./static/public'),
        publicPath: '/static/public/',
        filename: 'bundle.js'
    },
    module: {
        rules: [
            {
                test: /\.vue$/,
                use: {
                    loader: 'vue-loader'
                }
            },
            {
                test: /\.js$/,
                exclude: /(node_modules|bower_components)/,
                use: {
                    loader: 'babel-loader',
                }
            },
            {
                test: /\.(png|jpg|gif|svg)$/,
                loader: 'file-loader',
                options: {
                    name: '[name].[ext]?[hash]'
                }
            }
        ]
    },
    performance: {
        hints: false,
    },
    devtool: '#eval-source-map'
}