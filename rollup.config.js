module.exports = {

  plugins: [
    require('rollup-plugin-commonjs')(),
    require('rollup-plugin-node-resolve')(),
    require('rollup-plugin-buble')(),
    require('rollup-plugin-optimize-js')()
  ]
}
