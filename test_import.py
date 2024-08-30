try:
    from dotenv import load_dotenv
    print("Module imported successfully!")
except ModuleNotFoundError as e:
    print(e)