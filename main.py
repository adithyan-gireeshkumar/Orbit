import argparse
import torch
from transformers import pipeline


def main():
    model_id = input("Hugging Face model ID: ").strip()

    if not model_id:
        print("Model ID is required.")
        return

    print(f"\nLoading model: {model_id}...")
    print("The first run may download model files.")

    device = 0 if torch.cuda.is_available() else -1

    ai = pipeline(
        "text-generation",
        model=model_id,
        device=device,
    )

    print("\nOrbit is ready. Type 'exit' to quit.\n")

    while True:
        prompt = input("You: ").strip()

        if prompt.lower() == "exit":
            break

        if not prompt:
            continue

        result = ai(
            prompt,
            max_new_tokens=200,
            return_full_text=False,
        )

        print(f"\nOrbit: {result[0]['generated_text']}\n")


if __name__ == "__main__":
    main()