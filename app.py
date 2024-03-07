from src.config.config import fetch_config

config = fetch_config()

if __name__ == "__main__" and config != None:
    print("hello world!")
