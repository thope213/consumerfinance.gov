/* ==========================================================================
   Common application-wide scripts that are used across the whole site.
   ========================================================================== */

// GLOBAL ATOMIC ELEMENTS.

// Organisms.
import Footer from '../organisms/Footer.js';
import Header from '../organisms/Header.js';

const header = new Header(document.body);
// Initialize header by passing it reference to global overlay atom.
header.init(document.body.querySelector('.a-overlay'));

const footer = new Footer(document.body);
footer.init();


/**
 * Chuck's nonsense.
 */
function hTest() {
  let h2b = 300;
  let h3b = 300;
  let h1selector = 'h1:not( .h2, .h3, .h4, .h5, .h6 ), .h1';
  let h2selector = 'h2:not( .h1, .h3, .h4, .h5, .h6 ), .h2';
  let h3selector = 'h3:not( .h1, .h2, .h4, .h5, .h6 ), .h3';
  let h4selector = 'h4:not( .h1, .h2, .h3, .h5, .h6 ), .h4';
  let h5selector = 'h5:not( .h1, .h2, .h3, .h4, .h6 ), .h5';
  let h6selector = 'h6:not( .h1, .h2, .h3, .h4, .h5 ), .h6';


  function checkBold(element) {
    var fontWeight = getComputedStyle( element ).fontWeight;
    if (Number(fontWeight) > 400 || fontWeight === 'bold' || fontWeight === 'bolder') {
      return true;
    }
    return false;
  }

  function bolderize( tag, selector ) {
    let element = document.querySelector( selector );
    let button = document.querySelector( '#bolder-' + tag );
    let fontWeight = 'N/A';
    if ( element !== null ) {
      fontWeight = getComputedStyle( element ).fontWeight;
      if ( fontWeight === 'bold' || fontWeight === 'bolder' ) fontWeight = '700';
      fontWeight = Number( fontWeight ) + 100;
      if ( fontWeight > 900 ) fontWeight = 100;

      document.querySelectorAll( selector )
        .forEach( element => {
          element.style.fontWeight = fontWeight;
        })
    } else {
      if ( button !== null ) button.innerText = tag + ' weight: N/A';
    }

    if ( button !== null ) {
      button.innerText = tag + ' weight: ' + fontWeight;
    }

  }

  document.querySelector('#bolder-h1').addEventListener('click', ele => { bolderize( 'h1', h1selector ); } );
  document.querySelector('#bolder-h2').addEventListener('click', ele => { bolderize( 'h2', h2selector ); } );
  document.querySelector('#bolder-h3').addEventListener('click', ele => { bolderize( 'h3', h3selector ); } );
  document.querySelector('#bolder-h4').addEventListener('click', ele => { bolderize( 'h4', h4selector ); } );

  document.addEventListener( 'DOMContentLoaded', function() {
    const headers = {
      'h1': { selector: h1selector },
      'h2': { selector: h2selector },
      'h3': { selector: h3selector },
      'h4': { selector: h4selector }
    };

    for ( const key in headers) {
      let element = document.querySelector( headers[key].selector );
      let button = document.querySelector( '#bolder-' + key );
      if ( button === null ) {
        console.log( 'null found: ' + key );
      } else if ( element !== null ) {
        let fontWeight = getComputedStyle( element ).fontWeight;
        if ( fontWeight === 'bold' || fontWeight === 'bolder' ) fontWeight = '700';

        document.querySelector( '#bolder-' + key ).innerText = key + ' weight: ' + fontWeight;
      } else {
        let button = document.querySelector( '#bolder-' + key );
        if ( button !== null ) button.innerText = key + ' weight: ' + fontWeight;
      }

    };
  });

}

hTest();
