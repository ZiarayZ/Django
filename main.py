from src.config.config import fetch_config
import asyncio
import pygame

# Do init here
# Load any assets right now to avoid lag at runtime or network errors.
config = fetch_config()
# initializing imported module
pygame.init()

screen = pygame.display.set_mode((400, 500))
clock = pygame.time.Clock()
playerRect = pygame.Rect(250, 250, 50, 50)

# Setting name for window
pygame.display.set_caption("Square Game")


async def main():
    global screen, clock, playerRect

    while True:
        clock.tick(60)
        screen.fill((0, 0, 0))

        # Check for event if user has pushed
        # any event in queue
        for event in pygame.event.get():

            # if event is of type quit then set
            # running bool to false
            if event.type == pygame.QUIT:
                return

        # player movement
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_w] or user_input[pygame.K_UP]:
            playerRect.y -= 10
        if user_input[pygame.K_s] or user_input[pygame.K_DOWN]:
            playerRect.y += 10
        if user_input[pygame.K_a] or user_input[pygame.K_LEFT]:
            playerRect.x -= 10
        if user_input[pygame.K_d] or user_input[pygame.K_RIGHT]:
            playerRect.x += 10
        # player quits
        if user_input[pygame.K_ESCAPE]:
            return

        pygame.draw.rect(screen, (255, 50, 50), playerRect)

        pygame.display.update()  # should go right next line
        pygame.display.flip()

        await asyncio.sleep(0)  # Very important, and keep it 0


# This is the program entry point:
asyncio.run(main())

# Do not add anything from here, especially sys.exit/pygame.quit
# asyncio.run is non-blocking on pygame-wasm and code would be executed
# right before program start main()
