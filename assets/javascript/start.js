document.addEventListener('DOMContentLoaded',function() {
  document.querySelectorAll(".tab-links a").forEach(link => {
    link.addEventListener('click', showContent);
  });
});

function showContent(event) {
  event.preventDefault();
  var tab = event.target.getAttribute('href');
  // toggle active class for links
  document.querySelector(".tab-links a.active").classList.remove('active');
  event.target.classList.add('active');
  // toggle active class for content
  document.querySelector(".tab-content.active").classList.remove('active');
  document.getElementById(tab.substring(1)).classList.add('active');
}
