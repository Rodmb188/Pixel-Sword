from code.Const import C_GREEN, C_WHITE, TITLE, TITLE_SIZE


class Menu:

    def __init__(self):
        self.options = [
            "Start Game",
            "Commands",
            "Quit"
        ]

        self.selected = 0

    def move_up(self):
        if self.selected > 0:
            self.selected -= 1

    def move_down(self):
        if self.selected < len(self.options) - 1:
            self.selected += 1

    def draw(self, screen, font):
        title = font.render(TITLE, True, C_WHITE)
        screen.blit(title, TITLE_SIZE)

        for index, option in enumerate(self.options):
            if index == self.selected:
                option_text = "► " + option
                color = C_GREEN
            else:
                option_text = "   " + option
                color = C_WHITE
            
            text = font.render(
                option_text,
                True,
                color
            )

            screen.blit(
                text,
                (100, 200 + index * 60)
            )
