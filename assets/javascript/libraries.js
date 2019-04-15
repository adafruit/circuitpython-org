document.addEventListener('DOMContentLoaded', function() {
  async function getLatestReleases() {
    let response = await fetch('https://api.github.com/repos/adafruit/Adafruit_CircuitPython_Bundle/releases/latest');
    let data = await response.json();
    return data;
  }

  function buildReleaseLinks(data) {
    let releaseList = document.querySelector('.release-list');

    data.assets.forEach(function(asset) {
      let liElement = document.createElement('li');
      let linkElement = document.createElement('a');
      linkElement.title = asset.name;
      linkElement.href = asset.browser_download_url;
      let linkText = document.createTextNode(asset.name);
      linkElement.appendChild(linkText);
      liElement.appendChild(linkElement);
      releaseList.appendChild(liElement);
    });
  }

  getLatestReleases().then(buildReleaseLinks);
});
