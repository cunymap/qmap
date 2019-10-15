APP_NAME ?= QMap
APP_PLATFORM ?= Python
BUILD_ID ?= $(shell git rev-parse --short HEAD)
GIT_REPO ?= 
SSH_HOST ?= mars.cs.qc.cuny.edu
SSH_USER ?= dmap


ssh-ok:
	sed -i "20i\ForwardAgent yes" /etc/ssh/ssh_config && \
	sed -i "35i\StrictHostKeyChecking no" /etc/ssh/ssh_config

update-backend:
	ssh ${SSH_USER}@${SSH_HOST} "cd qmap; git pull"