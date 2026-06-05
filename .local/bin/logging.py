import logging
import sys
from pathlib import Path


class LevelFilter(logging.Filter):
    """Restrict a handler to records within [min_level, max_level]."""

    def __init__(self, min_level: int = logging.DEBUG, max_level: int = logging.CRITICAL):
        super().__init__()
        self.min_level = min_level
        self.max_level = max_level

    def filter(self, record: logging.LogRecord) -> bool:
        return self.min_level <= record.levelno <= self.max_level


def _apply_level_filter(
    handler: logging.Handler,
    min_level: int | None,
    max_level: int | None,
) -> None:
    if min_level is not None or max_level is not None:
        handler.addFilter(
            LevelFilter(
                min_level=min_level if min_level is not None else logging.DEBUG,
                max_level=max_level if max_level is not None else logging.CRITICAL,
            )
        )


def get_logger(
    name: str,
    level: int = logging.INFO,
    log_file: str | None = None,
    fmt: str = "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt: str = "%Y-%m-%d %H:%M:%S",
    min_level: int | None = None,
    max_level: int | None = None,
) -> logging.Logger:
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(level)
    formatter = logging.Formatter(fmt, datefmt=datefmt)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    _apply_level_filter(stream_handler, min_level, max_level)
    logger.addHandler(stream_handler)

    if log_file:
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(formatter)
        _apply_level_filter(file_handler, min_level, max_level)
        logger.addHandler(file_handler)

    logger.propagate = False
    return logger
