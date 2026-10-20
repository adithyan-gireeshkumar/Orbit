import requests

def main ():
    model = "qwen2.5-coder:7b"
    api = "https://localhost:11434/api/generate"

    print(f"Orbit Running... {model}")
    print("Type 'exit' to quit.")

    while True:
        prompt = input("You:").strip()

        if prompt.lower() == "exit":
            print("Exiting...")
            break

            if not prompt:
                continue
                response = requests.post(
                    api,
                    json={
                        "model" : model,
                        "prompt" : prompt,
                        "stream" : False,
                    },
                    timeout = 300,
                )
                response.raise_for_status()
                print(f"Orbit: {response.json()['response']}")

                if __name__ == "__main__":
                    main()