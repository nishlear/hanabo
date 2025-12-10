FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies using uv
RUN uv sync

# Run the bot using uv run (automatically uses .venv)
CMD ["uv", "run", "python", "src/main.py"]