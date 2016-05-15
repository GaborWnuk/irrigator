module.exports = {
    entry: __dirname + '/src/nuke/irrigator/web/static_src/js/index.jsx',
    output: {
        path: './src/nuke/irrigator/web/static',
        filename: 'app.js',
        publicPath: '/static/',
        library: 'App',
    },
    module: {
        loaders: [
            { test: /\.css$/, loader: 'style!css' },
            { test: /\.jsx?$/,
              exclude: /(node_modules|bower_components)/,
              loader: 'babel',
              query: { presets: ["es2015-loose", "react"],
                        plugins: ["add-module-exports"] }
            },
            { test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: "url-loader?limit=10000&mimetype=application/font-woff" },
            { test: /\.(ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: "file-loader" }
        ]
    },
};
