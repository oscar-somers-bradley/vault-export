#vars
IMAGENAME=vault_export
VERSION=0.1
IMAGEFULLNAME=${IMAGENAME}:${VERSION}

build:
	    @docker build -t ${IMAGEFULLNAME} .

all: build
