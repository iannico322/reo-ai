"""
JARVIS configuration.

Everything you'll want to tweak lives here so you don't have to dig through
the code. Change a value, restart, done.
"""

# ---------------------------------------------------------------------------
# Identity
# ---------------------------------------------------------------------------
ASSISTANT_NAME = "Reo"

SYSTEM_PROMPT = (
    "You are Reo, a sharp and funny AI assistant with the personality of a witty tech-savvy friend. "
    "You are deeply knowledgeable in technology — programming, software, hardware, networking, AI, "
    "cybersecurity, and everything in between. You think analytically and explain things clearly, "
    "but always sneak in a dry joke or clever observation when it fits naturally. "
    "You understand Bisaya (Cebuano) and Filipino — if the user speaks in Bisaya or mixes it with English, "
    "understand them fully and respond in English unless they explicitly ask you to reply in Bisaya. "
    "RESPONSE RULES — follow strictly: "
    "1. For normal conversation: one or two sentences max. Be direct, be smart, be a little funny. "
    "2. For code requests: output the code immediately in a fenced code block using triple backticks "
    "with the language name (e.g. ```python). Add only one short sentence before or after the code, not both. "
    "3. Never use bullet points, emojis, or markdown outside of code blocks. "
    "4. Never translate your own replies into another language in parentheses — say it once. "
    "5. If you genuinely don't know something, say so with confidence — never bluff."
)

# ---------------------------------------------------------------------------
# Speech-to-Text  (faster-whisper, runs offline on CPU)
# ---------------------------------------------------------------------------
WHISPER_MODEL = "base"        # tiny | base | small  (bigger = more accurate + slower)
WHISPER_COMPUTE = "int8"      # int8 is the fastest on a CPU
WHISPER_LANGUAGE = None       # None = auto-detect (handles Bisaya/Filipino/English)

# ---------------------------------------------------------------------------
# Microphone / recording
# ---------------------------------------------------------------------------
SAMPLE_RATE = 16000           # Whisper expects 16 kHz — leave this alone
SILENCE_THRESHOLD = 0.012     # mic loudness below this counts as "silence".
                              # Too sensitive? raise it. Cuts you off? lower it.
SILENCE_DURATION = 1.2        # seconds of quiet that mark the end of your sentence
MAX_RECORD_SECONDS = 15       # hard cap so it never records forever

# ---------------------------------------------------------------------------
# Brain  (Ollama, runs offline)
# ---------------------------------------------------------------------------
OLLAMA_MODEL = "llama3.2:3b"  # alternatives:
                              #   "gemma3:2b"   -> fastest, lighter
                              #   "qwen2.5:3b"  -> better at following commands
MEMORY_TURNS = 6              # how many recent back-and-forths Reo remembers

# ---------------------------------------------------------------------------
# Voice
# Primary: edge-tts (Microsoft neural voices, internet required)
#   TTS_VOICE  — any ShortName from `python -c "from core.voice import list_voices; list_voices()"`
#   TTS_RATE_EDGE — speaking rate offset, e.g. "+0%", "+10%", "-5%"
# Fallback: pyttsx3 (Windows SAPI voices, fully offline)
#   TTS_RATE / TTS_VOICE_INDEX used only when edge-tts is unavailable
# ---------------------------------------------------------------------------
TTS_VOICE       = "en-US-GuyNeural"   # edge-tts voice (natural, online)
TTS_RATE_EDGE   = "+5%"               # slightly faster than default
TTS_RATE        = 180                  # pyttsx3 fallback: words per minute
TTS_VOICE_INDEX = 0                    # pyttsx3 fallback: voice index

# ---------------------------------------------------------------------------
# Wake / exit
# ---------------------------------------------------------------------------
# Phrases that end the session when spoken.
EXIT_PHRASES = ["goodbye", "exit", "quit", "go to sleep", "shut down reo"]
