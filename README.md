# ESC-CTF-2016

This repository contains all the files required to play the challenges used during the ESC CTF 2016.

By cloning the repository you will get all the binaries and scripts that are needed to play the challenges

All challenges are running inside docker containers, this means you need docker to run them.

## what is missing
I didn't manage to upload the CTF platform, not that you need it anyway

Also some challenges are missing because they were not dockerized and were running on a separate VM.
When ready for publishing, the VM will be made available on VulnHub (www.vulnhub.com)

## challenges

### baby pwnables
- the initiation: listening on port 10010
- one in ten: listening on port 10040
- obo: listening on port  10050
- big or small: listening on port 10060

### pwnables
- The Inquest Lab: listening on port 10020
- Procedure: Listening on port 10030
- MiddleFingerD: Listening on port 79

### web
- Itadakimasu: Listening on port 5000
- Bilab: Listening on port 80

## Quick setup

- clone this repository
- go to the launcher directory
- run the script for the challenge you want to play
- play!

### Notes on web challenge BiLab
Bilab makes use of virtual hosts and you need to setup your network accordingly.
this challenge runs 2 web servers running behind an NGINX proxy
the machine where the proxy is running must resolve both as
- ssts.ctf.esc
- intranet.ctf.esc
