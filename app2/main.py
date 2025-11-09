from importlib import metadata


def main():
    print("Hello from app2!")
    packages = metadata.distributions()
    for package in packages:
        print(f"- {package.metadata['Name']} ({package.version})")


if __name__ == "__main__":
    main()
