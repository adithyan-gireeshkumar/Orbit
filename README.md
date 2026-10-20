
# Orbit 

A simple, open-source local AI model runner powered by Hugging Face Transformers.

Orbit lets you download Hugging Face models, manage your local model cache, and run supported models directly on your computer.

## Features

- Download models from Hugging Face.
- Run supported text-generation models locally.
- List cached Hugging Face models.
- Use a simple command-line interface.
- No Ollama or cloud inference service required.

## Requirements

- Python 3.10 or newer
- Internet connection for downloading models
- Sufficient RAM, storage, and compatible hardware for your chosen model

## Installation

Clone the repository:

```bash
git clone https://github.com/adithyan-gireeshkumar/Orbit.git
cd Orbit
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install Orbit:

```bash
python -m pip install --upgrade pip
python -m pip install -e .
```

## Usage

Download a model:

```bash
orbit pull Qwen/Qwen2.5-0.5B-Instruct
```

List cached models:

```bash
orbit list
```

Run a model:

```bash
orbit run Qwen/Qwen2.5-0.5B-Instruct
```

Type `exit` to leave the chat.

## How it works

Orbit uses Hugging Face Hub to download and cache model files, and Transformers to load supported models for text generation.

Model inference runs locally. The initial download requires internet access, and model size and performance depend on your computer's hardware.

## Project status

Orbit is an early-stage open-source project. Model compatibility, hardware support, and the command-line interface are still evolving.

Bug reports and contributions are welcome.

## License

Orbit is licensed under the MIT License. See [LICENSE](LICENSE).
