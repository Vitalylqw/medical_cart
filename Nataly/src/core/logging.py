from __future__ import annotations

import logging
import sys


def setup_logging(level: str = "INFO") -> None:
	"""Configure root logging with concise format suitable for console output."""
	root = logging.getLogger()
	if root.handlers:
		return

	logging.basicConfig(
		level=getattr(logging, level.upper(), logging.INFO),
		format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
		stream=sys.stdout,
	)


