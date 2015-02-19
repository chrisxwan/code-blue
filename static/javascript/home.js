(function (document) {
  'use strict';

  document.addEventListener('polymer-ready', function () {
    // Perform some behaviour
    console.log('Polymer is ready to rock!');
  });

// wrap document so it plays nice with other libraries
// http://www.polymer-project.org/platform/shadow-dom.html#wrappers
})(wrap(document));

$('.waves').stellar({
	horizontalScrolling: true,
	verticalScrolling: false,
	responsive: true,
	scrollProperty: 'scroll',
	positionProperty: 'position',
	parallaxBackgrounds: true,
  	parallaxElements: true,
});