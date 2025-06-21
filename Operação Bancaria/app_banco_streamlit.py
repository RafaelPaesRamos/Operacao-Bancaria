
import streamlit as st
import datetime

# Inicialização de sessão
if "saldo" not in st.session_state:
    st.session_state.saldo = 0.0
    st.session_state.extrato = ""
    st.session_state.saques_realizados = 0

# Limites
LIMITE_SAQUE = 500.0
LIMITE_SAQUES_DIARIOS = 3

st.title("🏦 Banco Python Interativo")

# Entrada de valor
valor = st.number_input("Informe o valor (R$):", min_value=0.0, step=10.0, format="%.2f")

# Botões de ação
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Depositar"):
        if valor > 0:
            st.session_state.saldo += valor
            st.session_state.extrato += f"{datetime.datetime.now()}: Depósito de R$ {valor:.2f}\n"
            st.success(f"Depósito de R$ {valor:.2f} realizado!")
        else:
            st.warning("Informe um valor positivo.")

with col2:
    if st.button("Sacar"):
        if st.session_state.saques_realizados >= LIMITE_SAQUES_DIARIOS:
            st.warning("Limite diário de saques atingido.")
        elif valor > LIMITE_SAQUE:
            st.warning(f"Limite máximo por saque: R$ {LIMITE_SAQUE:.2f}")
        elif valor > st.session_state.saldo:
            st.warning("Saldo insuficiente.")
        elif valor <= 0:
            st.warning("Valor inválido.")
        else:
            st.session_state.saldo -= valor
            st.session_state.saques_realizados += 1
            st.session_state.extrato += f"{datetime.datetime.now()}: Saque de R$ {valor:.2f}\n"
            st.success(f"Saque de R$ {valor:.2f} realizado!")

with col3:
    if st.button("Mostrar Extrato"):
        st.subheader("📄 Extrato")
        if st.session_state.extrato:
            st.text(st.session_state.extrato)
        else:
            st.info("Nenhuma movimentação registrada.")
        st.write(f"💰 Saldo atual: R$ {st.session_state.saldo:.2f}")
