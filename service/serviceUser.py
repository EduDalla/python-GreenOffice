# -*- coding: windows-1252 -*-

import re
import random
import time
import logging
import sqlite3
from datetime import datetime

# Iniciando conexão com o banco de dados
conn = sqlite3.connect('greenoffice.db')
cursor = conn.cursor()

# Configurando o logger
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

moedas = 0
# regex para email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


def cadastro_usuario(nome, email, password):
    timecreated = int(datetime.now().timestamp())
    timemodified = int(datetime.now().timestamp())

    cursor.execute('''
    INSERT 
        INTO usuarios (nome, email, password, timecreated, timemodified)
    VALUES (?, ?, ?, ?, ?)
    ''', (nome, email, password, timecreated, timemodified))

    conn.commit()


def login_usuario(email, senha):
    cursor.execute('''
    SELECT *
        FROM usuarios
    WHERE email = ? AND password = ?
    ''', (email, senha))

    resultados = cursor.fetchall()
    if resultados:
        return resultados
    return False


def email_regex(msg):
    email = input(msg)
    # Definindo o padrão para um e-mail válido
    while not bool(re.match(regex, email)):
        email = input("Digite um email válido: ")

    return email


# Função que verifica se o email do usuário existe
def email_existe(email):
    cursor.execute('''
    SELECT *
    FROM usuarios
    WHERE email = ?
    ''', (email,))
    resultados = cursor.fetchall()

    if resultados:
        return email

    logger.warning(f"Email não encontrado: {email}")
    return False


def select_arcondicionados_by_id(id_usuario):
    cursor.execute('''
    SELECT *
    FROM arcondicionado
    WHERE id_usuario = ?
    ''', (id_usuario,))
    resultados = cursor.fetchall()

    if resultados:
        return resultados
    return False


def insert_mensagem(id_usuario, mensagem):
    timecreated = int(datetime.now().timestamp())
    timemodified = int(datetime.now().timestamp())

    cursor.execute('''
    INSERT
        INTO Mensagem (id_usuario, mensagem, timecreated, timemodified)
    VALUES (?, ?, ?, ?)
    ''', (id_usuario, mensagem, timecreated, timemodified))

    conn.commit()


def select_arcondicionado(id_arcondicionado):
    cursor.execute('''
    SELECT *
    FROM arcondicionado
    WHERE id = ?
    ''', (id_arcondicionado,))
    resultados = cursor.fetchall()

    if resultados:
        return resultados
    return False

def cadastrar_arcondicionado(id_usuario):
    try:
        nome_ar = input("Digite um nome para o ar condicionado: ")
        data_consumo = datetime.now().strftime('%Y-%m-%d')  # Data fixa no formato YYYY-MM-DD
        horas_consumo = random.uniform(8, 12)  # 8 horas e meia
        consumo_energia_kWh = random.uniform(8, 15)  # Consumo de energia calculado
        saude_do_ambiente = random.uniform(80, 100)  # Indicador de saúde ambiental
        timecreated = int(datetime.now().timestamp())
        timemodified = timecreated

        # Inserir os dados na tabela
        cursor.execute('''
        INSERT
            INTO Arcondicionado (Id_usuario, Nome, Data_consumo, Horas_consumo, Consumo_energia_kWh, 
        Saude_do_ambiente, Timecreated, Timemodified)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (id_usuario, nome_ar, data_consumo, horas_consumo, consumo_energia_kWh, saude_do_ambiente,
              timecreated, timemodified))
        conn.commit()
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")


# Função para deletar arcondicionado
def deletar_arcondicionado(id):
    try:
        cursor.execute(f'''
        DELETE
            FROM arcondicionado
        WHERE id = ?
        ''', (id,))

        conn.commit()
        if cursor.rowcount > 0:
            print(f"{cursor.rowcount} registro(s) deletado(s).")
        else:
            print("Nenhum registro encontrado para deletar.")
    except Exception as e:
        print(f"Erro ao deletar dados: {e}")


# Função que verifica se a senha é igual ou maior que 5
def senha_len(msg):
    senha = input(msg)
    while len(senha) < 5:
        logger.warning("Senha muito curta, deve ter 5 ou mais caracteres.")
        senha = input("Digite sua senha: ")
    return senha


# Função para verificar se o input é um número
def verifica_numero(num):
    try:
        numero = int(num)
        return numero
    except ValueError:
        logger.warning(f"Entrada inválida, não é um número: {num}")
        return False


# Função para receber a lista e buscar o elemento digitado
def meu_in(lista, buscar):
    for elem in lista:
        if elem == buscar:
            return True
    return False


# Função que força a opção do usuário
def forca_opcao(msg, lista_opcoes):
    msg_erro = ' '.join(lista_opcoes)
    msg_erro = f"Somente essas opções:\n{msg_erro}"
    opcao = input(msg)
    while not meu_in(lista_opcoes, opcao):
        logger.warning(f"Opção inválida: {opcao}. Somente essas opções são permitidas: {lista_opcoes}")
        print(msg_erro)
        opcao = input(msg)
    return opcao
