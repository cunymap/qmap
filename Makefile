APP_NAME ?= QMap
APP_PLATFORM ?= Python
BUILD_ID ?= $(shell git rev-parse --short HEAD)
SSH_HOST ?= mars.cs.qc.cuny.edu

ssh-ok:
	sudo sed -i "20i\ForwardAgent yes" /etc/ssh/ssh_config && \
	sudo sed -i "35i\StrictHostKeyChecking no" /etc/ssh/ssh_config

update-backend:
	ssh ${SSH_HOST} "cd qmap; git pull"