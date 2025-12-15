# 🌱 GrowLab – Estufa Inteligente com IoT e IA  
## 📘 Milestone 1 – Investigação e Ideação  
📅 **Data de entrega:** 11 de novembro de 2025  

---

## Identificação

| Elemento | Número | Curso | UC | Ano/Semestre |
|-----------|---------|--------|---------------|---------------|
| **Bernardo Ferreira** | 20231588 | Licenciatura em Engenharia Informática | Projeto Integrador | 3.º Ano / 1.º Semestre |
| **Tiago Chiquilho** | 20231587 | Licenciatura em Engenharia Informática | Projeto Integrador | 3.º Ano / 1.º Semestre |

**Universidade:** IADE – Universidade Europeia  
**Faculdade:** Faculdade de Design, Tecnologia e Comunicação  
**Projeto:** *GrowLab – Estufa Inteligente com IoT e IA*  
**Repositório GitHub:** ([https://github.com/teu-utilizador/GrowLab](https://github.com/BernardoFerreira2001/Documentacao))

**Palavras-chave:** IoT, Sistemas Distribuídos, Inteligência Artificial, Estufa, Automação, FastAPI, ESP32

---

## Descrição e Motivação do Projeto

O projeto **GrowLab** tem como objetivo desenvolver uma **estufa inteligente** capaz de **monitorizar e ajustar automaticamente** as condições internas — **temperatura e humidade** — de forma a otimizar o crescimento de plantas.

Com o uso de sensores e atuadores controlados por um **ESP32**, o sistema reage a alterações do ambiente:
- Ativa uma **ventoinha** quando a temperatura está elevada;
- Liga um **nebulizador (mist)** quando a humidade está baixa;
- Controla um **LED** que simula o ciclo de luz diária, acendendo e apagando em horários específicos.

O sistema envia as medições para um **servidor central** através de uma **API REST desenvolvida em FastAPI**, armazenando os dados numa **base de dados MySQL**.  
Mais tarde, será integrado um módulo de **Inteligência Artificial** que permitirá prever variações ambientais e otimizar o funcionamento da estufa.

### Objetivos principais
- Automatizar a gestão de temperatura e humidade.  
- Aplicar os princípios de **Sistemas Distribuídos** na comunicação entre dispositivos.  
- Criar uma base sólida para a integração futura de **IA**.  
- Desenvolver um sistema **modular, escalável e de baixo custo**.

---

## Público-Alvo

O público-alvo inclui:
- Estudantes e docentes de engenharia, como projeto académico de integração.  
- Pequenos produtores agrícolas que desejem **automatizar estufas domésticas**.  
- Entusiastas de IoT e tecnologia aplicada à agricultura inteligente.

---

## Guiões de Teste (versão preliminar)

### Guião 1 – Monitorização básica
1. Ligar o sistema (ESP32 + sensores + atuadores).  
2. O sensor DHT22 recolhe temperatura e humidade.  
3. O ESP32 envia os dados via Wi-Fi para a API REST.  
4. A API grava as medições na base de dados MySQL.  
5. O dashboard apresenta os valores em tempo real.  

**Resultado esperado:** Leituras registadas e apresentadas corretamente no dashboard.

---

### Guião 2 – Ação automática dos atuadores
1. Simular temperatura > 28 °C.  
2. O ESP32 identifica o valor acima do limite e liga a ventoinha.  
3. Quando a temperatura baixa < 25 °C, a ventoinha desliga.  
4. Repetir o teste com humidade < 40 % → nebulizador ativa.  

**Resultado esperado:** Atuadores reagem automaticamente às condições ambientais.

---

## Enquadramento nas Unidades Curriculares

| UC | Contributo no Projeto |
|----|------------------------|
| **Sistemas Distribuídos (SD)** | Desenvolvimento da API REST (FastAPI), comunicação cliente-servidor, integração com base de dados e gestão de dados. |
| **Computação Física e IoT (CF/IoT)** | Montagem e programação do ESP32, ligação dos sensores (DHT22) e atuadores (ventoinha, mist e LED). |
| **Engenharia de Software (ES)** | Definição de requisitos, planeamento, documentação e gestão de versões no GitHub. |
| **Inteligência Artificial (IA)** | (Fase posterior) criação de modelo preditivo para previsão de temperatura/humidade e controlo inteligente. |

---

## Requisitos Técnicos e Tecnologias

| Categoria | Tecnologia / Ferramenta | Finalidade |
|------------|--------------------------|-------------|
| Microcontrolador | **ESP32 DevKit v1** | Recolha de dados e controlo de atuadores |
| Sensor | **DHT22** | Medição de temperatura e humidade |
| Atuadores | **Ventoinha**, **Nebulizador (mist)**, **LED** | Controlo ambiental e simulação de luz |
| Backend | **Python + FastAPI** | API REST (Sistemas Distribuídos) |
| Base de Dados | **MySQL** | Armazenamento de medições |
| Dashboard | **HTML + Chart.js** | Visualização de dados em tempo real |
| IDE / Ferramentas | **Arduino IDE**, **VS Code**, **GitHub**, **Postman** | Desenvolvimento, teste e versionamento |

---

## Arquitetura da Solução (versão preliminar)

[ESP32 + Sensores/Atuadores]
│ (HTTP/JSON)
▼
[API REST – FastAPI]
│
▼
[Base de Dados MySQL]
│
├────────────┐
│ │
[Dashboard] [Módulo IA]


### Descrição resumida
- O **ESP32** recolhe dados de temperatura e humidade.  
- A **API FastAPI** recebe e processa os dados.  
- A **base de dados MySQL** armazena as medições e o estado dos atuadores.  
- O **dashboard** consulta os dados e apresenta-os em tempo real.  
- A **IA** (futura) irá prever as condições e propor ajustes automáticos.

---

## Planeamento e Calendarização

### Tabela Resumida

| Fase | Período | Objetivos | Entregáveis | Responsáveis |
|------|----------|------------|--------------|---------------|
| **1. Ideação e Planeamento (M1)** | até 11 nov | Conceito, arquitetura e plano | Relatório SD + README + slides | Bernardo & Tiago |
| **2. Desenvolvimento Base (M2)** | nov–dez | API + BD + Firmware ESP32 | Protótipo funcional | Bernardo & Tiago |
| **3. IA e Dashboard (M3)** | jan–fev | Integração IA + visualização | Relatório final + vídeo | Bernardo & Tiago |
| **4. Testes e Apresentação** | fev | Validação e entrega final | Poster + apresentação | Bernardo & Tiago |

---

### Cronograma (formato Gantt simplificado)

Nov |Ideação & Planeamento (M1)
Dez |Desenvolvimento Base (M2)
Jan |IA e Dashboard (M3)
Fev |Testes e Apresentação Final

---

## Conclusão

O **GrowLab** é um projeto que combina **IoT, Sistemas Distribuídos e Inteligência Artificial** para criar uma estufa autónoma e eficiente.  
Através do controlo automático de temperatura, humidade e luz, demonstra a aplicação prática dos conceitos estudados nas diversas Unidades Curriculares.  

Esta **primeira milestone** define a base técnica e conceptual do sistema, garantindo um planeamento sólido e uma arquitetura distribuída pronta para implementação nas próximas fases.

---

## Estrutura de Repositório (parcial)

GrowLab/
├─ Documentacao/
│ ├─ 1aEntrega/
│ │ ├─ README.md ← (este ficheiro)
│ │ ├─ SD.md
│ │ ├─ slides_SD.txt
│ └─ 2aEntrega/
│ └─ 3aEntrega/
├─ src/
│ ├─ api/
│ ├─ firmware/
│ └─ db/
└─ modelos_fisicos/
