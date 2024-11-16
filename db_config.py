import sqlite3
from datetime import datetime

conn = sqlite3.connect('greenoffice.db')

cursor = conn.cursor()

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


cursor.execute('''
CREATE TABLE IF NOT EXISTS Arcondicionado (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Id_usuario INTEGER NOT NULL,
    Nome TEXT NOT NULL, -- Nome do arcondicionado
    Data_consumo TEXT NOT NULL,  -- Armazena a data como string no formato YYYY-MM-DD
    Horas_consumo REAL NOT NULL,  -- Horas de uso (número real para incluir frações de horas)
    Consumo_energia_kWh REAL NOT NULL,  -- Consumo em kWh (também número real para precisão)
    Saude_do_ambiente INTEGER NOT NULL,
    Timecreated INTEGER NOT NULL,
    Timemodified INTEGER NOT NULL,
    FOREIGN KEY (Id_usuario) REFERENCES usuarios(Id)
)
''')

conn.commit()
# Fechar conexão
conn.close()
