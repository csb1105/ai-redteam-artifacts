"""
extract_sessions.py

Utilities for loading session transcripts and metadata into analysis workflows.
"""

import json
from pathlib import Path


def extract_session(session_dir: str) -> dict:
    """
    Load transcript and metadata from a session directory.

    Args:
        session_dir: Path to the session directory.

    Returns:
        A dictionary with 'transcript' (str) and 'metadata' (dict).
    """
    base = Path(session_dir)
    transcript = (base / "transcript.md").read_text(encoding="utf-8")
    metadata = json.loads((base / "metadata.json").read_text(encoding="utf-8"))
    return {"transcript": transcript, "metadata": metadata}
