#### circuitpython.org Documentation Pages

## Documentation for Hero Images on the circuitpython.org homepage

The hero, or main, image is the picture seen when first arriving on the circuitpython.org website. As this is 
a major part of the look and feel of the site, care should be taken to ensure the image used fits established 
specifications and aesthetics. 

### Hero Image Specifications

- Hero images are stored in the /assets/images/heros directory in the repo.
- The images can be .png or .jpg files.
- The image size must be 1440 pixels by 800 pixels.
- The image ideally will be composited such that overlay text for the page blends into the style of the image.

### Where the Hero Image is specified in the Site Layout

The hero image on circuitpython.org may be changed by editing a value in the **_config.yml** file.

The **_config.yml** file is located in the root directory of the circuitpython.org repo on GitHub.

The typical contents (truncated after a number of lines) is similar to:

    title: CircuitPython
    email: justin@adafruit.com
    description: >-
      The easiest way to program microcontrollers
    site_image: "https://circuitpython.org/assets/images/CircuitPythonLogo_Black.png"
    **hero_image: CircuitPython_Hero.jpg**
    timezone: America/New_York
    twitter_username: circuitpython
    github_username:  adafruit
    baseurl: ""
    url: "https://circuitpython.org"
    paginate: 5
    excerpt_separator: <!--more-->
    permalink: pretty ...

### Adding New Potential Hero Images to the Repository

If you wish to add a new image not previously loaded on circuitpython.org, use the web browser to go to 
[https://github.com/adafruit/circuitpython-org/tree/master/assets/images/heroes](https://github.com/adafruit/circuitpython-org/tree/master/assets/images/heroes).

Using your operating system file explorer/finder, drag a properly formatted image file onto the center of the GitHub screen. 
GitHub should grab the file and format a pull request. You can continue to drag additional hero images to the screen if you wish.

To add the files:
- Scroll to the bottom of the page and put a description of the edit in the box marked "Add files via upload"
- Keep the value "Create a new branch for this commit and start a pull request" checked.
- Click the green "Commit changes" button.

This will place you in a new screen where you can describe the changes you have made in the "Leave a comment" block.

When ready, click the green "Create pull request" button.

The reviewers for circuitpython.org website content will review your change and accept it if all is ok. You can see the names of the 
reviewers on the right of the screen.

### To Change the Hero Image

First, ensure that a properly formatted hero image is in the /assets/images/heroes directory. 

Edit **_config.yml**. This is best done with the text edit tool built into GitHub. To do this:

- Go to [https://github.com/adafruit/circuitpython-org/blob/master/_config.yml](https://github.com/adafruit/circuitpython-org/blob/master/_config.yml) 
and click on the pencil icon on the right side.
- Go down to find the value "hero_image:"
- Replace the filename. For example, replace the text CircuitPython_Hero.jpg with the new name of a file placed in /assets/images/heroes, 
for example Gamer_Hero.png.
- Scroll to the bottom of the page and put a description of the edit in the box marked "Update _config.yml"
- Keep the value "Create a new branch and start a pull request" checked.
- Click the green "Commit changes" button.

This will place you in a new screen where you can describe the changes you have made in the "Leave a comment" block.

When ready, click the green "Create pull request" button.

The reviewers for circuitpython.org website content will review your change and accept it if all is ok. You can see the names of the 
reviewers on the right of the screen.

Revision 2020-02-05 Anne Barela
