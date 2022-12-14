import { getNewHash, isOldHash } from './regs3k-utils.js';
import { handleContentClick, handleNavClick } from './analytics.js';
import Expandable from '@cfpb/cfpb-expandables/src/Expandable.js';

const navHeader = document.querySelector('.o-regs3k-navigation_header');
const navItems = document.querySelector('.o-regs3k-sections');
const regContent = document.querySelector('.content_main.regulations3k');

/**
 * toggleSecondaryNav - Show/hide the secondary nav on smaller screens
 */
const toggleSecondaryNav = () => {
  navHeader.classList.toggle('o-expandable_target__collapsed');
  navHeader.classList.toggle('o-expandable_target__expanded');
  navItems.classList.toggle('u-hide-on-stacked');
};

/**
 * bindSecondaryNav - Set up secondary nav toggling.
 */
const bindSecondaryNav = () => {
  navHeader.addEventListener('click', toggleSecondaryNav);
};

/**
 * bindAnalytics - Set up analytics reporting.
 */
const bindAnalytics = () => {
  navItems.addEventListener('click', handleNavClick);
  regContent.addEventListener('click', handleContentClick);
};

/**
 * init - Initialize everything on page load.
 */
const init = () => {
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker
      .register('/regulations3k-service-worker.js')
      .catch((err) => {
        console.error('Error during service worker registration:', err);
      });
  }
  if (navHeader) {
    navHeader.classList.add('o-expandable_target__collapsed');
    navItems.classList.add('u-hide-on-stacked');
    bindSecondaryNav();
    bindAnalytics();
  }
  if (isOldHash(window.location.hash)) {
    window.location.hash = getNewHash(window.location.hash);
  }
};

Expandable.init();

window.addEventListener('load', init);
