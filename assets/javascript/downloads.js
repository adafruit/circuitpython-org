var downloadsSearch = {
  initFilter: false,
  featuresChecked: false,
  searchTerm: null,
  urlTimeout: null,
  manufacturers: {},
  features: {},
  selected: {
    manufacturers: [],
    features: []
  }
};

document.addEventListener('DOMContentLoaded', function() {
  document.getElementById("search").addEventListener('keyup', handleSearch);
  document.querySelector(".downloads-filter .filter").addEventListener('click', handleFilter);
  document.querySelector(".filter-buttons .save-changes").addEventListener('click', handleSaveChanges);

  document.addEventListener('click', handleRemoveTag);

  var sortRadios = document.querySelectorAll(".downloads-filter-content .sort-by input");
  for(var i = 0; i < sortRadios.length; i++) {
    sortRadios[i].addEventListener('click', handleSortResults);
  }

  handlePageLoad();
});

function setURL(query, value) {
  clearTimeout(downloadsSearch.urlTimeout);

  downloadsSearch.urlTimeout = setTimeout(function() {
    var url = new URL(window.location.href);
    if (!value.length) {
      url.searchParams.delete(query);
    } else if (Array.isArray(value)) {
      url.searchParams.delete(query);
      value.forEach(function(v) {
        url.searchParams.append(query, v);
      })
    } else {
      url.searchParams.set(query, value);
    }

    window.history.pushState(null, document.title, url.href);
  }, 1000);
}

function handlePageLoad() {
  initFilter();

  var url = new URL(window.location.href);
  //get values from URL
  var manufacturers = url.searchParams.getAll('manufacturers');
  var features = url.searchParams.getAll('features');
  var sort_by = url.searchParams.get('sort-by');
  downloadsSearch.searchTerm = url.searchParams.get('q');

  if (downloadsSearch.searchTerm) {
    document.getElementById("search").value = downloadsSearch.searchTerm;
    filterResults();
  }

  if (manufacturers.length) {
    manufacturers.forEach(function(selected) {
      document.querySelector("input[name='manufacturer'][value='" + selected + "']").click();
    });
  }

  if (features.length) {
    features.forEach(function(selected) {
      document.querySelector("input[name='feature'][value='" + selected + "']").click();
    });
  }

  if (sort_by.length) {
    document.querySelector("input[name='sort-by'][value='" + sort_by + "']").click();
  }
}

function handleSearch(event) {
  downloadsSearch.searchTerm = event.target.value;
  setURL('q', downloadsSearch.searchTerm);

  filterResults();
}

function handleFilter(event) {
  initFilter();
  toggleFilterContainer();
}

function initFilter() {
  if (downloadsSearch.initFilter) {
    return;
  }

  var downloads = document.querySelectorAll('.download');

  setupManufacturers(downloads);
  setupFeatures(downloads);
  setupFilterListeners();

  downloadsSearch.initFilter = true;
}

function handleSaveChanges() {
  toggleFilterContainer();
}

function handleRemoveTag(event) {
  if (event.target && /tag-remove/gi.test(event.target.className)) {
    var tag = event.target;
    var name = tag.dataset.name;
    var type = tag.dataset.type;
    var selector = "input[name='" + type + "'][value='" + name + "']";

    document.querySelector(selector).click();
  }
}

function toggleFilterContainer() {
  var filterContainer = document.querySelector('.downloads-filter-content');

  if (filterContainer.style.display == 'grid') {
    filterContainer.style.display = 'none';
  } else {
    filterContainer.style.display = 'grid';
  }
}

function setupManufacturers(downloads) {
  downloads.forEach(function(download) {
    var manufacturer = download.dataset.manufacturer;
    if (manufacturer in downloadsSearch.manufacturers) {
      downloadsSearch.manufacturers[manufacturer].push(download.dataset.id);
    } else {
      downloadsSearch.manufacturers[manufacturer] = [download.dataset.id];
    }
  });

  var manufacturerList = document.querySelector('.manufacturers .content');

  for (manufacturer in downloadsSearch.manufacturers) {
    var li = document.createElement("li");
    var checkbox = document.createElement('input');
    checkbox.type = "checkbox";
    checkbox.name = "manufacturer";
    checkbox.className = 'filter-checkbox';
    checkbox.value = manufacturer;

    li.appendChild(checkbox);
    li.appendChild(document.createTextNode(manufacturer));

    manufacturerList.appendChild(li);
  }
}

function setupFeatures(downloads) {
  downloads.forEach(function(download) {
    var features = download.dataset.features.split(',');
    features.forEach(function(feature) {
      if (!feature.length) {
        return;
      }

      if (feature in downloadsSearch.features) {
        downloadsSearch.features[feature].push(download.dataset.id);
      } else {
        downloadsSearch.features[feature] = [download.dataset.id];
      }
    });
  });

  var featureList = document.querySelector('.features .content');

  for (feature in downloadsSearch.features) {
    var li = document.createElement("li");
    var checkbox = document.createElement('input');
    checkbox.type = "checkbox";
    checkbox.name = "feature";
    checkbox.className = 'filter-checkbox';
    checkbox.value = feature;

    li.appendChild(checkbox);
    li.appendChild(document.createTextNode(feature));

    featureList.appendChild(li);
  }
}

