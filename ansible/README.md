# Ansible

This folder contains files for Ansible which performs a tasks of deploying the web application using Docker. Note that I have used Ansible v.2.8.18, so it was tested only on this version.

## Roles

This Ansible configuration contains 3 roles:

 * **pip-install**. One of the tasks requires pip, which usually is not installed on Ubuntu by default. This role implements tasks for installing pip through apt.
 * **docker-install**. This roles provides task for installation of the docker, which is neithe installed by default nor exists in default Ubuntu apt repository.
 * **docker-deploy**. This role deploys the web application.

## Usage

Ansible playbook located in _playbooks_ folder is automatically plays on Vagrand usage (`vagrant up`). You can run this playbook manually using `vagrant up --provision` command.
