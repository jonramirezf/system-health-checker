import psutil

# Función de control de CPU
def verificar_cpu(cpu):
    if cpu >= 90:
        return "Alerta"
    else:
        return "Normal"


# Función de control de RAM
def controlar_ram(ram):
    if ram >= 80:
        return "Alerta!"
    else:
        return "Memoria normal"


# Obtener datos reales del computador
cpu_actual = psutil.cpu_percent(interval=1)
ram_actual = psutil.virtual_memory().percent

# Ejecutar nuestras funciones
verificar = verificar_cpu(cpu_actual)
verificar_ram = controlar_ram(ram_actual)

# Mostrar resultados
print("CPU:", cpu_actual, "%", verificar)
print("RAM:", ram_actual, "%", verificar_ram)
                
