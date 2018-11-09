document.addEventListener('DOMContentLoaded',function() {
  var languageSelect = document.querySelector(".language-select select");
  languageSelect.onchange=languageSelectHandler;
},false);

function languageSelectHandler(event) {
    document.querySelector(".download-button").href = event.target.value;
}
