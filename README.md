# fileflightplans

https://fileflightplans.herokuapp.com/kml/

## Introduction

This is a preliminary website for creation and downloading of flight-plan related files. 
The project was borne out of my difficulties with the existing flight plan system.
My goal is to eventually replace the existing system with a better one that is more clear for users.

To start, I wanted to make the drawing of the flight boundaries easier. This is currently done by
using Google Earth and exporting .kml files of polygons. The inner boundaries were difficult to
draw just by eyeballing and could be easily automatically generated.

The program currently performs best when the boundaries of flight are large. Unfortunately, for
smaller boundaries, the drawn bounds aren't as far away as I would like. Still, they do the job
and the file output by the program is still a .kml so it can easily be edited.

## Standalone Program

### Installation

This is a Python program. Make sure you have Python 3.6+ installed on your system. I like to work
in a virtual environment which can be created by running:

```
python -m venv drawkmlenv
```

And activated as follows:

Linux:
```
source drawkmlenv/bin/activate
```

Windows:
```
drawkmlenv\Scripts\activate
```

Once in the virtual environment, run the following commands to download and install packages:
```
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Running

You can run the standalone version of this program by running the following command:

```
python draw_kml.py <name of file> <max speed in m/s>
```

Use this command to show the version number:
```
python draw_kml.py -v
```

### Long-term Goals

- Create fixed-wing KML generator
- Create data model
- Create form for full flight plan
- Create admin interface for approval
- Create tutorials
- Custom 404/500 pages

### Bugs

- Setting max_speed to be too high causes the KML output to be crazy