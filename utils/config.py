import os

# Configurare generala

BASE_URL = "https://www.emag.ro"

# Timeout 10 sec
DEFAULT_TIMEOUT = 60000

# Browser settings
# Pe CI/CD (GitHub Actions) headless automat
HEADLESS = os.environ.get("CI", "false").lower() == "true"
SLOW_MO = 0 if HEADLESS else 50
