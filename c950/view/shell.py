import argparse


class Shell:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Package Delivery Service")
        self.parser.add_argument(
            "-d",
            "--debug",
            help="Show debug information",
            action="store_true",
            required=False,
        )