function setupFilterListeners() {
  document.body.addEventListener('change', function (event) {
    var checkbox = event.target;
    var index = downloadsSearch.selected.manufacturers.indexOf(checkbox.value);
    if (checkbox.name === 'manufacturer') {
      if (checkbox.checked) {
        if (index == -1) {
          downloadsSearch.selected.manufacturers.push(checkbox.value);
          appendFilterTag('manufacturer', checkbox.value);
        }
      } else {
        if (index > -1) {
          downloadsSearch.selected.manufacturers.splice(index, 1);
          removeFilterTag('manufacturer', checkbox.value);
        }
      }
      setURL('manufacturers', downloadsSearch.selected.manufacturers);
      filterResults();
    }

    if (checkbox.name === 'feature') {
      if (checkbox.checked) {
        downloadsSearch.selected.features.push(checkbox.value);
        appendFilterTag('feature', checkbox.value);
      } else {
        var index = downloadsSearch.selected.features.indexOf(checkbox.value);
        if (index > -1) {
          downloadsSearch.selected.features.splice(index, 1);
          removeFilterTag('feature', checkbox.value);
        }
      }
      setURL('features', downloadsSearch.selected.manufacturers);
      filterResults();
    }
  });
}

function filterResults() {
  var displayedManufacturers = [], displayedFeatures = [];

  var selectedManufacturers = downloadsSearch.selected.manufacturers;
  var selectedFeatures = downloadsSearch.selected.features;

  selectedManufacturers.forEach(function(manufacturer) {
    Array.prototype.push.apply(displayedManufacturers, downloadsSearch.manufacturers[manufacturer]);
  });

  selectedFeatures.forEach(function(feature, index) {
    // if multiple features are selected, only add the id if it is included
    // in all feature types
    if (selectedFeatures.length > 1 && index > 0) {
      displayedFeatures = displayedFeatures.filter(function(displayed) {
        return downloadsSearch.features[feature].indexOf(displayed) !== -1;
      });
    } else {
      Array.prototype.push.apply(displayedFeatures, downloadsSearch.features[feature]);
    }

  });


  // we need to ensure that we check if features are checked, if you check
  // too many features, there is a good chance no boards will be visible.
  setFeaturesChecked();

  var downloads = document.querySelectorAll('.download');
  var board_count = 0
  downloads.forEach(function(download) {
    if (!shouldDisplayDownload(download, displayedManufacturers, displayedFeatures)) {
      download.style.display = 'none';
    } else {
      download.style.display = 'block';
      board_count++;
    }
  });
  document.getElementById("board_count").innerHTML = board_count;
}

function handleSortResults(event) {
  var sortType = event.target.value;
  setURL('sort-by', sortType);
  var downloads = document.querySelector('.downloads-section');

  Array.prototype.slice.call(downloads.children)
    .map(function (download) { return downloads.removeChild(download); })
    .sort(function (a, b) {
      switch(sortType) {
        case 'alpha-asc':
          return a.dataset.name.localeCompare(b.dataset.name);
        case 'alpha-desc':
          return b.dataset.name.localeCompare(a.dataset.name);
        default:
          // sort by download count is the deafult
          return parseInt(a.dataset.downloads, 10) < parseInt(b.dataset.downloads, 10);
      }
    })
    .forEach(function (download) { downloads.appendChild(download); });
}

function setFeaturesChecked() {
  downloadsSearch.featuresChecked = document.querySelectorAll('input[name="feature"]:checked').length > 0;
}

function shouldDisplayDownload(download, displayedManufacturers, displayedFeatures) {
  var shouldFilterFeatures = downloadsSearch.featuresChecked;
  var shouldFilterManufacturers = displayedManufacturers.length > 0;
  var shouldDisplay = false;

  var id = download.dataset.id;

  if (!shouldFilterFeatures && !shouldFilterManufacturers) {
    shouldDisplay = true;
  }

  if (shouldFilterManufacturers) {
    if (displayedManufacturers.includes(id)) {
      if (shouldFilterFeatures) {
        if (displayedFeatures.includes(id)) {
          shouldDisplay = true;
        }
      } else {
        shouldDisplay = true;
      }
    }
  } else if (shouldFilterFeatures && displayedFeatures.includes(id)) {
    shouldDisplay = true;
  }

  if (downloadsSearch.searchTerm && downloadsSearch.searchTerm.length > 0 && shouldDisplay) {
    var regex = new RegExp(downloadsSearch.searchTerm, "gi");
    var name = download.dataset.name;

    shouldDisplay = name.match(regex);
  }

  return shouldDisplay;
}

function appendFilterTag(type, name) {
  var tagHtml = "<span class='tag'><i class='fas fa-times tag-remove' title='Remove Filtered Option'";
  tagHtml += "data-type='" + type + "' ";
  tagHtml += "data-name='" + name + "'></i>";
  tagHtml += name + "</span>";

  document.querySelector('.downloads-filter-tags').insertAdjacentHTML('beforeend', tagHtml);
}

function removeFilterTag(type, name) {
  document.querySelector("[data-type='" + type + "'][data-name='" + name + "']").parentNode.remove();
}
