document.addEventListener('DOMContentLoaded', function() {
  // only load on open issues page for now
  var issueSelect = document.querySelector(".open-issues #label-filter");
  if (!issueSelect) {
    return;
  }

  issueSelect.onchange = function(event) {
    issueSelectHandler(event);
    applySorting();
  };

  var sortSelect = document.querySelector(".open-issues #sort-order");
  if (sortSelect) {
    sortSelect.onchange = function() {
      applySorting();
    };
  }

  // load issues label when using back button
  window.addEventListener('popstate', loadIssues.bind(null, true));

  // load issues label on page load
  loadIssues();
}, false);

function loadIssues(isPopState) {
  var params = new URLSearchParams(window.location.search);
  var label = params.get('label');
  var sort = params.get('sort');

  if (sort) {
    var sortSelect = document.querySelector('.open-issues #sort-order');
    if (sortSelect) {
      sortSelect.value = sort;
    }
  }

  if (label) {
    issueSelectHandler(label, isPopState);
    var issuesList = document.querySelector('.open-issues #label-filter');
    issuesList.value = label;
  }

  applySorting();
}

function issueSelectHandler(event, isPopState) {
  if (event.target) {
    var selectedOption = event.target.options[event.target.selectedIndex].value;
  } else {
    // page loads will set the event as just the selected label from params
    var selectedOption = event;
  }

  // don't set params on the back button
  if (!isPopState) {
    setParams();
  }

  // hide all elements first
  [].forEach.call(document.querySelectorAll('.issues-list li'), function (element) {
    element.style.display = 'none';
    element.parentElement.closest('li').style.display = 'none';
  });

  // show the selected options
  var selector = selectedOption === 'all' ? 'li' : '.' + selectedOption;
  var items = document.querySelectorAll('.issues-list ' + selector);
  items.forEach(function(item) {
    item.style.display = 'block';
    item.parentElement.closest('li').style.display = 'block';
  });
}

function getIssueDays(element) {
  // Parse "(Open X days)" from the issue title text
  var text = element.textContent || '';
  var match = text.match(/\(Open\s+(\d+)\s+days?\)/i);
  if (match) {
    return parseInt(match[1], 10);
  }
  return 0;
}

function applySorting() {
  var sortSelect = document.querySelector('.open-issues #sort-order');
  if (!sortSelect) return;

  var sortOrder = sortSelect.value;
  if (sortOrder === 'default') {
    // Restore original order by reloading — but simpler to just not sort
    // We store original order on first run
    restoreOriginalOrder();
    setParams();
    return;
  }

  // Sort issues within each library's issues-list
  var issuesLists = document.querySelectorAll('.issues-list');
  issuesLists.forEach(function(list) {
    var items = Array.from(list.querySelectorAll(':scope > li'));

    // Store original order if not already stored
    if (!list.dataset.originalOrder) {
      list.dataset.originalOrder = 'stored';
      items.forEach(function(item, index) {
        item.dataset.originalIndex = index;
      });
    }

    items.sort(function(a, b) {
      var daysA = getIssueDays(a);
      var daysB = getIssueDays(b);
      if (sortOrder === 'newest') {
        return daysA - daysB; // fewer days = newer = first
      } else {
        return daysB - daysA; // more days = older = first
      }
    });

    // Re-append in sorted order
    items.forEach(function(item) {
      list.appendChild(item);
    });
  });

  // Also sort the library-level list items by their oldest/newest issue
  var topList = document.querySelector('.open-issues > ul');
  if (topList) {
    var libraryItems = Array.from(topList.querySelectorAll(':scope > li'));

    if (!topList.dataset.originalOrder) {
      topList.dataset.originalOrder = 'stored';
      libraryItems.forEach(function(item, index) {
        item.dataset.originalIndex = index;
      });
    }

    libraryItems.sort(function(a, b) {
      var issuesA = a.querySelectorAll('.issues-list > li');
      var issuesB = b.querySelectorAll('.issues-list > li');
      var maxA = getMaxDays(issuesA, sortOrder);
      var maxB = getMaxDays(issuesB, sortOrder);
      if (sortOrder === 'newest') {
        return maxA - maxB;
      } else {
        return maxB - maxA;
      }
    });

    libraryItems.forEach(function(item) {
      topList.appendChild(item);
    });
  }

  setParams();
}

function getMaxDays(issues, sortOrder) {
  var result = sortOrder === 'newest' ? Infinity : 0;
  issues.forEach(function(issue) {
    var days = getIssueDays(issue);
    if (sortOrder === 'newest') {
      result = Math.min(result, days);
    } else {
      result = Math.max(result, days);
    }
  });
  return result === Infinity ? 0 : result;
}

function restoreOriginalOrder() {
  // Restore library-level order
  var topList = document.querySelector('.open-issues > ul');
  if (topList && topList.dataset.originalOrder) {
    var libraryItems = Array.from(topList.querySelectorAll(':scope > li'));
    libraryItems.sort(function(a, b) {
      return (parseInt(a.dataset.originalIndex) || 0) - (parseInt(b.dataset.originalIndex) || 0);
    });
    libraryItems.forEach(function(item) {
      topList.appendChild(item);
    });
  }

  // Restore issue-level order within each list
  var issuesLists = document.querySelectorAll('.issues-list');
  issuesLists.forEach(function(list) {
    var items = Array.from(list.querySelectorAll(':scope > li'));
    items.sort(function(a, b) {
      return (parseInt(a.dataset.originalIndex) || 0) - (parseInt(b.dataset.originalIndex) || 0);
    });
    items.forEach(function(item) {
      list.appendChild(item);
    });
  });
}

function setParams() {
  var params = new URLSearchParams(window.location.search);

  var labelSelect = document.querySelector('.open-issues #label-filter');
  if (labelSelect && labelSelect.value && labelSelect.value !== 'all') {
    params.set("label", labelSelect.value);
  } else {
    params.delete("label");
  }

  var sortSelect = document.querySelector('.open-issues #sort-order');
  if (sortSelect && sortSelect.value && sortSelect.value !== 'default') {
    params.set("sort", sortSelect.value);
  } else {
    params.delete("sort");
  }

  var query = params.toString();
  var newUrl = window.location.protocol + '//' + window.location.host + window.location.pathname;
  if (query) {
    newUrl += '?' + query;
  }
  window.history.pushState({path: newUrl}, '', newUrl);
}
