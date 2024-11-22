var downloadsSearch = {
  initFilter: false,
  featuresChecked: false,
  searchTerm: null,
  urlTimeout: null,
  manufacturers: {},
  mcufamilies: {},
  features: {},
  selected: {
    manufacturers: [],
    mcufamilies: [],
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
  var mcufamilies = url.searchParams.getAll('mcufamilies');
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

  if (mcufamilies.length) {
    mcufamilies.forEach(function(selected) {
      document.querySelector("input[name='mcufamily'][value='" + selected + "']").click();
    });
  }

  if (features.length) {
    features.forEach(function(selected) {
      document.querySelector("input[name='feature'][value='" + selected + "']").click();
    });
  }

  if (sort_by != null && sort_by.length) {
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
  setupMcufamilies(downloads);
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

  // build an alpha sorted array of manufacturer names
  var manufacturers = Object.keys(downloadsSearch.manufacturers).sort(function(a, b) {
    return a.localeCompare(b, 'en', {'sensitivity': 'base'});
  });

  manufacturers.forEach(function(manufacturer) {
    var li = document.createElement("li");
    var checkbox = document.createElement('input');
    checkbox.type = "checkbox";
    checkbox.name = "manufacturer";
    checkbox.className = 'filter-checkbox';
    checkbox.value = manufacturer;
    checkbox.id = 'manufacturer-' + manufacturer;

    li.appendChild(checkbox);
    var label = document.createElement('label');
    label.htmlFor = checkbox.id;
    label.innerText = manufacturer;
    li.appendChild(label);

    manufacturerList.appendChild(li);
  });
}

function setupMcufamilies(downloads) {
  downloads.forEach(function(download) {
    var mcufamily = download.dataset.mcufamily;
    if (mcufamily in downloadsSearch.mcufamilies) {
      downloadsSearch.mcufamilies[mcufamily].push(download.dataset.id);
    } else {
      downloadsSearch.mcufamilies[mcufamily] = [download.dataset.id];
    }
  });

  var mcufamilyList = document.querySelector('.mcufamilies .content');

  // build an alpha sorted array of mcufamily names
  var mcufamilies = Object.keys(downloadsSearch.mcufamilies).sort(function(a, b) {
    return a.localeCompare(b, 'en', {'sensitivity': 'base'});
  });

  mcufamilies.forEach(function(mcufamily) {
    if (mcufamily.length) {
      var li = document.createElement("li");
      var checkbox = document.createElement('input');
      checkbox.type = "checkbox";
      checkbox.name = "mcufamily";
      checkbox.className = 'filter-checkbox';
      checkbox.value = mcufamily;
      checkbox.id = 'mcufamily-' + mcufamily;

      li.appendChild(checkbox);

      var label = document.createElement('label');
      label.htmlFor = checkbox.id;
      label.innerText = mcufamily;
      li.appendChild(label);

      mcufamilyList.appendChild(li);
    }
  });
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

  var features = Object.keys(downloadsSearch.features).sort(function(a, b) {
    return a.localeCompare(b, 'en', {'sensitivity': 'base'});
  });

  features.forEach(function(feature) {
    var li = document.createElement("li");
    var checkbox = document.createElement('input');
    checkbox.type = "checkbox";
    checkbox.name = "feature";
    checkbox.className = 'filter-checkbox';
    checkbox.value = feature;
    checkbox.id = 'feature-' + feature;

    li.appendChild(checkbox);

    var label = document.createElement('label');
    label.htmlFor = checkbox.id;
    label.innerText = feature;
    li.appendChild(label);

    featureList.appendChild(li);
  });
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

    if (checkbox.name === 'mcufamily') {
      if (checkbox.checked) {
        downloadsSearch.selected.mcufamilies.push(checkbox.value);
        appendFilterTag('mcufamily', checkbox.value);
      } else {
        var index = downloadsSearch.selected.mcufamilies.indexOf(checkbox.value);
        if (index > -1) {
          downloadsSearch.selected.mcufamilies.splice(index, 1);
          removeFilterTag('mcufamily', checkbox.value);
        }
      }
      setURL('mcufamilies', downloadsSearch.selected.mcufamilies);
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
      setURL('features', downloadsSearch.selected.features);
      filterResults();
    }
  });
}

