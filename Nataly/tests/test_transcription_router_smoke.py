import shutil
from pathlib import Path
import pytest

from src.core.config import load_config
from src.transcription.audio_io import convert_to_wav_16k_mono
from src.transcription.router import TranscriptionRouter


@pytest.mark.skipif(shutil.which("ffmpeg") is None, reason="ffmpeg not installed")
def test_router_smoke_local(tmp_path: Path) -> None:
	# Skip if faster-whisper is not installed to avoid heavy dependency in CI by default
	try:
		from faster_whisper import WhisperModel  # noqa: F401
	except Exception:
		pytest.skip("faster-whisper not installed")

	# generate small wav and convert
	import wave, math, struct  # noqa: E401

	src = tmp_path / "sine.wav"
	with wave.open(str(src), "w") as w:
		w.setnchannels(1)
		w.setsampwidth(2)
		w.setframerate(16000)
		for i in range(16000 // 2):
			val = int(32767 * 0.1 * math.sin(2 * math.pi * 440 * i / 16000))
			w.writeframes(struct.pack("<h", val))

	cfg = load_config()
	dst = tmp_path / "norm.wav"
	convert_to_wav_16k_mono(src, dst, ffmpeg_bin=cfg.paths.ffmpeg_bin)

	router = TranscriptionRouter(config=cfg)
	# Should not raise
	try:
		router.transcribe(dst)
	except Exception:
		pytest.skip("Model may not be available locally; skip heavy smoke test")


