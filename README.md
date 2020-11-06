# CircuitPython organization site

**To add a new board to the site:**

1. Duplicate `template.md` to `_board/<board id>.md`.
2. Edit `_board/<board id>.md` according to the template's instructions.
3. Provide 3 images. An original high-quality image. A smaller image (300 px width),
and a larger image (700 px width) in each respective directory (assets/images/boards/{small large original})
and process them in something like https://squoosh.app/ to reduce file size. If
you only have one image, place it in the 'original' folder.
3. Create a pull request with the file changes.

**To test your changes locally:**

1. You need "ruby" and "ruby-bundler" installed locally.  These instructions
were tested with ruby 2.5 and ruby-bundler 1.17.3 on a Debian Stretch system.
2. As needed, `git submodule update --init --recursive` to fetch the submodules
3. One time, run `bundle config set path 'vendor/bundle' && bundle install`
4. Run `bundle exec jekyll serve` to generate the site locally
5. Visit the displayed "server address"
6. After most local edits, the content will be updated.  You will need to
reload (ctrl-r or F5) your browser
