
# Atividade - Pytest

Descrição:


## Instalação

Instalação do pytest:

É necessário ter o Python instalado em sua maquina e usar ambiente virtuai, 
Para instalar o ambiente virtual basta usar o código logo abaixo:
```bash
  python -m venv venv
  
```
E logo em seguida ativá-lo usando:
#### No Windows:
```bash
  .\venv\Scripts\activate
```
Logo após, instale o pytest:
```bash
    pip install pytest
```

## O Teste de Funções:

O test foi realizado para identifica se os valores são válidos para um teste funcional. Para que seja válido o teste deve
começar com letra, conter apenas letras e números, e ter no mínimo 1 caractére e 
no máximo 6. 

src/identifier/identifier.py fica a função.

tests/test_identifier.py saonde ficam os testes das funções

esses foram os casos de testes escolhidos a serem executados.
## Testes do programa:


| ID | Steps | Test Data | Expected Results | Actual Result|
|----|--------|-----------|---------|----------|
| 1| Usuario informa letras|Inserir letras e numero| Ab56| Válido|
| 2| Usuario informa letras|Inserir letras| aaaaaa| Válido|
| 3| Usuario informa letras|Inserir letras| 78787848484| Inválido|
| 4| Usuario informa letras|Inserir letras| #/*| Inválido|
| 5| Usuario informa letras|Inserir letras| a026456| Inválido|
| 6| Usuario informa letras|Inserir letras| | Inválido|





