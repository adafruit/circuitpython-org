document.addEventListener('DOMContentLoaded', function() {
  document.getElementById("mobile-menu-button").addEventListener('click', handleMobileToggle);
});

function handleMobileToggle(event) {
  event.preventDefault();

  var menuContainer = document.getElementById('mobile-menu-contents');

  menuContainer.classList.toggle('hidden');
}
