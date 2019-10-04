document.addEventListener('DOMContentLoaded',function() {
  var languageSelect = document.querySelectorAll(".language-select select");
  languageSelect.forEach(function(select) {
    select.onchange = languageSelectHandler;
  });

  var script = document.createElement('script');
  script.setAttribute('src', '//accounts.adafruit.com/users/locale?callback=setLocale');
  document.body.appendChild(script);
},false);

function languageSelectHandler(event) {
  // find download-details, two levels up from select
  // event may either be an event from selection, or passed from setLocale
  // as a select element.
  if (event.target) {
    var selectedOption = event.target;
    var parentNode = event.target.parentNode.parentNode;
  } else {
    var selectedOption = event.selectedOptions[0];
    var parentNode = event.parentNode.parentNode;
  }

  var files = selectedOption.value.split(',');

  files.forEach(function(file) {
    var extension = file.substr(file.lastIndexOf('.') + 1);
    parentNode.querySelector(".download-button." + extension).href = file;
  });
}

function setLocale(response) {
  var languages = response.languages;
  var languageSelect = document.querySelectorAll(".language-select select");

  languageSelect.forEach(function(select) {
    var options = select.options;

    for (var i = 0; i < options.length; i++) {
      if (languages.includes(options[i].dataset.locale)) {
        options[i].selected = true;
        select.onchange(select);
        break;
      }
    }
  });
}
