# CircuitPython organization site

TODO
- [ ] add feed_meta and seo tags to layout head
- [ ] setup github_pages gemfile
- [ ] favicons
- [ ] filtering and sorting of Downloads
- [x] layout of Downloads
- [ ] responsive sizes
- [x] download details pages
- [x] landing page
- [ ] news page
- [x] help page
- [x] setup travis for generate_downloads.rb
- [x] update header to latest version (different logo)
- [x] deploy accounts, and update url to accounts production in download.js
- [ ] authenticate github api for newsletter posts


# To add a new board to the site:

1. Edit _data/metadata.json and add a new object in the array with the board details.
2. Commit and push the code. A file will be automatically generated in _downloads/board_id.description_type
3. Edit the description and save the file
