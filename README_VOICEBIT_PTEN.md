# 🎙️ VoiceBit – Diego F Cruz

> **Te Amo, Victor 💙 – Tudo que faço é pelo meu filho autista.**
> **I Love You, Victor 💙 – Everything I do is for my autistic son.**

VoiceBit é um motor de análise vocal leve, auditável e poderoso, criado com amor por **Diego Fernando Cruz**.
VoiceBit is a lightweight, auditable, and powerful voice analysis engine, created with love by **Diego Fernando Cruz**.

Este sistema transforma voz em uma **assinatura binária única**, detectando **emoções humanas em tempo real** com altíssima eficiência – sem precisar de GPU ou nuvem.
This system turns voice into a **unique binary signature**, detecting **human emotions in real time** with high efficiency – no GPU or cloud required.

---

## ⚙️ O que o sistema faz | What this system does

- 🎧 Processa voz de arquivos `.mp3` ou `.wav`
  Processes `.mp3` or `.wav` voice files
- 🧠 Extrai pitch, energia, agitação, espectro
  Extracts pitch, energy, agitation, spectrum
- 🔐 Gera uma **assinatura binária única da voz**
  Generates a **unique binary signature of the voice**
- 🧠 Interpreta emoções: alegria, tristeza, ansiedade, raiva
  Interprets emotions: joy, sadness, anxiety, anger
- ⚡ Roda localmente em tempo real (até em computadores simples)
  Runs locally in real time (even on simple computers)

---

## 💡 Como funciona | How it works

O sistema divide o áudio em blocos de 1 segundo e extrai:
The system splits the audio into 1-second blocks and extracts:

- `pitch` (frequência fundamental da voz) // fundamental frequency of the voice
- `rms` (nível de energia) // energy level
- `zcr` (zero-crossing rate – agitação vocal) // vocal agitation
- `centroid`, `bandwidth`, `rolloff`

Esses vetores são normalizados e **transformados em um hash SHA-512**, gerando uma **assinatura acústica binária** que identifica padrões emocionais.
These vectors are normalized and **turned into a SHA-512 hash**, generating a **binary acoustic signature** that identifies emotional patterns.

---

## 🛠️ Como usar | How to use

1. Coloque seu áudio como `voz_teste.mp3`
   Place your audio as `voz_teste.mp3`
2. Rode o script com:
   Run the script with:

```bash
python voicebit.py
```

---

## 📦 Requisitos | Requirements

```bash
pip install numpy librosa pydub soundfile
```

---

## 📌 Exemplo de saída | Example output

```
📊 Análise em tempo real (total de 12 blocos de 1.0s cada)
📊 Real-time analysis (total of 12 blocks of 1.0s each)

🕒  1.0s: Riso / Excitação | Laughter / Excitement
🕒  2.0s: Tristeza / Apatia | Sadness / Apathy
```

---

## 🔒 Por que é especial? | Why is it special?

- ✅ 100% Offline
- ✅ Não precisa de GPU // No GPU required
- ✅ Auditável // Auditable
- ✅ Leve, rápido e explicável // Lightweight, fast, and explainable
- ✅ Feito com ética e propósito // Made with ethics and purpose

---

## ✨ Autor | Author

**Diego Fernando Cruz**
Macatuba – São Paulo – Brasil 🇧🇷
🧠 Criador do VoiceBit // Creator of VoiceBit
💙 Pai do Victor, minha razão de viver // Father of Victor, my reason to live

---

## 📜 Licença | License

MIT – Uso livre com crédito ao autor.
MIT – Free use with credit to the author.
## 🔒 Registro de Autoria – VoiceBit

**Arquivo:** `voicebit.py`  
**Hash SHA256:** `1F2D0F3C7E47E1A64A6FD935802185EB0B9202B153F25B8C8A6AE7C292DBA7F5`  
**Autor:** Diego Fernando Cruz  
**Data:** 25/07/2025  
**Projeto dedicado a:** Victor Katchor Cruz  
**Descrição:** Motor de análise de voz binária com detecção emocional em tempo real.

> Este hash é a identidade digital da obra e pode ser usado como prova de autoria e anterioridade em qualquer disputa jurídica.
