import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Parámetros
fs = 10000  # Frecuencia de muestreo (Hz)
t = np.arange(0, 1, 1/fs)  # Tiempo (1 segundo)

fm = 5  # Frecuencia del mensaje (Hz)
mensaje = np.sin(2 * np.pi * fm * t)



#Grafica de Señal de entrada
plt.figure(figsize=(10,4))
plt.plot(t, mensaje)
plt.title("Señal de Mensaje (Baja Frecuencia)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()
plt.show()



#Crear señal portadora y modular señal
fc = 100  # Frecuencia portadora (Hz)
portadora = np.cos(2 * np.pi * fc * t)

# Modulación AM
senal_modulada = mensaje * portadora



#Graficar señal modulada (tiempo)
plt.figure(figsize=(10,4))
plt.plot(t, senal_modulada)
plt.title("Señal Modulada (AM) - Dominio del Tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

#Análisis en frecuencia (FFT)
N = len(senal_modulada)
yf = fft(senal_modulada)
xf = fftfreq(N, 1/fs)

plt.figure(figsize=(10,4))
plt.plot(xf[:N//2], np.abs(yf[:N//2]))
plt.title("Espectro de Frecuencia (Señal Modulada)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.grid()
plt.show()



#Introducir ruido (AWGN)
ruido = np.random.normal(0, 0.5, len(senal_modulada))
senal_ruidosa = senal_modulada + ruido

plt.figure(figsize=(10,4))
plt.plot(t, senal_ruidosa)
plt.title("Señal Modulada con Ruido")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()
plt.show()



#Análisis de distorsión y atenuación
#Atenuación
factor_atenuacion = 0.5  
senal_atenuada = senal_modulada * factor_atenuacion

plt.figure(figsize=(10,4))
plt.plot(t, senal_atenuada)
plt.title("Señal Atenuada")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

#Comparación (Original vs Ruido vs Atenuada)
plt.figure(figsize=(10,5))
plt.plot(t, senal_modulada, label="Original")
plt.plot(t, senal_ruidosa, alpha=0.6, label="Con ruido")
plt.plot(t, senal_atenuada, linestyle="--", label="Atenuada")
plt.legend()
plt.title("Comparación de Señales")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()
plt.show()