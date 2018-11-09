document.addEventListener('DOMContentLoaded',function() {
  var searchElement = document.getElementById("search");

  searchElement.addEventListener('keyup', function(event) {
    var regex = new RegExp(searchElement.value, "gi");

    var i, downloads = document.getElementsByClassName("download");
    for (i = 0; i < downloads.length; i++) {
      download = downloads[i];
      var id = download.dataset.id;

      if (id.match(regex)) {
        download.style.display = 'block';
      } else {
        download.style.display = 'none';
      }
    }
  });
});
