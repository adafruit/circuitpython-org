document.addEventListener('DOMContentLoaded',function() {
  var languageSelect = document.querySelectorAll(".language-select select");
  languageSelect.forEach(function(select) {
    select.onchange = languageSelectHandler;
  });

  // get the language from memory
  var storedLanguage = null;
  if (window.localStorage) {
    storedLanguage = localStorage.getItem("language");
    if (storedLanguage != null && storedLanguage != "") {
      language = storedLanguage;
      updateLanguageMenus([language]);
    }
  }
  // or get the language from the browser
  if (storedLanguage == null) {
    var script = document.createElement('script');
    script.setAttribute('src', '//accounts.adafruit.com/users/locale?callback=setLocale');
    document.body.appendChild(script);
  }

  // set the board ID based on query string
  const hereurl = new URL(window.location.href);
  const board_id = hereurl.searchParams.get("unknown_id");
  if(board_id) {
    for(var link of document.querySelectorAll("a")) {
      if(link.href.search("bin/unknown") > 0) {
        link.href = link.href.replace("bin/unknown", `bin/${board_id}`);
      }
    }
    // change the title too
    const title_tag = document.querySelector("#download-page h1");
    var unknown_title = board_id.replaceAll("_"," ");
    unknown_title = unknown_title[0].toUpperCase() + unknown_title.substr(1);
    title_tag.textContent = unknown_title;
    document.title = `${unknown_title} Download`;
  }

},false);

// update the links of the download buttons for the given langage menu item
function updateFileLinks(option, language) {
  var files = option.value.split(',');
  parentNode = option.parentNode.parentNode.parentNode;
  files.forEach(function(file) {
    var extension = file.substr(file.lastIndexOf('.') + 1);
    parentNode.querySelector(".download-button." + extension).href = file;
    if (parentNode.querySelector(".installer-button") !== null){
      parentNode.querySelector(".installer-button").setAttribute(extension + "file", file);
    }
  });
}

// update language menus
function updateLanguageMenus(languages) {
  var languageSelect = document.querySelectorAll(".language-select select");
  languageSelect.forEach(function(select) {
    var options = select.options;
    // find and set one menu with one language
    function findAndSetLocale(language) {
      for (var i = 0; i < options.length; i++) {
        if (language.toLowerCase() == options[i].dataset.locale.toLowerCase()) {
          options[i].selected = true;
          updateFileLinks(options[i],language);
          return true;
        }
      }
      return false;
    }
    // match languages to menu items
    for (var j = 0; j < languages.length; j++) {
    var language = languages[j];
      // test the full language-region string first
      if (findAndSetLocale(language)) return;
      var pos = language.search("-");
      if (pos > 0) {
        // test the language string to catch eg: "fr-FR" as "fr"
        var shortLang = language.substr(0,pos);
        if (findAndSetLocale(shortLang)) return;
      }
    }
  });
}

function languageSelectHandler(event) {
  // set language from selection
  var selectedOption = event.target.selectedOptions[0];
  var selectedLanguage = selectedOption.dataset.locale;
  // save to memory
  if (window.localStorage && event.target) {
    localStorage.setItem("language",selectedLanguage);
  }
  // synchronize all the menus if possible
  updateLanguageMenus([selectedLanguage]);
}

function setLocale(response) {
  var languages = response.languages;
  updateLanguageMenus(languages);
}
