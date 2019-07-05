# Manifold Ansible Demo

This repo houses code used in the [Manifold Ansible Integration blog
post](link-tbd). It’s set up to provision a simple Python application which
pushes logs to LogDNA.  Credentials necessary to authenticate with LogDNA are
fetched from Manifold using the [Ansible Manifold Lookup
plugin](https://docs.ansible.com/ansible/latest/plugins/lookup/manifold.html).
Running this demo on your machine requires: a Manifold.co account

Running this demo on your machine requires:
- a [Manifold.co](https://manifold.co) account
- [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) 2.8 or higher
- [Vagrant](https://www.vagrantup.com/downloads.html)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

To run the demo:
1. Edit the resource name and project name in `provision/roles/app/tasks/main.yaml` to match an existing project and resource in your Manifold account
1. Export `MANIFOLD_API_TOKEN=<your-api-token>`
1. From `./provision` run `vagrant up`

See also the [Manifold Ansible integration documentation](tbd).
