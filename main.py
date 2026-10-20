from huggingface_hub import snapshot_download

model_id = input("Enter your model ID: ").strip()

if not model_id:
    print("Model ID cannot be empty.")
else:
    print(f"Downloading {model_id}...")
    path = snapshot_download(repo_id=model_id)

    print(f"Model downloaded to: {path}")