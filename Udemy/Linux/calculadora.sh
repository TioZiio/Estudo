#!/bin/bash

clear
printf "\n\n"

echo "############### Calculadora ###############"
echo ''

# Eu escolhi duas possibilidades de calculadora, apenas para aprendizado, pois,
# durante os estudos encontrei a forma de calcular usando o BC (Basic Calculator),
# que é uma linguagem de calculo que suporta operações aritméticas interativas.
# Logo, a Calculadora complexa faz todas as operações que a simples e vai além.
 
function calculadora()
    # Escolha de qual calculadora usar;
{
    echo "Escolha qual calculadora deseja:"
    echo "[1] Simples"
    echo "[2] Complexa"
    echo -n "Escolha: "
    read escolha
    echo ''
}

function calculadora_valores_simples()
    # Pegando os valores do Usuário;
{
    echo -n 'Digite o Primeiro valor: '
    read valor_1

    echo -n 'Digite o Segundo valor: '
    read valor_2
    echo ''
}

function calculadora_apresentacao_simples()
    # Escolha de qual operação será feita;
{
    echo 'Escolha a operação:'
    echo '  (+) - Soma'
    echo '  (-) - Subtração'
    echo '  (*) - Multiplicação'
    echo '  (/) - Divisão'
    echo ''
    echo -n 'Operação: '
    read operador
    echo ''
}

function calculadora_calculo_simples()
    # Cálculo completo da operação.
    # Contém um validador final, para não gerar erro durante a execução do script;
{
    case $operador in
        +)
            resultado=$( echo "$valor_1 + $valor_2" | bc )
            verificador=1
        ;;
        -)
            resultado=$( echo "$valor_1 - $valor_2" | bc )
            verificador=1
        ;;
        \*)
            resultado=$( echo "$valor_1 * $valor_2" | bc )
            verificador=1
        ;;
        /)
            resultado=$(echo "scale=1; $valor_1 / $valor_2" | bc )
            verificador=1
        ;;
        *)
            echo "Escolha de operador Inválido!"
            echo "Sua escolha ($operador);"
            verificador=0
        ;;
    esac
}

function calculadora_complexa()
    # Recebe a operação do Usuário
    # Durante o estudo, percebi que o BC não trabalha com operações que tenha  colchete [];
{
    echo 'Digite a expressão matemática'
    echo 'Nesta calculadora aceita ()+-*/'
    echo 'Exemplo 1: (2 + 5 - 6) ou (3 - 2 * 4)'
    echo 'Exemplo 2: 2* ( 5 - 3 ) + ( 2- (3 * 5)) + 1'
    echo -n "Expressão: "
    read complexa
}

function calculadora_calculo_complexo()
    # Calculo complexo final;
    # É utilizado o echo para passar o calculo como entrada para o comando BC,
    # por isso de sua utilização durante o calculo;
{
    resultado=$( echo "scale=2; $complexa" | bc)
    echo ''
}

calculadora # Chama a função de escolha da calculadora

# Avalia qual calculadora será usada:
if [ $escolha -eq 1 ]; then
    calculadora_valores_simples
    calculadora_apresentacao_simples
    calculadora_calculo_simples
    sleep 1
    # Verifica se ocorreu algum erro durante o processo de calculo:
    if [ $verificador -eq 1 ]; then
        echo "Calculo: $valor_1 $operador $valor_2 = $resultado"
    else
        echo 'Erro ao digitar comandos'
    fi
elif [ $escolha -eq 2 ]; then
    calculadora_complexa
    calculadora_calculo_complexo
    sleep 1
    echo "Calculo: $complexa = $resultado"
else
    echo "A sua escolha $escolha foi Inválida!"
fi

