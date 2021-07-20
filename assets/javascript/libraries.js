document.addEventListener('DOMContentLoaded', function() {
  async function getLatestReleases() {
    let response = await fetch('https://api.github.com/repos/adafruit/Adafruit_CircuitPython_Bundle/releases/latest');
    let data = await response.json();
    return data;
  }

  function buildReleaseLinks(data) {
    let releaseList = document.querySelector('.release-list');

    data.assets.forEach(function(asset) {
      let name = asset.name;

      if (name.slice(-6) === 'ignore') {
        // any .ignore files in the assets list
        return;
      }

      let versionId = name.replace(/(-[\d]+.zip$)/, '');
      let versionElement = document.getElementById(versionId);

      if (!versionElement) {
        // likely an older version we don't want to link to, such as 2.x
        return;
      }

      let iconElement = document.createElement('i');
      iconElement.className = "fas fa-download";

      let linkElement = document.createElement('a');
      linkElement.title = "Library Bundle Download";
      linkElement.href = asset.browser_download_url;
      linkElement.className = "purple-button-link";
      let linkText = document.createTextNode(asset.name);
      linkElement.appendChild(linkText);
      linkElement.appendChild(iconElement);
      versionElement.appendChild(linkElement);
    });
  }

  getLatestReleases().then(buildReleaseLinks);
});
