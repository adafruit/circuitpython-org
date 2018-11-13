var languageSelect;

document.addEventListener('DOMContentLoaded',function() {
  languageSelect = document.querySelector(".language-select select");
  languageSelect.onchange = languageSelectHandler;

  var script = document.createElement('script');
  script.src = '//accounts.adafruit.com/users/locale?callback=setLocale';
  document.head.appendChild(script);

},false);

function languageSelectHandler(event) {
  document.querySelector(".download-button").href = languageSelect.value;
}

function setLocale(response) {
  var languages = response.languages.join(' ')
  var options = languageSelect.options;

  for (var i = 0; i < options.length; i++) {
    if (languages.includes(options[i].dataset.locale)) {
      options[i].selected = true;
      languageSelect.onchange();
    }
  }
}
