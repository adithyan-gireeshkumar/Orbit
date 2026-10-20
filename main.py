import argparse
import torch
from transformers import pipeline
from huggingface_hub import scan_cache_dir

def run_model(model_id):
    print(f"Loading model : {model_id}..")

    device = 0 if torch.cuda.is_available() else -1

    ai = pipeline(
        "text-generation",
        model=model_id,
        device=device
    )
    print(f"Orbit is ready. Type 'exit' to quit.")
    while True:
        prompt = input("you: ").strip()
        if prompt.lower() == "exit":
            break
        if not prompt:
            continue

            result = ai(
                prompt,
                max_new_tokens=200,
                return_full_text=False,
            )
            print(f"Orbit: {result[0]['generated_text']}")

def main():
    parser = argparse.ArgumentParser(prog="orbit")
    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )
    run_parser = subparsers.add_parser(
        "run",
        help="Run a Hugging Face model",
    )
    run_parser.add_argument(
        "model_id",
        help="The Hugging Face model ID",
    )
    args = parser.parse_args()

    if args.command == "run":
        run_model(args.model_id)

if __name__ == "__main__":
    main()