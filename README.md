# B3 Slack Alerter
![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=ORANGE&style=for-the-badge)

Um script automatizado em Python que busca a cotação de Ações e FIIs e envia um resumo agradável e formatado diretamente para canais do Slack.

## Indice
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Utilizando o projeto](#utilizando-o-projeto)
- [Funções](#funções)
- [Autores](#autores)

## Tecnologias Utilizadas
**Linguagem:** ``Python``

## Utilizando o projeto
Antes de iniciar, é imprescindível configurar o arquivo `.env` na raiz do projeto contendo as credenciais necessarias:
- `TOKEN`: Seu token da API do brapi.dev
- `WEBHOOK_ACOES`: URL do webhook do Slack para ações
- `WEBHOOK_FIIS`: URL do webhook do Slack para FIIs

## Funções

### 1. Busca de Cotações
  Coleta os dados ao vivo de diversas Ações e Fundos Imobiliários na B3 usando a API da brapi.dev.
### 2. Tratamento e Formatação
  Processa os valores devolvendo o preço atual, tendência (alta/baixa), percentual de variação e valor de mercado de forma visual com emojis.
### 3. Integração e Notificação via Slack
  Gera e envia automaticamente relatórios unificados informando o resumo do mercado diretamente pra seus canais configurados no Slack.

## Autores
<div align="left">
  <a href="https://github.com/LFelipeSN" target="_blank">
    <img src="https://github.com/LFelipeSN.png" width="64" height="64" alt="LFelipeSN" style="border-radius:50%;margin-top:8px;" />
  </a>
</div>
