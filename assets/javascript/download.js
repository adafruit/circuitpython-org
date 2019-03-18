var languageSelect;

document.addEventListener('DOMContentLoaded',function() {
  languageSelect = document.querySelectorAll(".language-select select");
  languageSelect.forEach(function(select) {
    select.onchange = languageSelectHandler;
  });

  var script = document.createElement('script');
  script.src = '//accounts.adafruit.com/users/locale?callback=setLocale';
  document.head.appendChild(script);
},false);

function languageSelectHandler(event) {
  // find download-details, two levels up from select
  var parentNode = event.target.parentNode.parentNode;
  var files = event.target.value.split(',');

  files.forEach(function(file) {
    var extension = file.substr(file.lastIndexOf('.') + 1);
    parentNode.querySelector(".download-button." + extension).href = file;
  });
}

function setLocale(response) {
  var languages = response.languages.join(' ')
  var options = languageSelect.options;

  for (var i = 0; i < options.length; i++) {
    if (languages.includes(options[i].dataset.locale)) {
      console.log(options[i].dataset.locale);
      options[i].selected = true;
      languageSelect.onchange();
    }
  }
}
