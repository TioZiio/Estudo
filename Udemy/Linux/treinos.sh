#!/bin/bash


# Exemplo 1 – Enviando parâmetros posicionais para uma função.
function imprimir
{
	echo $1
	echo $2
	echo $0
	echo $#
}
imprimir $*

echo '#####################################'

function variaveis
{
	dois=2
	tres=3
	local quatro=4
	local cinco=6
}
dois=david
quatro=jose
variaveis
echo $dois $tres $cinco $quatro

echo '####################################'
val=(perci arthur tiozio)
echo ${val[1]}
echo ${val[2]}
echo ${val}
echo '####################################'
A=4 
B=2
echo "$A + $B = $(( A + B )) -> soma"
echo "$A + $B = $(( A - B )) -> subtração"
echo "$A + $B = $(( A * B )) -> multpicação"
echo "$A + $B = $(( A / B )) -> divisão"
echo '####################################'

var=($("date"))
data=${var[4]}
echo $data
echo "${data:0:2}"
echo "${data:3:2}"
echo "${data:6}"

echo '##################################'


