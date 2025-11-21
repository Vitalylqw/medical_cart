# Описание и цель проекта

Цель: локальный Telegram‑бот (Windows 10, long polling), который принимает голос/аудио
разных форматов, автоматически определяет язык и возвращает транскрипт текста.

Архитектура: монолит. Основной провайдер — локальный faster‑whisper (GPU), резерв — OpenAI.

Ключевые требования:
- Мультиязычность, авто‑детект языка
- Поддержка voice/audio/video_note/документов (ogg/opus, mp3, m4a, wav, webm, flac)
- Конверсия в WAV 16kHz mono (ffmpeg)
- Кэш транскриптов по хэшу
- Документация прогресса в `project_progress/*`

Релевантные решения:
- `aiogram 3` для бота
- `faster-whisper` (CUDA, float16) + OpenAI API как резерв
- Конфиг через `.env` + `src/config/settings.yaml`
- Хранилище: SQLite + файлы в `var/`
- Тестирование: `pytest` + `pytest-cov` (покрытие 59%), unit-тесты для core/config, core/storage, transcription/router

## Подключение провайдеров (кратко)
- Локально: `pip install faster-whisper` и установите `ffmpeg`. Путь можно указать в
  `paths.ffmpeg_bin` в `src/config/settings.yaml`. Модель по умолчанию: `large-v3` (CUDA, 14 ГБ VRAM).
- Облако (резерв): `pip install openai`, задайте `OPENAI_API_KEY` в `.env`.
  Модель: `gpt-4o-mini-transcribe` (fallback: `whisper-1`).


