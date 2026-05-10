# Extract session metadata and transcripts for analysis.

def extract_session(path):
    """Load transcript and metadata from a session directory."""
    return {
        "transcript": open(f"{path}/transcript.md").read(),
        "metadata": open(f"{path}/metadata.json").read()
    }
