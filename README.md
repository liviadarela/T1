# Sistema de Gerenciamento de Locadora de Veículos
Este é um sistema orientado a objetos, desenvolvido em Python, para o gerenciamento de uma locadora de veículos. O sistema oferece funcionalidades para cadastro de veículos, clientes, locações e geração de relatórios, garantindo o cumprimento de regras de negócio específicas para o processo de locação

## 📖 Sobre o Projeto

A locadora gerencia uma frota de veículos e mantém o registro de clientes e locações. O sistema deve permitir:

Cadastro, alteração, visualização e exclusão de veículos e clientes.
Registro de locações e devoluções, com atualização automática da disponibilidade dos veículos.
Geração de relatórios para auxiliar na gestão da locadora.

## 🚀 Funcionalidades

1. Cadastro de Veículos
    - Veículos podem ser cadastrados com atributos como placa, modelo, marca, ano, valor por dia e status.
    - Tipos de veículos:
      - Carro: Inclui a categoria (popular ou luxo).
      - Moto: Inclui adicional de seguro.
      - Caminhão: Inclui número de eixos.
    - Veículos podem ser excluídos do sistema.
      
2. Gerenciamento de Clientes
    - Cadastro, alteração, exclusão e visualização de clientes.
    - Atributos incluem CPF, nome, data de nascimento, endereço, e CNH (composição com cliente).
     
3. Registro de Locações
    - Registro de locações com atributos como data de início, data de término, veículo alugado e cliente.
    - Funcionalidades:
       - Realizar aluguel (realizar_aluguel).
       - Alterar datas do aluguel.
       - Registrar devoluções.
       - Listar alugueis realizados.
       
4. Geração de Relatórios
     - Relatório de Locações por Período: Mostra veículos alugados em um intervalo de tempo.
     - Relatório de Clientes: Lista todos os clientes cadastrados.

## 🛠️ Tecnologias Utilizadas

**Linguagem:** 
  - Python 3.x.

**Bibliotecas:**
  - PySimpleGUI: Interface gráfica.

**Paradigmas:**
  - Programação orientada a objetos (POO).
  - Utilização de herança, associação, composição e classes abstratas.
  - Utilização de interface grafica e persistência de dados 

## 📦 Instalação

**Clone este repositório:** git clone https://github.com/liviadarela/T1.git

**Instale as dependências necessárias:** pip install PySimpleGUI

**Execute o sistema:** python main.py
