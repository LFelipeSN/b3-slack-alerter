import os
import requests
from typing import Dict, Optional
from datetime import datetime

def send_slack_notification(webhook_url: str, message: str):
    payload = {"text": message}
    try:
        response = requests.post(webhook_url, json=payload, timeout=10)
        response.raise_for_status()
        print("Notificação enviada com sucesso para o Slack!")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao enviar notificação para o Slack: {e}")

#  Busca cotação de um ativo na B3
def get_quote(ticker: str, token: str) -> Optional[Dict]:
    url = f'https://brapi.dev/api/quote/{ticker}?range=1mo&interval=1d&token={token}'
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Erro ao buscar cotação para {ticker}: {e}')
        return None

def processar_tickers(lista_tickers: list, token_api: str) -> list:
    msgs = []
    for ticker_ativo in lista_tickers:
        data = get_quote(ticker_ativo, token_api)
    
        if data and 'results' in data and data['results']:
            q = data['results'][0]
            
            symbol = q.get('symbol', 'N/A')
            name = q.get('longName', 'N/A')
            price = q.get('regularMarketPrice')
            change = q.get('regularMarketChange')
            change_percent = q.get('regularMarketChangePercent')
            currency = q.get('currency', 'BRL')
            market_cap = q.get('marketCap')
            fifty_two_week = q.get('fiftyTwoWeekRange', 'N/A')
            
            if price is not None and change_percent is not None:
                m_cap_str = f"{market_cap:,.2f}" if market_cap else "N/A"
                
                tendencia = "📈" if change > 0 else "📉" if change < 0 else "➖"
                sinal = "+" if change > 0 else ""
                
                msg = (
                    f"🔹 *{symbol}* | _{name}_\n"
                    f"  💵 *Preço:* {currency} {price:.2f}\n"
                    f"  {tendencia} *Variação:* {sinal}{change_percent:.2f}% ({currency} {sinal}{change:.2f})\n"
                    f"  🏢 *Valor de Mercado:* {currency} {m_cap_str}\n"
                    f"  📊 *Faixa 52 Semanas:* {fifty_two_week}"
                )
                print(msg + "\n")
                msgs.append(msg)
            else:
                msg = f"⚠️ *{symbol}* - {name}: Sem dados de preço atuais."
                print(msg + "\n")
                msgs.append(msg)
    return msgs

def enviar_resumo_mercado(mensagens: list, webhook_url: str, titulo: str):
    """Gera o cabeçalho com a data atual, formata os dados e envia para o Slack."""
    if not mensagens or not webhook_url:
        return
        
    now = datetime.now()
    data_hora = now.strftime("%d/%m/%Y às %H:%M:%S")
    
    cabecalho = f"{titulo}\n📅 _Gerado em {data_hora}_"
    msg_completa = f"{cabecalho}\n\n" + "\n\n".join(mensagens)
    
    send_slack_notification(webhook_url, msg_completa)