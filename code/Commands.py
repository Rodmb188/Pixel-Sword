from code.Const import C_WHITE, MENU_X, OPTION_SPACING, OPTION_Y, TITLE_SIZE


class Commands:

    def draw(self, screen, font):
        title = font.render("COMMANDS", True, C_WHITE)

        screen.blit(title, TITLE_SIZE)

        controls = [
            "A       - Walk Back",
            "D       - Walk Forward",
            "J       - Guard High",
            "K       - Guard Middle",
            "L       - Guard Low",
            "SPACE   - Attack",
            "",
            "ESC     - Back"
        ]
        
        for index, command in enumerate(controls):
            text = font.render(
                command,
                True,
                C_WHITE
            )

            screen.blit(
                text,
                (MENU_X, OPTION_Y + index * OPTION_SPACING)
            )