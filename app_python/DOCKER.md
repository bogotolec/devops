# Docker

The information about docker container.

## Image

It is good practice to use specific base image for the python applications. For example, the one whi I have used `python:3.9-alpine`.

## User permissions

For the container I have created a new user with restricted permissions because of security reasons. (Default user is _root_, which leaves some possibilites to harm the system)