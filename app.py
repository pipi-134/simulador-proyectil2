# simulador-proyectil2
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título y descripción
st.title("Simulador de Trayectoria de un Proyectil")
st.write("Este simulador calcula la trayectoria de un proyectil en función de la fuerza y el ángulo iniciales.")

# Parámetros de entrada
angle = st.slider("Ángulo de lanzamiento (en grados):", min_value=0, max_value=90, value=45)
initial_velocity = st.slider("Velocidad inicial (m/s):", min_value=0, max_value=100, value=50)

# Botón para asignar la fuerza
if st.button("Asignar Fuerza"):
    st.write(f"Fuerza asignada con una velocidad inicial de {initial_velocity} m/s y un ángulo de {angle} grados.")
    
    # Constantes
    g = 9.81  # gravedad en m/s^2

    # Convertir ángulo a radianes
    angle_rad = np.radians(angle)

    # Calcular componentes de la velocidad inicial
    v0_x = initial_velocity * np.cos(angle_rad)
    v0_y = initial_velocity * np.sin(angle_rad)

    # Calcular el tiempo total de vuelo
    t_flight = (2 * v0_y) / g

    # Generar el tiempo en intervalos para la simulación
    t = np.linspace(0, t_flight, num=500)

    # Calcular las posiciones x e y en función del tiempo
    x = v0_x * t
    y = v0_y * t - 0.5 * g * t**2

    # Gráfico de la trayectoria
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel("Distancia (m)")
    ax.set_ylabel("Altura (m)")
    ax.set_title("Trayectoria del Proyectil")
    st.pyplot(fig)
else:
    st.write("Asigna la fuerza para simular la trayectoria del proyectil.")
