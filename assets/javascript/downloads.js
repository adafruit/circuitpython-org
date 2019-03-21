var downloadsSearch = {
  initFilter: false,
  featuresChecked: false,
  manufacturers: {},
  features: {},
  selected: {
    manufacturers: [],
    features: []
  }
};

document.addEventListener('DOMContentLoaded', function() {
  var searchElement = document.getElementById("search");
  searchElement.addEventListener('keyup', handleSearch);

  var filterElement = document.querySelector(".downloads-filter .filter");
  filterElement.addEventListener('click', handleFilter);
});

function handleSearch(event) {
  filterResults(event.target.value);
}

function handleFilter(event) {
  if (!downloadsSearch.initFilter) {
    initFilter();
  }

  toggleFilterContainer();
}

function initFilter() {
  var downloads = document.querySelectorAll('.download');

  setupManufacturers(downloads);
  setupFeatures(downloads);
  setupFilterListeners();

  downloadsSearch.initFilter = true;
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
    if (checkbox.name === 'manufacturer') {
      if (checkbox.checked) {
        downloadsSearch.selected.manufacturers.push(checkbox.value);
      } else {
        var index = downloadsSearch.selected.manufacturers.indexOf(checkbox.value);
        if (index > -1) {
          downloadsSearch.selected.manufacturers.splice(index, 1);
        }
      }
      filterResults();
    }

    if (checkbox.name === 'feature') {
      if (checkbox.checked) {
        downloadsSearch.selected.features.push(checkbox.value);
      } else {
        var index = downloadsSearch.selected.features.indexOf(checkbox.value);
        if (index > -1) {
          downloadsSearch.selected.features.splice(index, 1);
        }
      }
      filterResults();
    }
  });
}

function filterResults(searchTerm) {
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

  downloads.forEach(function(download) {
    if (!shouldDisplayDownload(download, searchTerm, displayedManufacturers, displayedFeatures)) {
      download.style.display = 'none';
    } else {
      download.style.display = 'block';
    }
  });
}

function setFeaturesChecked() {
  downloadsSearch.featuresChecked = document.querySelectorAll('input[name="feature"]:checked').length > 0;
}

function shouldDisplayDownload(download, searchTerm, displayedManufacturers, displayedFeatures) {
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

  if (searchTerm && searchTerm.length > 0 && shouldDisplay) {
    var regex = new RegExp(searchTerm, "gi");
    var name = download.dataset.name;

    shouldDisplay = name.match(regex);
  }

  return shouldDisplay;
}
