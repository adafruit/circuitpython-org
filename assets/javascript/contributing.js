document.addEventListener('DOMContentLoaded', function() {
  // only load on open issues page for now
  var issueSelect = document.querySelector(".open-issues select");
  if (!issueSelect) {
    return;
  }

  issueSelect.onchange = issueSelectHandler;

  // load issues label when using back button
  window.addEventListener('popstate', loadIssues.bind(null, true));

  // load issues label on page load
  loadIssues();
}, false);

function loadIssues(isPopState) {
  var params = new URLSearchParams(window.location.search);
  var label = params.get('label');

  if (!label) {
    return;
  }

  issueSelectHandler(label, isPopState);
  var issuesList = document.querySelector('.open-issues select');
  issuesList.value = label;
}

function issueSelectHandler(event, isPopState) {
  if (event.target) {
    var selectedOption = this.options[this.selectedIndex].value;
  } else {
    // page loads will set the event as just the selected label from params
    var selectedOption = event;
  }

  // don't set params on the back button
  if (!isPopState) {
    setIssueParams(selectedOption);
  }

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

function setIssueParams(label) {
  var params = new URLSearchParams(window.location.search);
  params.set("label", label);
  var newUrl = `${window.location.protocol}//${window.location.host}${window.location.pathname}?${params.toString()}`;
  window.history.pushState({path:newUrl}, '', newUrl);
}