function filterResults() {
  var displayedManufacturers = [], displayedMcufamilies = [], displayedFeatures = [];

  var selectedManufacturers = downloadsSearch.selected.manufacturers;
  var selectedMcufamilies = downloadsSearch.selected.mcufamilies;
  var selectedFeatures = downloadsSearch.selected.features;

  selectedManufacturers.forEach(function(manufacturer) {
    Array.prototype.push.apply(displayedManufacturers, downloadsSearch.manufacturers[manufacturer]);
  });

  selectedMcufamilies.forEach(function(mcufamily) {
    Array.prototype.push.apply(displayedMcufamilies, downloadsSearch.mcufamilies[mcufamily]);
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
    if (!shouldDisplayDownload(download, displayedManufacturers, displayedMcufamilies, displayedFeatures)) {
      download.style.display = 'none';
    } else {
      download.style.display = 'block';
      board_count++;
      // exact tag match re-order
      if (downloadsSearch.searchTerm !== null && downloadsSearch.searchTerm !== undefined) {
        let searched = downloadsSearch.searchTerm.toLowerCase();
        let tags = download.getAttribute("data-tags").split(",");
        if (searched !== "" && tags.indexOf(searched) >= 0) {
          let parent = download.parentElement;
          parent.removeChild(download);
          parent.prepend(download);
        }
      }
    }
  });
  document.getElementById("board_count").innerHTML = board_count;
}

function handleSortResults(event) {
  let searched;
  if (downloadsSearch.searchTerm !== null && downloadsSearch.searchTerm !== undefined) {
    searched = downloadsSearch.searchTerm.toLowerCase();
  }
  var sortType = event.target.value;
  setURL('sort-by', sortType);
  var downloads = document.querySelector('.downloads-section');
  Array.prototype.slice.call(downloads.children)
    .map(function (download) { return downloads.removeChild(download); })
    .sort(function (a, b) {
      // exact tag match re-order
      if (searched !== undefined && searched !== "" &&
          a.dataset.tags.split(",").indexOf(searched) >= 0){

        return -2;
      }
      switch(sortType) {
        case 'alpha-asc':
          return a.dataset.name.localeCompare(b.dataset.name);
        case 'alpha-desc':
          return b.dataset.name.localeCompare(a.dataset.name);
        case 'date-asc':
          dateA = new Date(a.dataset.date)
          dateB = new Date(b.dataset.date)
          return dateA.getTime() < dateB.getTime() ? -1 : 1;
        case 'date-desc':
          dateA = new Date(a.dataset.date)
          dateB = new Date(b.dataset.date)
          return dateA.getTime() < dateB.getTime() ? 1 : -1;
        default:
          // sort by download count is the default
          return parseInt(a.dataset.downloads, 10) < parseInt(b.dataset.downloads, 10) ? 1 : -1;
      }
    })
    .forEach(function (download) { downloads.appendChild(download); });
}

function setFeaturesChecked() {
  downloadsSearch.featuresChecked = document.querySelectorAll('input[name="feature"]:checked').length > 0;
}

function shouldDisplayDownload(download, displayedManufacturers, displayedMcufamilies, displayedFeatures) {
  const shouldFilterFeatures = downloadsSearch.featuresChecked;
  const shouldFilterManufacturers = displayedManufacturers.length > 0;
  const shouldFilterMcufamilies = displayedMcufamilies.length > 0;

  const boardId = download.dataset.id;

  if (shouldFilterManufacturers && !displayedManufacturers.includes(boardId)) {
    return false;
  }

  if (shouldFilterMcufamilies && !displayedMcufamilies.includes(boardId)) {
    return false;
  }

  if (shouldFilterFeatures && !displayedFeatures.includes(boardId)) {
    return false;
  }

  if (downloadsSearch.searchTerm) {
    const downloadData = [
        download.dataset.name,
        download.dataset.id,
        download.dataset.manufacturer,
        download.dataset.mcufamily,
        download.dataset.features,
        download.dataset.tags,
        download.dataset.modules,
    ].join(" ").toLowerCase();


    for (const term of downloadsSearch.searchTerm.toLowerCase().split(" ")) {
        if (!
            (downloadData.includes(term) ||
             downloadData.includes(term.replaceAll("-", "")))) {
            return false;
        }
    }
  }

  return true;
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

window.addEventListener('load', function () {
    document.querySelector("#search").focus();
});
