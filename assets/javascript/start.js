document.addEventListener('DOMContentLoaded',function() {
  document.querySelectorAll(".tab-links a").forEach(link => {
    link.addEventListener('click', showContent);
  });
});

function showContent(event) {
  event.preventDefault();
  var tabId = event.target.getAttribute('href').substring(1);
  var startSection = event.target.closest('.start-section');
  // toggle active class for links
  startSection.querySelector(".tab-links a.active").classList.remove('active');
  event.target.classList.add('active');
  // toggle active class for content
  startSection.querySelector(".tab-content.active").classList.remove('active');
  document.getElementById(tabId).classList.add('active');
}
