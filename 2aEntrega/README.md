🌱 GrowLab – Estufa Inteligente com IoT e IA
📘 Milestone 1 – Investigação e Ideação
📅 Data de entrega: 11 de novembro de 2025

Identificação
Elemento	Número	Curso	UC	Ano/Semestre
Bernardo Ferreira	20231588	Licenciatura em Engenharia Informática	Projeto Integrador	3.º Ano / 1.º Semestre
Tiago Chiquilho	20231587	Licenciatura em Engenharia Informática	Projeto Integrador	3.º Ano / 1.º Semestre
Universidade: IADE – Universidade Europeia
Faculdade: Faculdade de Design, Tecnologia e Comunicação
Projeto: GrowLab – Estufa Inteligente com IoT e IA
Repositório GitHub: (https://github.com/teu-utilizador/GrowLab)

Palavras-chave: IoT, Sistemas Distribuídos, Inteligência Artificial, Estufa, Automação, FastAPI, ESP32

Descrição e Motivação do Projeto
O projeto GrowLab tem como objetivo desenvolver uma estufa inteligente capaz de monitorizar e ajustar automaticamente as condições internas — temperatura e humidade — de forma a otimizar o crescimento de plantas.

Com o uso de sensores e atuadores controlados por um ESP32, o sistema reage a alterações do ambiente:

Ativa uma ventoinha quando a temperatura está elevada;
Liga um nebulizador (mist) quando a humidade está baixa;
Controla um LED que simula o ciclo de luz diária, acendendo e apagando em horários específicos.
O sistema envia as medições para um servidor central através de uma API REST desenvolvida em FastAPI, armazenando os dados numa base de dados MySQL.
Mais tarde, será integrado um módulo de Inteligência Artificial que permitirá prever variações ambientais e otimizar o funcionamento da estufa.

Objetivos principais
Automatizar a gestão de temperatura e humidade.
Aplicar os princípios de Sistemas Distribuídos na comunicação entre dispositivos.
Criar uma base sólida para a integração futura de IA.
Desenvolver um sistema modular, escalável e de baixo custo.
Público-Alvo
O público-alvo inclui:

Estudantes e docentes de engenharia, como projeto académico de integração.
Pequenos produtores agrícolas que desejem automatizar estufas domésticas.
Entusiastas de IoT e tecnologia aplicada à agricultura inteligente.
Guiões de Teste (versão preliminar)
Guião 1 – Monitorização básica
Ligar o sistema (ESP32 + sensores + atuadores).
O sensor DHT22 recolhe temperatura e humidade.
O ESP32 envia os dados via Wi-Fi para a API REST.
A API grava as medições na base de dados MySQL.
O dashboard apresenta os valores em tempo real.
Resultado esperado: Leituras registadas e apresentadas corretamente no dashboard.

Guião 2 – Ação automática dos atuadores
Simular temperatura > 28 °C.
O ESP32 identifica o valor acima do limite e liga a ventoinha.
Quando a temperatura baixa < 25 °C, a ventoinha desliga.
Repetir o teste com humidade < 40 % → nebulizador ativa.
Resultado esperado: Atuadores reagem automaticamente às condições ambientais.

Enquadramento nas Unidades Curriculares
UC	Contributo no Projeto
Sistemas Distribuídos (SD)	Desenvolvimento da API REST (FastAPI), comunicação cliente-servidor, integração com base de dados e gestão de dados.
Computação Física e IoT (CF/IoT)	Montagem e programação do ESP32, ligação dos sensores (DHT22) e atuadores (ventoinha, mist e LED).
Engenharia de Software (ES)	Definição de requisitos, planeamento, documentação e gestão de versões no GitHub.
Inteligência Artificial (IA)	(Fase posterior) criação de modelo preditivo para previsão de temperatura/humidade e controlo inteligente.
Requisitos Técnicos e Tecnologias
Categoria	Tecnologia / Ferramenta	Finalidade
Microcontrolador	ESP32 DevKit v1	Recolha de dados e controlo de atuadores
Sensor	DHT22	Medição de temperatura e humidade
Atuadores	Ventoinha, Nebulizador (mist), LED	Controlo ambiental e simulação de luz
Backend	Python + FastAPI	API REST (Sistemas Distribuídos)
Base de Dados	MySQL	Armazenamento de medições
Dashboard	HTML + Chart.js	Visualização de dados em tempo real
IDE / Ferramentas	Arduino IDE, VS Code, GitHub, Postman	Desenvolvimento, teste e versionamento
Arquitetura da Solução (versão preliminar)
[ESP32 + Sensores/Atuadores] │ (HTTP/JSON) ▼ [API REST – FastAPI] │ ▼ [Base de Dados MySQL] │ ├────────────┐ │ │ [Dashboard] [Módulo IA]

Descrição resumida
O ESP32 recolhe dados de temperatura e humidade.
A API FastAPI recebe e processa os dados.
A base de dados MySQL armazena as medições e o estado dos atuadores.
O dashboard consulta os dados e apresenta-os em tempo real.
A IA (futura) irá prever as condições e propor ajustes automáticos.
Planeamento e Calendarização
Tabela Resumida
Fase	Período	Objetivos	Entregáveis	Responsáveis
1. Ideação e Planeamento (M1)	até 11 nov	Conceito, arquitetura e plano	Relatório SD + README + slides	Bernardo & Tiago
2. Desenvolvimento Base (M2)	nov–dez	API + BD + Firmware ESP32	Protótipo funcional	Bernardo & Tiago
3. IA e Dashboard (M3)	jan–fev	Integração IA + visualização	Relatório final + vídeo	Bernardo & Tiago
4. Testes e Apresentação	fev	Validação e entrega final	Poster + apresentação	Bernardo & Tiago
Cronograma (formato Gantt simplificado)
Nov |Ideação & Planeamento (M1) Dez |Desenvolvimento Base (M2) Jan |IA e Dashboard (M3) Fev |Testes e Apresentação Final

Conclusão
O GrowLab é um projeto que combina IoT, Sistemas Distribuídos e Inteligência Artificial para criar uma estufa autónoma e eficiente.
Através do controlo automático de temperatura, humidade e luz, demonstra a aplicação prática dos conceitos estudados nas diversas Unidades Curriculares.

Esta primeira milestone define a base técnica e conceptual do sistema, garantindo um planeamento sólido e uma arquitetura distribuída pronta para implementação nas próximas fases.

Estrutura de Repositório (parcial)
GrowLab/ ├─ Documentacao/ │ ├─ 1aEntrega/ │ │ ├─ README.md ← (este ficheiro) │ │ ├─ SD.md │ │ ├─ slides_SD.txt │ └─ 2aEntrega/ │ └─ 3aEntrega/ ├─ src/ │ ├─ api/ │ ├─ firmware/ │ └─ db/ └─ modelos_fisicos/

📘 Milestone 2 – Desenvolvimento e Prototipagem

📅 Data de entrega: 16 de dezembro de 2025
📚 Unidade Curricular: Sistemas Distribuídos

Esta milestone dá continuidade ao trabalho iniciado na Milestone 1, mantendo a visão, objetivos e arquitetura previamente definidos, e focando-se na implementação de um protótipo funcional que integra hardware e software.

1. Descrição da Funcionalidade do Protótipo

Nesta segunda fase do projeto GrowLab, foi desenvolvido um protótipo funcional que implementa, de forma prática, os conceitos definidos na Milestone 1.

O protótipo é capaz de:

Medir temperatura e humidade em tempo real através do sensor DHT22;

Enviar os dados recolhidos para um servidor central através de uma API REST;

Armazenar automaticamente as medições numa base de dados MySQL;

Controlar atuadores físicos:

Ventoinha (controlo automático da temperatura);

LED (simulação do ciclo de luz);

Nebulizador/mist (preparado para controlo de humidade);

Permitir controlo manual e monitorização remota através da plataforma Blynk.

Este protótipo valida pelo menos um requisito funcional completo envolvendo hardware + software + comunicação distribuída, conforme exigido para esta milestone.

2. Descrição da Solução e Arquitetura Implementada
Arquitetura Implementada

A arquitetura definida na Milestone 1 foi implementada e validada, seguindo um modelo distribuído cliente-servidor.

[ESP32 + Sensores/Atuadores]
          |
      HTTP / JSON
          |
[API REST - FastAPI]
          |
     [Base de Dados MySQL]
          |
   [Dashboard / Blynk]

Componentes Implementados
ESP32 (Cliente IoT)

Leitura periódica do sensor DHT22;

Lógica de controlo automático baseada em limites definidos;

Envio de dados para a API REST;

Receção de comandos manuais via Blynk;

Funcionamento híbrido Automático / Manual, com prioridade ao utilizador.

API REST (FastAPI)

Endpoints REST para:

Receção de leituras dos sensores;

Registo do estado dos atuadores;

Comunicação via JSON;

Integração com base de dados MySQL usando ORM;

Preparada para futura expansão (dashboard web e IA).

Base de Dados MySQL

Armazena:

Leituras de sensores;

Estados dos atuadores;

Configurações da estufa;

Estrutura relacional alinhada com a arquitetura definida na Milestone 1.

3. Diagramas de Circuitos Necessários
Componentes Físicos Utilizados

ESP32 DevKit v1

Sensor DHT22

Módulo de relés (2 canais)

Ventoinha 5V

LED

Fonte de alimentação MB102

Protoboard e cabos jumper

Ligações Principais

DHT22 → GPIO 4 (ESP32)

Relé Ventoinha → GPIO 5

Relé Mist → GPIO 23

LED → GPIO 21

Alimentação dos relés via módulo MB102


4. Descrição das Atividades Realizadas

Durante a Milestone 2 foram realizadas as seguintes atividades:

Desenvolvimento de Software

Implementação da API REST em FastAPI;

Definição dos modelos ORM de acordo com a base de dados;

Implementação dos endpoints de sensores e atuadores;

Testes locais da API com dados reais.

Firmware ESP32

Programação do ESP32 em Arduino/C++;

Implementação da leitura do DHT22;

Controlo automático da ventoinha e LED;

Integração com a API REST via HTTP;

Integração com o Blynk para controlo remoto;

Otimização do envio de dados para evitar sobrecarga da base de dados.

Integração e Testes

Testes de comunicação ESP32 ↔ API;

Validação da persistência dos dados na base de dados;

Testes de controlo automático e manual;

Validação do protótipo como sistema distribuído funcional.

5. Código Fonte Desenvolvido

Todo o código desenvolvido está organizado e disponível no repositório GitHub do projeto:

GrowLab/
 ├─ src/
 │   ├─ api/          # FastAPI + ORM + MySQL
 │   ├─ firmware/     # Código ESP32
 │   └─ db/           # Scripts SQL
 ├─ Documentacao/
 │   ├─ 1aEntrega/
 │   ├─ 2aEntrega/
 └─ modelos_fisicos/

6. Modelos Físicos Envolvidos no Projeto

Na pasta /modelos_fisicos encontram-se:

Fotografias do protótipo montado;

Diagrama de ligações;

Lista de componentes utilizados;

Descrição da montagem física.

Conclusão da Milestone 2

Com a conclusão da Milestone 2, o projeto GrowLab evoluiu de uma proposta conceptual para um protótipo funcional, demonstrando na prática:

Comunicação distribuída entre dispositivos;

Integração de hardware e software;

Persistência de dados;

Controlo automático e remoto.

Esta milestone estabelece uma base sólida para a próxima fase do projeto, onde serão integrados o dashboard web completo e o módulo de Inteligência Artificial, conforme planeado inicialmente.
