# Статус выполнения

- Прогресс: 92%
- Сделано: каркас, конфиг, хранилище, аудио‑пайплайн, провайдеры, роутер, бот, кэш, скрипты, базовые и расширенные тесты (config/storage/router), добавлен скрипт покрытия
- Осталось: обновить пользовательскую/техдокументацию (провайдеры, тесты, CI), завести CI (ruff + pytest-cov) и адаптировать конфиг Ruff к новой схеме `lint`.

Чек‑лист:
- [x] Бутстрап репозитория и базовые файлы
- [x] Конфиг/логирование/хранилище
- [x] Аудио‑пайплайн
- [x] Провайдер faster‑whisper
- [x] Провайдер OpenAI
- [x] Router провайдеров + fallback
- [x] Бот и UX
- [x] Тесты и скрипты
- [ ] Документация обновлена
- [ ] CI и .gitignore


Дополнения (2025-11-21):
- Фикс `scripts/test/run_tests.bat`: теперь запускается из любой директории, использует `venv\Scripts\python.exe`, корректно возвращает код выхода.
- Актуальный результат тестов: 2 passed, 1 skipped.
- Добавлен сервисный загрузчик модели: `scripts/servises/download_faster_whisper_model.py` и бат‑обёртка `scripts/servises/download_faster_whisper_model.bat`. По умолчанию подтягивает модель из `local.model` (`settings.yaml`) и инициализируется на CPU, чтобы избежать требований CUDA при скачивании.
- pytest-cov добавлен в dev-зависимости, создан `scripts/test/run_coverage.bat`, текущее покрытие `pytest --cov=src --cov-report=term-missing`: 59% (8 passed, 1 skipped; без тяжелых smoke-тестов).
- Написаны юнит-тесты для `load_config`, `Storage` (transcripts и user_settings) и `TranscriptionRouter` (кэш-хит, fallback, склейка чанков); тяжелые зависимости заменены monkeypatch-стабами.
- Ruff запущен для новых тестов, выявлен deprecation warning для настроек (`[tool.ruff] select/ignore` → `[tool.ruff.lint]`), требуется обновление конфигурации в отдельной задаче.
- 2025-11-21 13:15: smoke-тест `tests/test_transcription_router_smoke.py`
  - Команда: `venv\Scripts\python.exe -m pytest tests\test_transcription_router_smoke.py -vv -rs`
  - Результат: `SKIPPED (Model may not be available locally; skip heavy smoke test)`
  - Что дальше: скачать локальную модель faster-whisper и убедиться в наличии `ffmpeg`
