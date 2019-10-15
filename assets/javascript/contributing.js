document.addEventListener('DOMContentLoaded', function() {
  var issueSelect = document.querySelector(".open-issues select");
  issueSelect.onchange = issueSelectHandler;
}, false);

function issueSelectHandler(event) {
  var selectedOption = this.options[this.selectedIndex].value;

  // hide all elements first
  [].forEach.call(document.querySelectorAll('.issues-list li'), function (element) {
    element.style.display = 'none';
    element.parentElement.closest('li').style.display = 'none';
  });

  // show the selected options
  var selectedOption = selectedOption === 'all' ? 'li' : `.${selectedOption}`;
  var items = document.querySelectorAll(`.issues-list ${selectedOption}`);
  items.forEach(function(item) {
    item.style.display = 'block'
    item.parentElement.closest('li').style.display = 'block';
  });
}

