import os
from views import app

import granian

# For direct execution during development
if __name__ == "__main__":
    import granian
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", "8000"))
    granian.run(app, host=host, port=port)