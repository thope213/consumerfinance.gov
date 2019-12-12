/* ==========================================================================
   Settings for webpack JavaScript bundling system.
   ========================================================================== */

const BROWSER_LIST = require( '../config/browser-list-config' );
const envvars = require( '../config/environment' ).envvars;
const webpack = require( 'webpack' );
const TerserPlugin = require( 'terser-webpack-plugin' );

// Constants
const COMMON_BUNDLE_NAME = 'common.js';
const WEBPACK_MODE = 'production';
const IS_MINIMIZED = true;

/* Commmon webpack 'module' option used in each configuration.
   Runs code through Babel and uses global supported browser list. */
const COMMON_MODULE_CONFIG = {
  rules: [ {
    test: /\.js$/,

    /* The `exclude` rule is a double negative.
       It excludes all of `node_modules/` but it then un-excludes modules that
       start with `cf-` and `cfpb-` (CF components and cfpb-chart-builder).
       Regex test: https://regex101.com/r/zizz3V/5 */
    exclude: {
      test: /node_modules/,
      exclude: /node_modules\/(?:cf-.+|cfpb-.+)/
    },
    use: {
      loader: 'babel-loader?cacheDirectory=true',
      options: {
        presets: [ [ '@babel/preset-env', {
          targets: {
            browsers: BROWSER_LIST.LAST_2_IE_11_UP
          },
          debug: false
        } ] ]
      }
    }
  } ]
};

/* Set warnings to true to show linter-style warnings.
   Set mangle to false and beautify to true to debug the output code. */
const COMMON_MINIFICATION_CONFIG = new TerserPlugin( {
  cache: true,
  parallel: true,
  extractComments: false,
  terserOptions: {
    ie8: false,
    ecma: 5,
    warnings: false,
    mangle: true,
    output: {
      comments: false,
      beautify: false
    }
  }
} );

const COMMON_CHUNK_CONFIG = new webpack.optimize.SplitChunksPlugin( {
  name: COMMON_BUNDLE_NAME
} );

const STATS_CONFIG = {
  stats: {
    entrypoints: false
  }
};

const commonConf = {
  cache: true,
  mode: WEBPACK_MODE,
  module: COMMON_MODULE_CONFIG,
  output: {
    filename: '[name]'
  },
  optimization: {
    minimize: IS_MINIMIZED,
    minimizer: [
      COMMON_MINIFICATION_CONFIG
    ]
  },
  resolve: {
    symlinks: false
  },
  stats: STATS_CONFIG.stats
};

const externalConf = {
  cache: true,
  mode: WEBPACK_MODE,
  module: COMMON_MODULE_CONFIG,
  output: {
    filename: 'external-site.js'
  },
  optimization: {
    minimize: IS_MINIMIZED,
    minimizer: [
      COMMON_MINIFICATION_CONFIG
    ]
  },
  resolve: {
    symlinks: false
  },
  stats: STATS_CONFIG.stats
};

const modernConf = {
  cache: true,
  mode: WEBPACK_MODE,
  module: COMMON_MODULE_CONFIG,
  output: {
    filename: '[name]'
  },
  plugins: [
    COMMON_CHUNK_CONFIG
  ],
  optimization: {
    minimize: IS_MINIMIZED,
    minimizer: [
      COMMON_MINIFICATION_CONFIG
    ]
  },
  resolve: {
    symlinks: false
  },
  stats: STATS_CONFIG.stats
};

const onDemandHeaderRawConf = {
  mode: WEBPACK_MODE,
  module: COMMON_MODULE_CONFIG,
  resolve: {
    symlinks: false
  }
};

const appsConf = {
  cache: true,
  mode: WEBPACK_MODE,
  module: COMMON_MODULE_CONFIG,
  output: {
    filename: '[name]',
    jsonpFunction: 'apps'
  },
  plugins: [
    COMMON_CHUNK_CONFIG
  ],
  optimization: {
    minimize: IS_MINIMIZED,
    minimizer: [
      COMMON_MINIFICATION_CONFIG
    ]
  },
  resolve: {
    symlinks: false
  },
  stats: STATS_CONFIG.stats
};

const spanishConf = {
  cache: true,
  mode: WEBPACK_MODE,
  module: COMMON_MODULE_CONFIG,
  output: {
    filename: 'spanish.js'
  },
  optimization: {
    minimize: IS_MINIMIZED,
    minimizer: [
      COMMON_MINIFICATION_CONFIG
    ]
  },
  resolve: {
    symlinks: false
  },
  stats: STATS_CONFIG.stats
};

const devConf = {
  devtool: 'inline-source-map',
  mode: 'development',
  module: COMMON_MODULE_CONFIG,
  plugins: [],
  resolve: {
    symlinks: false
  }
};

const configExports = {
  commonConf,
  devConf,
  externalConf,
  modernConf,
  onDemandHeaderRawConf,
  appsConf,
  spanishConf
};

if ( envvars.NODE_ENV === 'development' ) {
  // eslint-disable-next-line guard-for-in
  let key;
  for ( key in configExports ) {
    if ( {}.hasOwnProperty.call( configExports, key ) ) {
      Object.assign( configExports[key], devConf );
    }
  }
}

module.exports = configExports;
