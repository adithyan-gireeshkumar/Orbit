import argparse
import torch
from transformers import pipeline
from huggingface_hub import HfApi, scan_cache_dir, snapshot_download

def run_model(model_id):
    print(f"Loading model : {model_id}..")

    device = 0 if torch.cuda.is_available() else -1

    ai = pipeline(
        "text-generation",
        model=model_id,
        device=device
    )
    print("Orbit is ready. Type 'exit' to quit.")
    conversation = []

    while True:
        prompt = input("You: ").strip()

        if prompt.lower() == "exit":
            break

        if not prompt:
            continue

        if getattr(ai.tokenizer, "chat_template", None):
            conversation.append({
                "role": "user",
                "content": prompt,
            })

            result = ai(
                conversation,
                max_new_tokens=200,
            )

            generated = result[0]["generated_text"]

            if isinstance(generated, list):
                answer = generated[-1]["content"]
                conversation = generated
            else:
                answer = str(generated)
                conversation.append({
                    "role": "assistant",
                    "content": answer,
                })

        else:
            result = ai(
                prompt,
                max_new_tokens=200,
                return_full_text=False,
            )

            answer = result[0]["generated_text"]


        print(f"\nOrbit: {answer}\n")
def list_models():
    cache = scan_cache_dir()

    models = sorted(
        (repo for repo in cache.repos if repo.repo_type == "model"),
        key=lambda repo: repo.repo_id.lower(),
    )

    if not models:
        print("No cached Hugging Face models found.")
        return

    print("Cached Hugging Face models:\n")

    for model in models:
        size_gb = model.size_on_disk / (1024 ** 3)
        print(f"{model.repo_id} ({size_gb:.2f} GB)")
def pull_model(model_id):
    print(f"Pulling model : {model_id}..")
    try:
        path = snapshot_download(repo_id=model_id)
        print(f"\nDownload Completed")
        print(f"Model path: {path}")
    except Exception as error:
        print(f"\nDownload failed: {error}")

def main():
    
    parser = argparse.ArgumentParser(prog="orbit")
    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )
    subparsers.add_parser(
        "list",
        help="List cached Hugging Face models",
    )
    run_parser = subparsers.add_parser(
        "run",
        help="Run a Hugging Face model",
    )
    run_parser.add_argument(
        "model_id",
        help="The Hugging Face model ID",
    )
    pull_parser = subparsers.add_parser(
        "pull",
        help="Download a Hugging Face model",
    )

    pull_parser.add_argument(
        "model_id",
        help="Hugging Face model repository ID",
    )
    args = parser.parse_args()

    if args.command == "run":
        run_model(args.model_id)
    elif args.command == "list":
        list_models()
    elif args.command == "pull":
        pull_model(args.model_id)

if __name__ == "__main__":
    main()
