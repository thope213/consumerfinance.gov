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
  let h2b = false;
  let h3b = false;

  function checkBold(element) {
    var fontWeight = getComputedStyle( element ).fontWeight;
    if (Number(fontWeight) > 400 || fontWeight === 'bold' || fontWeight === 'bolder') {
      return true;
    }
    return false;
  }

  function toggleBold(tag) {
    document.querySelectorAll(tag)
      .forEach(header => {
        if ( checkBold( header) === false ) {
          header.style.fontWeight = 'bold';
        } else {
          header.style.fontWeight = 'normal';
        }
      })
  }

  document.querySelector('#toggle-h2').addEventListener('click', ele => { toggleBold( 'h2' ) } );
  document.querySelector('#toggle-h2').addEventListener('click', ele => { toggleBold( 'h3' ) } );

}

hTest();
