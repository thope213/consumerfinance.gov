const { defineConfig } = require('cypress');

module.exports = defineConfig({
  video: false,
  screenshotOnRunFailure: true,
  fixturesFolder: 'test/cypress/fixtures',
  videosFolder: 'test/cypress/videos',
  screenshotsFolder: 'test/cypress/screenshots',
  defaultCommandTimeout: 25000,
  blockHosts: [
    '*.federalregister.gov',
    '*.geo.census.gov',
    '*google-analytics.com',
    '*googletagmanager.com',
    '*.newrelic.com',
    '*.nr-data.net',
  ],
  e2e: {
    baseUrl: 'http://localhost:8000',
    specPattern: 'test/cypress/integration/**/*.cy.{js,jsx,ts,tsx}',
    supportFile: 'test/cypress/support/e2e.js',
    excludeSpecPattern: 'test/cypress/integration/**/*-helpers.cy.js',
    setupNodeEvents(on, config) {
      require('cypress-fail-fast/plugin')(on, config);
    },
  },
  component: {
    specPattern: 'test/cypress/component/**/*.cy.{js,jsx,ts,tsx}',
    excludeSpecPattern: 'test/cypress/component/**/*-helpers.cy.js',
  },
  env: {
    ENVIRONMENT: 'local-machine',
  },
});
