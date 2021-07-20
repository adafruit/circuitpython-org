document.addEventListener('DOMContentLoaded', function() {
  async function getBoardStats() {
    let response = await fetch('https://api.github.com/repos/adafruit/circuitpython/releases');
    let data = await response.json();
    return data;
  }

  function buildBoardStats(data) {
    let boards = [];

    clearLoadingIndicator();

    data.forEach(function(release) {
      displayBoardHeader(release);

      release.assets.forEach(function(asset) {
        let board_name = asset.name.split('-')[2];
        let index = boards.findIndex(board => board.name === board_name);

        if (index === -1) {
          boards.push({name: board_name, downloads: asset.download_count});
        } else {
          boards[index].downloads += asset.download_count;
        }
      });

      boards.sort(function(a, b) {
        return b.downloads - a.downloads;
      });

      displayBoardStats(boards);
    });
  }

  function clearLoadingIndicator() {
    let contentElement = document.querySelector('.stats-wrapper');
    contentElement.innerHTML = "";
  }

  function displayBoardHeader(release) {
    let contentElement = document.querySelector('.stats-wrapper');
    let h2Element = document.createElement('h2');
    let nameContent = document.createTextNode(`${release.tag_name} - ${release.name}`);
    h2Element.appendChild(nameContent);
    contentElement.appendChild(h2Element);
  }

  function displayBoardStats(boards) {
    let contentElement = document.querySelector('.stats-wrapper');
    let table = document.createElement('table');

    //header row
    let thead = table.createTHead();
    let tr = thead.insertRow();
    tr.insertCell().appendChild(document.createTextNode("Board"));
    tr.insertCell().appendChild(document.createTextNode("Downloads"));

    let tbody = table.createTBody();

    boards.forEach(function(board) {
      let tr = tbody.insertRow();
      let name = document.createTextNode(board.name);
      let downloads = document.createTextNode(board.downloads);
      tr.insertCell().appendChild(name);
      tr.insertCell().appendChild(downloads);
    });

    contentElement.appendChild(table);
  }

  getBoardStats().then(buildBoardStats);
});
