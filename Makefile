APP_NAME ?= QMap
APP_PLATFORM ?= Python
BUILD_ID ?= $(shell git rev-parse --short HEAD)
SSH_USER ?= dmap
SSH_HOST ?= mars.cs.qc.cuny.edu

ssh-ok:
	sudo sed -i "20i\ForwardAgent yes" /etc/ssh/ssh_config && \
	sudo sed -i "35i\StrictHostKeyChecking no" /etc/ssh/ssh_config && \
	sudo apt-get install -y sshpass

update-backend:
	@sshpass -p ${SSH_PASS} ssh ${SSH_USER}@${SSH_HOST} "cd qmap; git pull"