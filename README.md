# utils

Personal utilities and scripts.

## Contents

### `.local/bin/logging.py`

A Python logging factory with optional per-handler level filtering.

```python
from logging_util import get_logger

log = get_logger("myapp", log_file="app.log")
log.info("started")

# Only emit WARNING–ERROR to stdout, everything to the file
log = get_logger("myapp", log_file="app.log", min_level=30, max_level=40)
```

**`get_logger(name, level, log_file, fmt, datefmt, min_level, max_level)`**

| Parameter | Default | Description |
|-----------|---------|-------------|
| `name` | — | Logger name |
| `level` | `INFO` | Root logger level |
| `log_file` | `None` | Optional file path; parent dirs created automatically |
| `fmt` | `%(asctime)s [%(levelname)s] %(name)s: %(message)s` | Log format |
| `datefmt` | `%Y-%m-%d %H:%M:%S` | Timestamp format |
| `min_level` | `None` | Clamp handler to this minimum level |
| `max_level` | `None` | Clamp handler to this maximum level |

Returns the same logger on repeated calls (idempotent).
