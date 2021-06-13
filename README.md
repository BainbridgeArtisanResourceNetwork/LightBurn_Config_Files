# LightBurn Config Files

This repo is where the BARN ETA studio is keeping the configuration  files for the LightBurn software that we use with our two laser  cutter/engravers.

## Files we intend to keep here

- LightBurn Cut Library for Little Blue 
- LightBurn Cut Library for Big Red 
- Python script for merging Cut libraries from Little Blue and Big Red 
- LightBurn Default config file for Little Blue LightBurn Default config file for Big Red

## Use Models

### Cut Libraries

The computers that control Little Blue and Big Red will each contain a clone of this repo in their C:/users/maker/documents/Lightburn directory. The cut library loaded into LightBurn when the app starts will be the version that matches the laser the computer is connected to.   The cut libraries on those machines will evolve over time and the changes committed back to this repo.

The python script that merges the cut libraries will be run periodically on the Little Blue and Big Red libraries in this repo to create a merged cut library. 

The workstations in the Studio  that are not directly connected to a laser will  also each contain a clone of this repo in their C:/users/maker/documents/Lightburn directory. The cut library loaded into LightBurn when the app starts will be the merged version of the Little Blue and Big Red cut libraries.

Members with their own copies of LightBurn can clone this repo (or just download any of the cut libraries) for their own use.



### Default config files

One day, we hope to understand how to create a user config file for LightBurn that will enable us to force LightBurn to start in a specific configuration. This will eliminate the challenges that happen when changes a user makes for their project carries over to the next user.
