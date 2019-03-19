document.addEventListener('DOMContentLoaded',function() {
  var searchElement = document.getElementById("search");
  searchElement.addEventListener('keyup', handleSearch);

  var filterElement = document.querySelector(".downloads-filter .filter");
  filterElement.addEventListener('click', displayFilter);
});

function handleSearch(event) {
  var regex = new RegExp(event.target.value, "gi");

  var i, downloads = document.getElementsByClassName("download");
  for (i = 0; i < downloads.length; i++) {
    download = downloads[i];
    var name = download.dataset.name;

    if (name.match(regex)) {
      download.style.display = 'block';
    } else {
      download.style.display = 'none';
    }
  }
}

function displayFilter(event) {
  var manufacturers = [];
  var downloads = document.querySelectorAll('.download');

  downloads.forEach(function(download) {
    if (manufacturers.indexOf(download.dataset.manufacturer) === -1) {
      manufacturers.push(download.dataset.manufacturer);
    }
  });

  setupManufacturers(manufacturers);

  toggleFilterContainer();
}

function toggleFilterContainer() {
  var filterContainer = document.querySelector('.downloads-filter-content');

  if (filterContainer.style.display == 'grid') {
    filterContainer.style.display = 'none';
  } else {
    filterContainer.style.display = 'grid';
  }
}

function setupManufacturers(manufacturers) {
  var manufacturerList = document.querySelector('.manufacturers .content');

  manufacturers.forEach(function(manufacturer) {
    var li = document.createElement("li");
    var checkbox = document.createElement('input');
    checkbox.type = "checkbox";
    checkbox.name = "manufacturer";
    checkbox.value = manufacturer;

    li.appendChild(checkbox);
    li.appendChild(document.createTextNode(manufacturer));

    manufacturerList.appendChild(li);
  });
}
