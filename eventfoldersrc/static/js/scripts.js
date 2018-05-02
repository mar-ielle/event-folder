
var panel = document.getElementById("panel");

function checkPanelOffset() {
  return panel.offsetTop <= window.scrollY;
}

var panelStickyness = function() {
  panel.classList.toggle('sticky', checkPanelOffset());
}

function tryCheck() {
 requestAnimationFrame(panelStickyness)
}

window.addEventListener('scroll', tryCheck, false);
window.addEventListener('resize', tryCheck, false);