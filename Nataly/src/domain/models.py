from __future__ import annotations

from typing import List, Optional
from pydantic import BaseModel


class TranscriptionSegment(BaseModel):
	start: float
	end: float
	text: str


class TranscriptionResult(BaseModel):
	text: str
	language: Optional[str] = None
	segments: List[TranscriptionSegment] = []
	provider: str = ""


