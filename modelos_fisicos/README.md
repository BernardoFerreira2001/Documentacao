# 📦 Modelos Físicos – GrowLab

Esta pasta contém toda a documentação relacionada com a **montagem física do protótipo** da estufa inteligente GrowLab, desenvolvida no âmbito da Milestone 2.

---

## 🔌 Componentes Utilizados

- ESP32 DevKit v1  
- Sensor de temperatura e humidade DHT22  
- Módulo de relés (2 canais)  
- Ventoinha 5V  
- LED  
- Fonte de alimentação MB102  
- Protoboard  
- Cabos jumper (macho-macho e macho-fêmea)

---

## 🔗 Ligações Elétricas

### Sensor DHT22
- **VCC** → 3.3V (ESP32)
- **DATA** → GPIO 4
- **GND** → GND

### Atuadores
- **Relé da Ventoinha** → GPIO 5
- **Relé do Nebulizador (Mist)** → GPIO 23
- **LED** → GPIO 21 (com resistência apropriada)

### Alimentação
- Os módulos de relé são alimentados através da fonte MB102
- O ESP32 é alimentado via USB

---

## 🧩 Diagrama de Ligações

O diagrama elétrico do sistema encontra-se representado nos seguintes ficheiros:

- `diagrama_ligacoes.png`
- `esquema_circuito.pdf`

Estes diagramas ilustram a ligação entre o ESP32, o sensor DHT22, os relés e os atuadores.

---

## 📸 Fotografias do Protótipo

Nesta pasta encontram-se fotografias reais do protótipo físico montado, incluindo:

- Visão geral do sistema
- Ligações na protoboard
- Sensor DHT22 em funcionamento
- Módulo de relés ligado aos atuadores

---

## 🛠️ Descrição da Montagem

O protótipo foi montado numa protoboard para facilitar testes e alterações.  
O ESP32 atua como controlador central, recolhendo dados do sensor DHT22 e acionando os atuadores através do módulo de relés.

Esta abordagem permite:
- Facilidade de manutenção
- Expansão futura do sistema
- Testes rápidos de funcionalidades

---

## 📌 Observações

O sistema físico foi desenvolvido com foco na **prototipagem funcional**, garantindo a integração entre hardware e software conforme os requisitos definidos para a Milestone 2.
