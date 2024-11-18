import sqlite3
from datetime import datetime
import logging

# Configuração do logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_connection():
    return sqlite3.connect('greenoffice.db')


def create_tables():
    global conn
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Criação de tabelas
        logging.info("Criando tabela 'usuarios'...")
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                email TEXT,
                password TEXT NOT NULL,
                timecreated INTEGER NOT NULL,
                timemodified INTEGER NOT NULL
            )
            ''')

        logging.info("Criando tabela 'Arcondicionado'...")
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Arcondicionado (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Id_usuario INTEGER NOT NULL,
                Nome TEXT NOT NULL,
                Data_consumo TEXT NOT NULL,
                Horas_consumo REAL NOT NULL,
                Consumo_energia_kWh REAL NOT NULL,
                Saude_do_ambiente INTEGER NOT NULL,
                Timecreated INTEGER NOT NULL,
                Timemodified INTEGER NOT NULL,
                FOREIGN KEY (Id_usuario) REFERENCES usuarios(Id)
            )
            ''')

        logging.info("Criando tabela 'Mensagem'...")
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Mensagem (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Id_usuario INTEGER NOT NULL,
                Mensagem TEXT NOT NULL,
                Timecreated INTEGER NOT NULL,
                Timemodified INTEGER NOT NULL,
                FOREIGN KEY (Id_usuario) REFERENCES usuarios(Id)
            )
            ''')

        conn.commit()
        logging.info("Tabelas criadas com sucesso!")
    except sqlite3.Error as e:
        logging.error(f"Erro ao criar tabelas: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    create_tables()
