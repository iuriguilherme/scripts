#!/bin/bash
## Inicia um serviço ices2 pré configurado

CANAL=""

if  [ ! -z $1 ]
then
	CANAL="${1}"
fi

/usr/bin/ices2-${CANAL} ${HOME}/ices2.d/${CANAL}-playlist.xml
