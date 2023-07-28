import pygame

class Font:
    def __init__(self, filepath: str, target_resolution: int, character_order: list[str], split_color: int = 127) -> None:
        self.font_atlas = pygame.image.load(filepath).convert_alpha()
        self.font_atlas.set_colorkey((0,0,0,0))

        # changing font color
        for x in range(self.font_atlas.get_width()):
            for y in range(self.font_atlas.get_height()):
                pixel = self.font_atlas.get_at((x,y))
                if pixel[0] == 0 and pixel[3] == 255:
                    self.font_atlas.set_at((x,y), "white")

        self.scale = target_resolution / self.font_atlas.get_height()
        self.char_spacing = {}
        self.characters = self.get_characters(self.font_atlas, character_order, split_color)
        self.inbetweenchar = self.char_spacing['A']*0.25
        self.space = self.char_spacing['A']
        self.char_spacing[" "] = self.space
        self.line_spacing = self.font_atlas.get_height() * self.scale * 1.2
    def get_characters(self, font_atlas: pygame.Surface, character_order: list[str], split_color: int) -> dict:
        characters = {}
        
        character_index = 0
        prev_split_index = 0

        for x in range(font_atlas.get_width()):
            pixel = font_atlas.get_at((x, 0))
            if pixel[0] == split_color:
                characters[character_order[character_index]] = self.create_surf(font_atlas, prev_split_index, x)
                self.char_spacing[character_order[character_index]] = int((x-prev_split_index)*self.scale)
                # print(f'{x-prev_split_index} {character_order[character_index]}')
                prev_split_index = x+1
                character_index += 1
            if character_index > len(character_order)-1:
                break
        return characters
    def create_surf(self, font_atlas: pygame.Surface, left, right):
        image = pygame.transform.scale_by(pygame.Surface.subsurface(font_atlas, pygame.Rect(left, 0, right-left, font_atlas.get_height())), self.scale)
        image.set_colorkey((0,0,0))
        return image
    
    def draw_character(self, char: str, display: pygame.Surface, coords: tuple):
        if char != " ":
            display.blit(self.characters[char], coords)
    def draw_paragraph(self, text, display: pygame.Surface, position: tuple):
        if type(text) == str:
            text_li = [char for char in text]
        else:
            text_li = text
        paragraph_line = 0
        right_spacing = 0

        for i, char in enumerate(text_li):
            if char == "\n":
                paragraph_line += 1
                right_spacing = 0
            else:
                self.draw_character(char, display, (position[0] + right_spacing, position[1] + paragraph_line*self.line_spacing))
                char_spacing = self.char_spacing[char] + self.inbetweenchar
                right_spacing += char_spacing
    def draw_paragraph_within_bounds(self, text, display: pygame.Surface, position: tuple, bounds: pygame.Rect, padding: tuple = (10,10)):
        if type(text) == str:
            text_li = [char for char in text]
        else:
            text_li = text
        paragraph_line = 0
        right_spacing = padding[0]

        for i, char in enumerate(text_li):
            if right_spacing > bounds.width - (padding[0]*2):
                paragraph_line += 1
                right_spacing = padding[0]
                if char != "\n":
                    self.draw_character(char, display, (position[0] + right_spacing, position[1] + paragraph_line*self.line_spacing + padding[1]))
                    char_spacing = self.char_spacing[char] + self.inbetweenchar
                    right_spacing += char_spacing
            else:
                if not self.overflow_text(text_li[i:len(text_li)-1], bounds.width-right_spacing-(padding[0]*2)):
                    self.draw_character(char, display, (position[0] + right_spacing, position[1] + paragraph_line*self.line_spacing + padding[1]))
                    char_spacing = self.char_spacing[char] + self.inbetweenchar
                    right_spacing += char_spacing
                else:
                    right_spacing = padding[0]
                    paragraph_line += 1
                    self.draw_character(char, display, (position[0] + right_spacing, position[1] + paragraph_line*self.line_spacing + padding[1]))
                    char_spacing = self.char_spacing[char] + self.inbetweenchar
                    right_spacing += char_spacing
    def overflow_text(self, text: list, text_space: int) ->bool:
        text_length = 0
        for text in text:
            text_length += self.char_spacing[text]
            if text_length > text_space:
                return True
            if text == " " or text == "\n":
                return False
        return False