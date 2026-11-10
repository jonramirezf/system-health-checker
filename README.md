# System Health Checker 🖥️

Script de monitoreo de recursos del sistema desarrollado en Python, orientado al aprendizaje de automatización, Linux y DevOps.

## Funcionalidades

- Monitoreo real del uso de CPU y memoria RAM.
- Obtención de métricas mediante la biblioteca `psutil`.
- Verificación de umbrales de utilización.
- Alertas según el estado de los recursos.
- Visualización de resultados en la terminal.

## Tecnologías

- Python 3
- psutil
- Linux (Ubuntu)
- Git y GitHub

## Instalación

Crear y activar un entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

## Ejecución

```bash
python system_health.py
```

### Ejemplo de salida

```text
CPU: 21.0 % Normal
RAM: 77.3 % Memoria normal
```

Los porcentajes corresponden al consumo real del computador y pueden variar en cada ejecución.

## Umbrales actuales

- CPU ≥ 90 %: Alerta.
- RAM ≥ 80 %: Alerta.

## Próximas mejoras

- Incorporar monitoreo del disco.
- Generar reportes de ejecución.
- Agregar pruebas automáticas.
- Integrar GitHub Actions para validar el código.

## Objetivo

Desarrollar habilidades prácticas de programación y automatización con Python, aplicadas a la administración y observabilidad de sistemas.
