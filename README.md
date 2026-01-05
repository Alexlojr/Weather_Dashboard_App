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

### OpenWeather API Configuration
in .env
```
API_KEY=your_api_key_here
```
#### Get your free API key at: https://openweathermap.org/api_keys, creating a account is necessary

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

![img.png](src/resources/img.png)