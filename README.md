
# CircuitPython organization site
A more detailed gude for adding a board to CircuitPython can be found in the
following Adafruit Learn guide: [How to add a New Board to the circuitpython.org website](https://learn.adafruit.com/how-to-add-a-new-board-to-the-circuitpython-org-website)

**To add a new board to the site:**

1. Duplicate `template.md` to `_board/<board id>.md`.
2. Edit `_board/<board id>.md` according to the template's instructions.
3. In your `_board/<board id>.md` you will specify a `board_image`. Create 3
versions of this file, in the following sizes and folder locations:

|Size|File|Dimensions (px)|
|--|--|--|
|Original|assets/images/orignal/{board_image}|900px+ width and 4:3 ratio width|
|||example: 900 x 675|
|Large|assets/images/large/{board_image}|800 x 600|
|Small|assets/images/small/{board_image}|300 x 225|

> For more information on preferred images or if you prefer or must use 13:10 see
> [Preparing the Images](https://learn.adafruit.com/how-to-add-a-new-board-to-the-circuitpython-org-website/preparing-the-images)
> in the Adafruit Learn guide

4. Create a pull request with the file changes.

**To test your changes locally:**

1. You need "ruby" and "ruby-bundler" installed locally.  These instructions
were tested with ruby 2.5 and ruby-bundler 1.17.3 on a Debian Stretch system.
2. As needed, `git submodule update --init --recursive` to fetch the submodules
3. One time, run `bundle config set path 'vendor/bundle' && bundle install`
4. Run `bundle exec jekyll serve` to generate the site locally
5. Visit the displayed "server address"
6. After most local edits, the content will be updated.  You will need to
reload (ctrl-r or F5) your browser

Note: For faster jekyll builds, you can use the `--incremental` flag. You'll
also want to install ruby with yjit enabled for even faster builds.
