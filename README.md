# tornado-base-project

Simple architecture of a Tornado project. 

## Basic usage:

#### make deps
It's gonna install all deps your project needs in order to run a simple Tornado "Hello World". You can put your dependences inside "requirements" file and always type `make deps` to make sure your environment is up to date.

#### make run
Starts your application. By default the project will listen to port 8888. You should rename 'project' folder to your project name and after it reconfigure your "make run" rule.

#### make clear
Removes .pyc cache files.

## Read the docs
Tornado Stable Version:
http://www.tornadoweb.org/en/stable/

## TODO:
* include test-cases to show how to test Tornados features;
* define a basic API using tornado's async features;
