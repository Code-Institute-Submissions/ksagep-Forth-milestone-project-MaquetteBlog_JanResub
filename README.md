# MaquetteNews Blog for modelers

I took the advice of my mentor and the teachers of the Code Institute's Diploma in Software Development Course and I have created a blog site which I liked and enjoyed the development of it.

For link to this website click [Here](https://ksagep.github.io/).

Design has been focused to *Desktop, Laptop and Tablet first* and *Responsive* but it is also working on mobile assets.

![My Image](media/pictures/xx.jpg)

## Who is this blog site for?

This blog page contains information about maquettes which are mainly aircrafts. These information would be interesting who makes maquette or who wants a little bit more info about a specific model.

## What does this website do?

The website serves as a collection of pictures and short descriptions of different maquettes. The registered users could like or comment any posts. Possibility of comment could provide a base for small conversation between users. The non-registered users can see the posts but they can not like or comment the posts.

## UX 5 Planes

### Strategy Plane

This page was created in a simple way. The information is clear and serves to help the visitors of the website.

### Scope Plane

In this project You can find the following features:
* The header and footer are common in every pages
* Three different pages which are as follows:

- Home page contains a picture what I took at the 'Queen's View' and two other buttons to other pages

![My picture](assets/images/home-page.jpg)

- Enjoy page contains pictures about drinks, foods and attractions which could visit during the trip

![My picture](assets/images/enjoy-page.jpg)

- Sign Up page contains the opportunity to create a contact with me and I could share some information in private session

![My picture](assets/images/signup-page.jpg)

### Structure Plane

The three pages provide various information about different themes. These provide a possibility for visitors that they could choose the most appropriate theme they would be interest in. 

### Skeleton Plane

Design was focused on big screen (desktop, laptop) primarily but you can use this website on mobile also.

### Surface Plane

* Colors

For navigation and footer part of the website the main aim was the big contrast it was the reason why I used #0a0a0a/black on a light background (beige - rgb 245, 245, 220).

* Typography

I used two types of fonts what I downloaded from the Google Fonts families:

**Tourney** (weight: 700)

**Oswald** (weight: 500)

## Features

### Existing Features

* Created in HTML5, CSS3, Django, Bootstrap
* One main page for registration or sign-in and currently two different pages for posts (6 posts by page)

### Features for future implementation

* Grouping of posts according to different scales e.g. 1/72, 1/48, 1/35 etc.
* Upload more than one picture to the post
* Special icons before the username
* 

## Technologies

- HTML5 for basic structure of the website
- CSS3 for style the website
- Google Fonts for fonts families
- Font Awesome for social media icons
- Git for version control
- GitHub for storage the files and steps of development of the website

## Resources

- Code Institute course materials
- Code Institute Slack Community for some helps
- Code Institute Mentor meetings and support
- Code Institute tutor support
- Am I Responsive for a responsive image in README 
- the culture trip for some pictures of the food
- jolly tomato for image of the Scottish egg
- wikipedia for image of the black and white pudding
- cinnamonhotels for image of the grilled Scottish salmon
- candyfactory for image of the Irn-Bru
- ongewonlekker for image of the Botanist gin
- tasteatlas for image of the Atholl Brose, Glayva, Scottish beers
- wikipedia for image of the Scottish whiskies

## Testing

### Browser testing

Website was tested in Google Chrome, Opera, Microsoft Edge and Safari. On each browser this website works properly (functionality, visuality).

It was tested on  Macbook Pro, Apple iPhone 13 Pro and Samsung A6 and A10 mobile phones and the website worked on these type of devices.

### Validators

The website was checked by W3C HTML validator and it did not reported any issues. You can find the result [Here](assets/images/W3C%20HTML%20assessment.jpg).

The website was checked by W3C CSS validator and it did not reported any issues. You can find the result [Here](assets/images/W3C%20CSS%20assessment.jpg).

### Local testing

The buttons of the website were tested locally and these worked properly.

### Responsiveness

I used Google Chrome Dev Tools for this exercise. I tested for mobile and desktop devices. According to the tool, some images were big for mobile devices and the downloads were slow.

Lighthouse mobile assessment:
![My Image](assets/images/lighthouse_mobile_assessment.jpg)

Lighthouse desktop assessment:
![My Image](assets/images/lighthouse_desktop_assessment.jpg)

## Version control

I used two repositories during the development: GitPod for local repository and GitHub for remote or background repository. 

I managed the versions with the followung process:
- I created a repository in GitHub
- I opened and developped the repository in GitPod
- I created and developped the files and folders in GitPod
- I saved and pushed my works to GitHub repository:
    1. git add . - adding work to git
    2. git commit -m "Commit message" - to commit the stage of work
    3. git push - to update my work in GitHub

## Publish the project

The steps of the publishing on the GitHub were as follow:
    
    1. **"Settings"** on the repository
    2. **"Source"** of "GitHub Pages" selected *master for Branch* and saved it
    3. The website was published on GitHub Pages and the link was provided in the same section.

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome ksagep,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
