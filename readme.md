# GreenOffice - Plataforma Inteligente de Conforto e Sustentabilidade

## Descrição do Projeto
A **GreenOfiice** está disposta a ajudar a saúde da sua empresa por um bem maior, trazendo mais conforto para seus clientes através da tecnologia e sustentabilidade. Utilizando sensores IoT e uma interface intuitiva, o sistema monitora e controla o uso de ar-condicionado com base em presença de pessoas e condições ambientais, reduzindo custos e promovendo sustentabilidade.

---

## Funcionalidades
- **Cadastro e Login**: 
  - Usuários podem se cadastrar com nome, e-mail e senha.
  - Sistema de login com validação de credenciais.
  
- **Gestão de Ar-Condicionado**:
  - Cadastro de novos ar-condicionados.
  - Consulta de informações detalhadas sobre ar-condicionados cadastrados.
  - Remoção de ar-condicionados.

- **Página Home**:
  - Apresentação da GreenOffice e seus objetivos.
  - Informações sobre a equipe de desenvolvimento.

- **Página Contato**:
  - Envio de mensagens diretamente à equipe do GreenOffice.
  - Informações de contato para suporte e dúvidas.

---

## Pré-requisitos
Para executar o projeto, certifique-se de ter o seguinte instalado:
- Python 3.8
- Módulos necessários listados em `service/serviceUser.py`:
  - **logging**
  - **regex** ou outros pacotes específicos de validação e manipulação.

---

## Como Executar o Projeto
1. **Clone o repositório**:
   ```bash
   git clone https://github.com/EduDalla/python-GreenOffice.git
   cd python-GreenOffice
   ```

2. **Instale as dependências**:
   Certifique-se de instalar quaisquer módulos necessários executando:
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o banco de dados**:
   No diretório raiz, execute o comando:
   ```bash
   python db_config.py
   ```

4. **Execute o programa**:
   No diretório raiz, execute o comando:
   ```bash
   python main.py
   ```

---

## Estrutura do Projeto
```plaintext
.
├── main.py                # Arquivo principal para execução
├── service/
│   └── serviceUser.py     # Lógica de negócio e funções auxiliares
├── db_config.py           # Arquivo para execução do banco de dados
├── README.md              # Documentação do projeto
└── requirements.txt       # Dependências do projeto
```

---

## Fluxo de Navegação
1. **Página Inicial**:
   - Escolha entre cadastro ou login.
2. **Após o login**:
   - Acesse:
     - Página "Home" para informações gerais.
     - Página "Ar-condicionados" para gerenciar dispositivos.
     - Página "Contato" para enviar mensagens.
3. **Encerrar**:
   - Navegue até sair ou feche a aplicação.

---

## Equipe de Desenvolvimento
- **Eduardo Dallabella Lima**: Back-end
- **Helôisa Real**: IoT e Cálculo
- **Pedro Gustavo Schmitz**: Front-end

---

## Licença
Este projeto é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.

---

## Contribuições
Contribuições são bem-vindas! Para colaborar:
1. Faça um fork do repositório.
2. Crie uma nova branch:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça commit das alterações:
   ```bash
   git commit -m "Minha nova feature"
   ```
4. Envie suas alterações:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request no GitHub.

