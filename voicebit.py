# ==============================================================================
# Esse Programa foi criado em dedicação ao meu filho Victor Katchor Cruz
# Diego Fernando Cruz – Motor Voice Brazil Beta (2025)
# ------------------------------------------------------------------------------
# This program was created in dedication to my son Victor Katchor Cruz
# Diego Fernando Cruz – Motor Voice Brazil Beta (2025)
# ==============================================================================

import numpy as np
np.complex = complex  # Compatibilidade com librosa // Compatibility with librosa

import librosa          # Para extração de features de áudio // For audio feature extraction
import hashlib          # Para gerar assinaturas únicas // For generating unique hashes
import time             # Para simular tempo real // To simulate real time
from pydub import AudioSegment  # Para carregar áudios mp3/wav // To load mp3/wav audio files
import io
import soundfile as sf

# =================== CONFIGURAÇÃO =======================
# Nome do arquivo de áudio de entrada // Input audio file name
ARQUIVO_AUDIO = "voz_teste.mp3"
# Segundos para cada bloco de análise // Seconds for each analysis block
DURACAO_JANELA = 1.0
# Total de bits desejados por janela // Total bits per window
BITS_POR_BLOCO = 100
# Frequência padrão (Hz) // Default frequency (Hz)
FREQ_PADRAO = 22050

def carregar_audio_completo(path):
    """
    Carrega um áudio (mp3/wav), converte para mono e ajusta frequência.
    // Loads audio file (mp3/wav), converts to mono and resamples.
    Retorna samples normalizados e frequência.
    // Returns normalized samples and frequency.
    """
    audio = AudioSegment.from_file(path)
    audio = audio.set_channels(1).set_frame_rate(FREQ_PADRAO)
    samples = np.array(audio.get_array_of_samples()).astype(np.float32)
    samples /= np.max(np.abs(samples)) + 1e-9
    return samples, FREQ_PADRAO

def extrair_features(y, sr):
    """
    Extrai características acústicas principais do áudio:
    // Extracts main acoustic features from audio:
    pitch, energia (RMS), taxa de cruzamento por zero (ZCR),
    centroide espectral, largura de banda e rolloff espectral.
    // pitch, energy (RMS), zero-crossing rate (ZCR),
    spectral centroid, bandwidth, and spectral rolloff.
    """
    pitch = librosa.yin(y, fmin=50, fmax=500, sr=sr)
    rms = librosa.feature.rms(y=y)[0]
    zcr = librosa.feature.zero_crossing_rate(y=y)[0]
    centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
    bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)[0]
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)[0]

    vetor = np.concatenate([
        [np.mean(pitch), np.std(pitch)],
        [np.mean(rms), np.std(rms)],
        [np.mean(zcr)],
        [np.mean(centroid)],
        [np.mean(bandwidth)],
        [np.mean(rolloff)],
    ])
    return vetor

def gerar_assinatura_binaria(vetor, n_bits):
    """
    Normaliza vetor de features, gera hash (SHA-512) e extrai n_bits.
    // Normalizes feature vector, generates SHA-512 hash, extracts n_bits.
    """
    norm = (vetor - np.min(vetor)) / (np.ptp(vetor) + 1e-8)
    vetor_str = ','.join([f"{x:.6f}" for x in norm])
    hash_digest = hashlib.sha512(vetor_str.encode()).hexdigest()
    binario = bin(int(hash_digest, 16))[2:].zfill(n_bits * 2)[:n_bits]
    return binario

def interpretar_emocao(vetor):
    """
    Estima a emoção predominante no bloco de áudio com regras simples.
    // Estimates predominant emotion in audio block with simple rules.
    """
    pitch_m, pitch_std = vetor[0], vetor[1]
    rms_m = vetor[2]
    zcr = vetor[4]

    # As faixas abaixo são heurísticas simples.
    # The ranges below are simple heuristics.
    if pitch_m > 250 and rms_m > 0.04:
        return "Raiva / Grito | Anger / Scream"
    elif pitch_std > 20:
        return "Ansiedade / Agitação | Anxiety / Agitation"
    elif pitch_m < 120 and rms_m < 0.015:
        return "Tristeza / Apatia | Sadness / Apathy"
    elif zcr > 0.1:
        return "Riso / Excitação | Laughter / Excitement"
    else:
        return "Neutro / Calmo | Neutral / Calm"

def analisar_tempo_real(audio, sr, janela_s=1.0, bits=20):
    """
    Percorre o áudio em blocos, exibe a emoção e a assinatura de cada bloco.
    // Loops through audio in blocks, prints emotion and binary signature for each block.
    """
    total_amostras = len(audio)
    tamanho_janela = int(sr * janela_s)
    total_blocos = total_amostras // tamanho_janela

    print(f"\n📊 Análise em tempo real (total de {total_blocos} blocos de {janela_s:.1f}s cada)")
    print(f"📊 Real-time analysis (total of {total_blocos} blocks of {janela_s:.1f}s each)\n")
    for i in range(total_blocos):
        inicio = i * tamanho_janela
        fim = inicio + tamanho_janela
        bloco = audio[inicio:fim]
        if len(bloco) < tamanho_janela:
            break

        features = extrair_features(bloco, sr)
        assinatura = gerar_assinatura_binaria(features, bits)
        emocao = interpretar_emocao(features)

        print(f"🕒 {i+1*janela_s:5.1f}s: {emocao:35} | Assinatura Binária / Binary Signature: {assinatura}")
        time.sleep(0.2)  # Simula tempo real // Simulates real time

# =================== EXECUÇÃO PRINCIPAL =======================
# =================== MAIN EXECUTION ===========================
if __name__ == "__main__":
    print("🎙️ VoiceBit – Diego F Cruz | Te amo, Victor K Cruz 💙")
    print("🎙️ VoiceBit – Diego F Cruz | I love you, Victor K Cruz 💙")
    audio, sr = carregar_audio_completo(ARQUIVO_AUDIO)
    analisar_tempo_real(audio, sr, DURACAO_JANELA, BITS_POR_BLOCO)
