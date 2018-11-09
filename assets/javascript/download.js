document.addEventListener('DOMContentLoaded',function() {
  var languageSelect = document.querySelector(".language-select select");
  languageSelect.onchange = languageSelectHandler;

  var script = document.createElement('script');
  script.src = '//accounts.adafruit.vm/users/locale?callback=setLocale';
  document.head.appendChild(script);

},false);

function languageSelectHandler(event) {
  var languageSelect = document.querySelector(".language-select select");
  document.querySelector(".download-button").href = languageSelect.value;
}

function setLocale(response) {
  var languages = response.languages.join(' ')
  var languageSelect = document.querySelector(".language-select select");
  var options = languageSelect.options;

  for (var i = 0; i < options.length; i++) {
    if (languages.includes(options[i].dataset.locale)) {
      options[i].selected = true;
      languageSelect.onchange();
    }
  }
}
