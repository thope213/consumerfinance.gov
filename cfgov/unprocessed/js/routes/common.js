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

 const h1selector = 'h1:not( .h2, .h3, .h4, .h5, .h6 ), .h1';
 const h2selector = 'h2:not( .h1, .h3, .h4, .h5, .h6 ), .h2';
 const h3selector = 'h3:not( .h1, .h2, .h4, .h5, .h6 ), .h3';
 const h4selector = 'h4:not( .h1, .h2, .h3, .h5, .h6 ), .h4';
 const h5selector = 'h5:not( .h1, .h2, .h3, .h4, .h6 ), .h5';
 const h6selector = 'h6:not( .h1, .h2, .h3, .h4, .h5 ), .h6';

 const headers = {
   'h1': { selector: h1selector },
   'h2': { selector: h2selector },
   'h3': { selector: h3selector },
   'h4': { selector: h4selector }
 };



function hTest() {
  let h2b = 300;
  let h3b = 300;

  function checkBold(element) {
    let fontWeight = getComputedStyle( element ).fontWeight;
    if (Number(fontWeight) > 400 || fontWeight === 'bold' || fontWeight === 'bolder') {
      return true;
    }
    return false;
  }

  function AJizer( version ) {


    document.querySelectorAll( h1selector ).forEach( element => {
      if ( version === 'v1' ) {
        element.style.fontSize = '40px';
        element.style.fontWeight = '700';       
      } else {
        element.style.fontSize = null;
        element.style.fontWeight = '600';
      }

    } );
    document.querySelectorAll( h2selector ).forEach( element => {
      if ( version === 'v1' ) {
        element.style.fontSize = '32px';
        element.style.fontWeight = '700';
      } else {
        element.style.fontSize = null;
        element.style.fontWeight = '600';
      }
    } );
    document.querySelectorAll( h3selector ).forEach( element => {
      if ( version === 'v1' ) {
        element.style.fontSize = '26px';
        element.style.fontWeight = '500';
      } else {
        element.style.fontSize = null;
        element.style.fontWeight = null;
      }
    } );
    document.querySelectorAll( h4selector ).forEach( element => {
      if ( version === 'v1' ) {
        element.style.fontSize = '20px';
        element.style.fontWeight = '500';
      } else {
        element.style.fontSize = null;
        element.style.fontWeight = null;
      }
    } );
  }

  function cleanse() {
    for ( let key in headers ) {
      document.querySelectorAll( headers[key]['selector'] ).forEach( elem => {
        elem.style.fontWeight = null;
        elem.style.fontSize = null;
      } );
    }
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

  function resizer( target ) {
    const elem = target.closest( 'button.h-resizer' );

    const header = elem.dataset.header_name;
    const resize = elem.dataset.header_resize;
    const sizeElem = document.querySelector( '[data-h_size="' + header + '"]' );
    const size = Number( sizeElem.innerText.replace(/\D/g,'') );
    let newSize = size;
    if ( resize === "bigger" ) {
      newSize += 2;
    } else if ( resize === "smaller" ) {
      newSize -= 2;
    }

    if ( typeof header !== 'undefined' && typeof resize !== 'undefined' ) {
        document.querySelectorAll( headers[header].selector )
          .forEach( element => {
            element.style.fontSize = newSize + 'px';
          });
        document.querySelector( '[data-h_size="' + header + '"]').innerText = newSize + 'px';
    }
  }

  for ( const key in headers) {
    let element = document.querySelector( headers[key].selector );
    let button = document.querySelector( '#bolder-' + key );
    if ( button === null ) {
      console.log( 'null found: ' + key );
    } else if ( element !== null ) {
      let fontWeight = getComputedStyle( element ).fontWeight;
      let fontSize = getComputedStyle( element ).fontSize;
      if ( fontWeight === 'bold' || fontWeight === 'bolder' ) fontWeight = '700';

      document.querySelector( '#bolder-' + key ).innerText = key + ' weight: ' + fontWeight;
      document.querySelector( '[data-h_size="' + key + '"]' ).innerText = fontSize;
    } else {
      let button = document.querySelector( '#bolder-' + key );
      if ( button !== null ) button.innerText = key + ' weight: ???';
    }
  };

  document.querySelector('#bolder-h1').addEventListener('click', event => { bolderize( 'h1', h1selector ); } );
  document.querySelector('#bolder-h2').addEventListener('click', event => { bolderize( 'h2', h2selector ); } );
  document.querySelector('#bolder-h3').addEventListener('click', event => { bolderize( 'h3', h3selector ); } );
  document.querySelector('#bolder-h4').addEventListener('click', event => { bolderize( 'h4', h4selector ); } );

  document.querySelector('#v1').addEventListener('click', event => { AJizer( 'v1' ); } );
  document.querySelector('#v2').addEventListener('click', event => { AJizer( 'v2' ); } );
  document.querySelector('#cleanse').addEventListener('click', event => { cleanse(); } );

  document.querySelectorAll( '.h-resizer')
  .forEach( ele => {
      ele.addEventListener( 'click', event => { resizer( event.target ) } );
    });

}


window.addEventListener( 'load', function() {
  hTest();
} );
