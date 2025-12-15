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

https://cdn.discordapp.com/attachments/775789461388656651/1450156639138353285/image.png?ex=6941831d&is=6940319d&hm=4b23a592f67acf6cea2c81e46b49a433b20f6754c261e4b5136ec35e500b1453&
https://cdn.discordapp.com/attachments/775789461388656651/1450156581583982734/image.png?ex=6941830f&is=6940318f&hm=7bbe1eb2097ba2fa89543fb3f935f15e60200c7d19465b3baec85ed6af9873c0&


---

## 📸 Fotografias do Protótipo

Nesta pasta encontram-se fotografias reais do protótipo físico montado, incluindo:

blob:https://web.whatsapp.com/356e20d4-99eb-421d-868d-49361eb0b0fb


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
