# Weather Dashboard

Dashboard de clima em tempo real com PySide6.

## Setup
```bash
# Instalar dependências
pip install -r requirements.txt

# Configurar API key
cp .env.example .env
# Adicione sua chave do OpenWeatherMap

# Rodar
python src/main.py
```

## Stack

- Python 3.10+
- PySide6 6.10
- OpenWeather API

## Estrutura
```
src/
├── main.py           # Entry point
├── ui/               # Interface
│   ├── main_window.py
│   ├── widgets/      # Componentes
│   └── styles.qss    # Estilos
├── services/         # Lógica de negócio
└── utils/            # Utilidades
```

## Preview

_Em desenvolvimento..._