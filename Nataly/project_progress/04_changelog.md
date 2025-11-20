# Хронологический журнал

- init: создан каркас проекта, pyproject.toml, базовые документы и .gitignore.
- core: добавлены config/logging/storage (SQLite), settings.yaml.
- audio: добавлены конвертация в WAV 16k/mono (ffmpeg) и чанкинг.
- providers: реализованы faster-whisper (CUDA) и OpenAI, тестовые .bat.
- router: выбор провайдера, тайм-ауты, fallback, кэш в SQLite.
- bot: обработчики /start /help /settings и приём аудио/voice/video_note/документов.
- tests: unit и smoke, бат-скрипт запуска pytest.


