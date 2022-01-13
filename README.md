# autopull
Simple python tool that allows you to automatically pull from a github repository whenever a file with a specified name is uploaded
## installation 📲
1. clone the repo or download source as zip
2. choose the options you want in config.ini
3. clone the repository you want to pull from in the same directory as this program. ensure the directory name is the same as the repository's name.
4. `python main.py`: it will automatically pull the latest commits on startup and then listen for commits with your specified update filename
## config ⚙️
there are 5 options in the config.ini file, filename and sleeptime are not very necessary to change, but they are there if you want to change them anyway.  
### repo-name 📂
put the repository name here, it will use it to pull from the repository and also to know what your cloned directory is called.
### owner-username 🥶
put the repository's owner's name here.
### token 🪙
generate an api token by going to `Settings > Developer settings > Personal access tokens` and then clicking on `Generate new token` configure it however you'd like and then paste it into the config file.
### filename 🗄️
put the name of the file you want to trigger the update function here. file extensions also work
### sleeptime 💤
put the amount of time (in seconds) that you want the program to wait inbetween checks here.

## problem? 🤖
open an issue and i'll get back to you!  
feel free to leave feature requests, bug reports, or any other thing you need to let me know about.
