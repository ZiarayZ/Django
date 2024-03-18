import asyncio
from src.config.config import fetch_config


# Try to declare all your globals at once to facilitate compilation later.
COUNT_DOWN = 20

# Do init here
# Load any assets right now to avoid lag at runtime or network errors.
config = fetch_config()


async def main():
    global COUNT_DOWN

    while True:

        # Do your rendering here, note that it's NOT an infinite loop,
        # and it is fired only when VSYNC occurs
        # Usually 1/60 or more times per seconds on desktop
        # could be less on some mobile devices
        if __name__ == "__main__" and config != None:
            print(
                f"""

                Hello[{COUNT_DOWN}] from Python

    """
            )
        # pygame.display.update() should go right next line

        await asyncio.sleep(0)  # Very important, and keep it 0

        if not COUNT_DOWN:
            return

        COUNT_DOWN = COUNT_DOWN - 1


# This is the program entry point:
asyncio.run(main())

# Do not add anything from here, especially sys.exit/pygame.quit
# asyncio.run is non-blocking on pygame-wasm and code would be executed
# right before program start main()
