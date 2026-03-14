import os
from dotenv import load_dotenv
from core import processar_tickers, enviar_resumo_mercado

load_dotenv()
webhook_acoes = os.getenv('WEBHOOK_ACOES')
webhook_fiis = os.getenv('WEBHOOK_FIIS')
token = os.getenv('TOKEN')

acoes = [
    'BBAS3', 'PETR4', 'ITSA4', 'VALE3', 'ITUB4', 
    'ALOS3', 'BBDC4', 'CPLE3', 'DIRR3', 'MOTV3', 
    'RADL3', 'VIVT3'
]
fiis = ['MXRF11', 'GARE11', 'XPML11', 'HGLG11', 'KNCR11']

print("Buscando dados de AÇÕES...")
mensagens_acoes = processar_tickers(acoes, token)

print("Buscando dados de FIIs...")
mensagens_fiis = processar_tickers(fiis, token)

enviar_resumo_mercado(mensagens_acoes, webhook_acoes, "📊 *Resumo do Mercado - Ações* 📊")
enviar_resumo_mercado(mensagens_fiis, webhook_fiis, "🏢 *Resumo do Mercado - FIIs* 🏢")