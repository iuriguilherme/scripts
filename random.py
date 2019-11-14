#!/usr/bin/env python
# -*- coding: utf-8 -*-
## Cria uma senha pseudo aleatória boa pra criptografia

import binascii, os, sys

## Usar 8 como tamanho por omissão se nenhum parâmetro for fornecido
tamanho = 8

## Caso um número seja fornecido, use-o como tamanho
if len(sys.argv) > 1 and str(sys.argv[1]).isdigit():
  tamanho = int(sys.argv[1])

print(binascii.hexlify(os.urandom(tamanho)).decode('utf-8'))

