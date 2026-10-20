import requests


def main():
    model = "qwen2.5-coder:7b"
    api = "http://localhost:11434/api/generate"

    print(f"Orbit running... {model}")
    print("Type 'exit' to quit.\n")

    while True:
        prompt = input("You: ").strip()

        if prompt.lower() == "exit":
            print("Exiting...")
            break

        if not prompt:
            continue

        try:
            response = requests.post(
                api,
                json={
                    "model": model,
                    "prompt": prompt,
                    "stream": False,
                },
                timeout=300,
            )
            response.raise_for_status()
            print(f"\nOrbit: {response.json()['response']}\n")

        except requests.RequestException as error:
            print(f"Could not connect to Ollama: {error}")


if __name__ == "__main__":
    main()