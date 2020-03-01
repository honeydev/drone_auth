const path = require('path');

module.exports = {
  outputDir: path.resolve(__dirname, './dist'),
  publicPath: 'static/',
  configureWebpack: {
    devtool: 'source-map'
  }
};
