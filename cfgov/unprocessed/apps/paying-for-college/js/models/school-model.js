// This model contains school information
import { setUrlQueryString } from '../util/url-parameter-utils.js';

const schoolModel = {
  values: {},

  setValue: function( name, value ) {
    schoolModel.values[name] = value;
    setUrlQueryString();
  }

};

export {
  schoolModel
};
