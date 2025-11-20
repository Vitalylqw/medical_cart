# Telegram Audio Transcriber (Windows 10, monolith)

Telegram‑бот для транскрибации аудио/voice. Основной провайдер — локальный `faster-whisper`
(GPU CUDA), резерв — OpenAI (Whisper API / gpt‑4o‑mini‑transcribe).

## Быстрый старт (Windows 10, polling)

1) Установите Python 3.10+ и Git.  
2) Клонируйте репозиторий и создайте виртуальное окружение:

```
python -m venv venv
```

3) Активируйте окружение:

```
venv\Scripts\activate.bat
```

4) Установите зависимости из pyproject:

```
pip install -e .
```

5) Создайте `.env` на основе `.env.example` и заполните `TELEGRAM_TOKEN`, при использовании
резерва — `OPENAI_API_KEY`.

6) (Опционально) Установите `ffmpeg` и пропишите путь в `src/config/settings.yaml`
(`paths.ffmpeg_bin`) или добавьте в PATH. Можно воспользоваться
`scripts\servises\download_ffmpeg.bat`.

7) Запустите бота:

```
scripts\servises\run_bot.bat
```

## Структура
См. `project_progress/02_plan.md` и `src/`.

## Качество кода
- Линтер: Ruff (`pyproject.toml`)
- Стиль: PEP8, длина строки 100

## Примечания
- Работает без вебхуков (long polling).
- Локальный провайдер использует GPU (если доступна CUDA), при ошибках — fallback в облако.
- Временные файлы в `var/` (в .gitignore).


