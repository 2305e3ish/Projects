import tkinter as tk
from collections import deque
import random
import time
from PIL import Image, ImageTk, ImageSequence
import pygame
import pygame.mixer
pygame.mixer.init()

# Function to check if there is a wall in the board
def is_wall(board, n):
    return any(all(board[i][j] == '0' for j in range(n)) for i in range(n)) or \
           any(all(board[i][j] == '0' for i in range(n)) for j in range(n)) or \
           all(board[i][i] == '0' for i in range(n)) or \
           all(board[i][n - 1 - i] == '0' for i in range(n))

# Function to get all possible moves from the current state of the board
def all_moves(board, n):
    moves = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == '0':
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < n and board[x][y] == ' ':
                        moves.append(((i, j), (x, y)))
    return moves

# Breadth-first search function to find the minimum number of moves to form a wall
def bfs(board, n):
    queue = deque([(board, 0)])
    visited = set()
    visited.add(tuple(''.join(row) for row in board))
    while queue:
        current_board, moves_count = queue.popleft()
        if is_wall(current_board, n):
            return moves_count, current_board
        for move in all_moves(current_board, n):
            new_board = [row[:] for row in current_board]
            (x1, y1), (x2, y2) = move
            new_board[x1][y1] = ' '
            new_board[x2][y2] = '0'
            newboard_str = tuple(''.join(row) for row in new_board)
            if newboard_str not in visited:
                queue.append((new_board, moves_count + 1))
                visited.add(newboard_str)
    return -1, None

# Function to solve the problem
def solve(n, stones):
    board = [[' ' for _ in range(n)] for _ in range(n)]
    for x, y in stones:
        board[x-1][y-1] = '0'
    return bfs(board, n)

class AnimatedCircle:
    def __init__(self, canvas, x, y, radius, color, speed_x, speed_y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.circle = self.canvas.create_oval(x - self.radius, y - self.radius, x + self.radius, y + self.radius, fill=self.color, outline=self.color)
        self.is_animating = True
        self.animate()

    def animate(self):
        if not self.is_animating:
            return
        new_x = self.x + self.speed_x
        new_y = self.y + self.speed_y

        if new_x - self.radius < 0 or new_x + self.radius > self.canvas.winfo_width():
            self.speed_x = -self.speed_x
            self.change_color()  # Change color when hitting the left or right edge
            new_x = self.x + self.speed_x
            
        if new_y - self.radius < 0 or new_y + self.radius > self.canvas.winfo_height():
            self.speed_y = -self.speed_y
            self.change_color()  # Change color when hitting the top or bottom edge
            new_y = self.y + self.speed_y

        self.canvas.coords(self.circle, new_x - self.radius, new_y - self.radius, new_x + self.radius, new_y + self.radius)
        self.x = new_x
        self.y = new_y
        self.canvas.after(30, self.animate)
        
    def change_color(self):
        # Generate a new random color
        r = lambda: random.randint(0, 255)
        new_color = '#%02X%02X%02X' % (r(), r(), r())

        # Update the circle color
        self.canvas.itemconfigure(self.circle, fill=new_color, outline=new_color)
        self.color = new_color
        
    def stop_animation(self):
        self.is_animating = False
        
      
class HomePage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("The Great Wall Game")
        
        self.attributes('-fullscreen', True)

        # Create canvas for GIF
        self.canvas = tk.Canvas(self, bg="white", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Load and animate GIF
        self.gif_file =r"c:\Users\ishan\OneDrive\Documents\python\The_Great_Wall_game\giphy.gif"
        self.load_gif()

        self.create_title()
        self.create_buttons()

    def load_gif(self):
        gif = Image.open(self.gif_file)
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        
        # Resize frames to fit the screen size
        self.gif_frames = [ImageTk.PhotoImage(frame.resize((self.screen_width, self.screen_height), Image.LANCZOS)) for frame in ImageSequence.Iterator(gif)]
        self.current_frame = 0
        self.animate_gif()

    def animate_gif(self):
        frame = self.gif_frames[self.current_frame]
        self.canvas.create_image(0, 0, anchor=tk.NW, image=frame)
        self.current_frame = (self.current_frame + 1) % len(self.gif_frames)
        self.after((1), self.animate_gif)

    def create_title(self):
        title = tk.Label(self.canvas, text="The Great Wall Game", font=("Arial", 30, "bold"), fg="black",bg="light salmon")
        title.place(relx=0.5, rely=0.3, anchor='center')

        
    def create_buttons(self):
        play_button = tk.Button(self.canvas, text="Play", font=("Arial", 20), command=self.go_to_input_page, bg='white')
        play_button.place(relx=0.5, rely=0.5, anchor='center')

        about_button = tk.Button(self.canvas, text="About Game", font=("Arial", 20), command=self.about_game, bg='white')
        about_button.place(relx=0.5, rely=0.6, anchor='center')

    def go_to_input_page(self):
        self.destroy()
        InputPage().mainloop()

    def about_game(self):
        self.destroy()
        AboutPage().mainloop()
        
class AboutPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("About The Great Wall Game")
        self.configure(background='RosyBrown1')
        self.attributes('-fullscreen', True)
        canvas = tk.Canvas(self, bg="RosyBrown1", highlightthickness=0)
        canvas.pack(fill='both', expand=True)
        paragraph_text=(
            '''                                  
                                                                                    ABOUT THE GREAT WALL GAME                                  
            The  Great  Wall  Game  is  played  by  one  player .  
            The  objective  is  to  build  a  wall of stones .  
            If  the  number  of  moves  made  by  the  player  is  equal  to  the  minimum  number  of  moves  required to form a wall ,  
            the  player  wins.'''
            "\n\n"
            "\n\n"
            '''           HOW TO PLAY:
            
            1. The  value  of  n  is  given  by the  user ,  where  n  is  the  size  of  the  board.\n
            2. The  game  is  played  by  the  user  with  n  stones  on  an  n × n  grid .\n
            3.  The  stones  are  placed  at  random  in the  squares  of  the  grid ,  at  most  one  stone  per  square .\n
            4. In  a  single  move ,  any  single  stone  can  move  into  an  unoccupied  location  one  unit  horizontally  or  vertically .\n
            5.  The  goal  of  the game  is  to  build  a  wall  of  stones  using  the  fewest  number  of  moves  .\n '''
            
        )
        paragraph_label = tk.Label(self, text=paragraph_text, font=("Arial", 20), bg="RosyBrown1", fg="Black", wraplength=1250, justify='left')
        paragraph_label.place(relx=0, rely=-0.1, anchor='nw',relwidth=1, relheight=0.95)
        back_button = tk.Button(self, text="Back to Home", font=("Arial", 20), bg="white", fg="black", command=self.go_to_home_page)
        back_button.place(relx=0.6, rely=0.9, anchor='se') 

    def go_to_home_page(self):
        self.destroy()
        HomePage().mainloop()
        
class InputPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg='white')
        self.attributes('-fullscreen', True)
        self.after(1, self.initialize_gui)  # Delay the GUI initialization by 1ms

    def initialize_gui(self):
        # Create the canvas
        self.canvas = tk.Canvas(self, bg="white", highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)

        # Load the image
        image_path = r"c:\Users\ishan\OneDrive\Documents\python\The_Great_Wall_game\input_page_img.jpg"
        try:
            image = Image.open(image_path)
            print(f"Image loaded successfully: {image_path}")
        except Exception as e:
            print(f"Error loading image: {e}")
            image = None

        if image:
            # Resize the image to fit the full screen
            self.screen_width = self.winfo_screenwidth()
            self.screen_height = self.winfo_screenheight()
            image = image.resize((self.screen_width, self.screen_height), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            # Create an image object on the canvas
            self.bg_image = self.canvas.create_image(0, 0, anchor='nw', image=photo)
            self.canvas.image = photo  # Keep a reference to prevent garbage collection

        # Create the heading label
        heading_label = tk.Label(self, text="Input Board Size", font=("Arial", 24, "bold"), bg="light salmon", fg="black")
        heading_label_window = self.canvas.create_window(self.screen_width // 2, self.screen_height // 3, window=heading_label)

        # Create the entry field
        self.entry = tk.Entry(self, font=("Arial", 20), width=13)
        self.entry.focus_set()
        entry_window = self.canvas.create_window(self.screen_width // 2, self.screen_height // 2, window=self.entry)

        # Create the animated circle
        self.circle = AnimatedCircle(self.canvas, 100, 100, 35, "black", 20, 15)

        # Create the OK button
        button = tk.Button(self, text="OK", font=("Arial", 15, "bold"), bg="white", fg="black", padx=20, pady=10, command=self.create_board)
        button_window = self.canvas.create_window(self.screen_width // 2, (self.screen_height // 4) * 3, window=button)

    def create_board(self):
        board_size = self.entry.get()
        if board_size.isdigit():
            self.circle.stop_animation()
            self.destroy()
            BoardGUI(int(board_size)).mainloop()
        else:
            error_label = tk.Label(self, text="Please enter a valid integer.", fg="red", font=("Arial", 14))
            error_label_window = self.canvas.create_window(self.screen_width // 2, (self.screen_height // 4) * 3.5, window=error_label)
            


class BoardGUI(tk.Tk):
    def __init__(self, board_size):
        super().__init__()
        self.title("Board with Stone Positions")
        self.board_size = board_size
        self.stone_positions = set()
        self.attributes('-fullscreen', True)
        self.configure(background="#2F4F4F")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        board_size_percentage = 0.7
        max_board_size = int(min(screen_width, screen_height) * board_size_percentage)
        cell_size = max_board_size // board_size
        board_width = cell_size * board_size
        board_height = cell_size * board_size

        self.board_frame = tk.Canvas(self, width=board_width, height=board_height, bg="#2F4F4F", bd=30, relief="ridge")
        self.board_frame.place(relx=0.5, rely=0.4, anchor="center")

        self.buttons = []
        for i in range(board_size):
            row = []
            for j in range(board_size):
                button = tk.Canvas(self.board_frame, width=cell_size, height=cell_size, bg="#fffde0", highlightthickness=1, highlightbackground="black")
                button.bind("<Button-1>", lambda event, x=i, y=j: self.toggle_stone(x, y))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        proceed_button = tk.Button(self, text="Proceed", font=("Arial", 20, "bold"), bg="white", fg="black", command=self.proceed_to_game)
        proceed_button.place(relx=0.5, rely=0.93, anchor="center")

        back_button = tk.Button(self, text="Back", font=("Arial", 20, "bold"), bg="white", fg="black", command=self.go_to_input_page)
        back_button.place(relx=0.3, rely=0.93, anchor="center")

        clear_button = tk.Button(self, text="Clear", font=("Arial", 20, "bold"), bg="white", fg="black", command=self.clear_board)
        clear_button.place(relx=0.7, rely=0.93, anchor="center")
        self.selected_stone = None

    def toggle_stone(self, row, col):
        button = self.buttons[row][col]
        if button.find_withtag("stone") == ():
            if len(self.stone_positions) < self.board_size:
                button.create_oval(5, 5, button.winfo_reqwidth() - 5, button.winfo_reqheight() - 5, fill='saddle brown', tags="stone")
                self.stone_positions.add((row + 1, col + 1))
        else:
            button.delete("stone")
            self.stone_positions.discard((row + 1, col + 1))

    def proceed_to_game(self):
        if len(self.stone_positions) == self.board_size:
            moves_required, final_board = solve(self.board_size, list(self.stone_positions))
            if moves_required != -1:
                self.destroy()
                SplitBoardGUI(self.board_size, list(self.stone_positions)).mainloop()
            else:
                self.result_label.config(text="No wall can be formed.")
        else:
            self.result_label.config(text="Please place exactly the number of stones equal to board size.")

    def go_to_input_page(self):
        self.destroy()
        InputPage().mainloop()
        
    def clear_board(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                button = self.buttons[row][col]
                button.delete("stone")
        self.stone_positions.clear()
        self.result_label.config(text="")
        self.reset_button_colors()

    def reset_button_colors(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                button = self.buttons[row][col]
                if button.find_withtag("stone") == ():
                    button.config(bg='#fffde0')
                else:
                    button.config(bg='#fffde0')



class SplitBoardGUI(tk.Tk):
    
    def __init__(self, board_size, stone_positions):
        super().__init__()
        self.title("The Great Wall Game - Split Board")
        self.board_size = board_size
        self.stone_positions = set(stone_positions)
        self.move_count = 0
        self.attributes('-fullscreen', True)
        self.configure(background="#2F4F4F")
        
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        board_size_percentage = 0.6
        max_board_size = int(min(screen_width, screen_height) * board_size_percentage)
        cell_size = max_board_size // board_size
        board_width = cell_size * board_size
        board_height = cell_size * board_size

        self.board_frames = []
        for i in range(2):
            frame = tk.Canvas(self, width=board_width, height=board_height, bg="#2F4F4F", highlightthickness=30,highlightbackground="black", relief="ridge")
            frame.place(relx=0.25 + i * 0.5, rely=0.4, anchor="center")
            self.board_frames.append(frame)
            
        user_board_label = tk.Label(self, text="User Board", font=("Arial", 30), bg="#2F4F4F", fg="white")
        user_board_label.place(relx=0.25, rely=0.035, anchor="center")
        
        computer_board_label = tk.Label(self, text="Computer Board", font=("Arial", 30), bg="#2F4F4F", fg="white")
        computer_board_label.place(relx=0.75, rely=0.035, anchor="center")
        
        self.buttons = [[], []]
        for k in range(2):
            for i in range(board_size):
                row = []
                for j in range(board_size):
                    button = tk.Canvas(self.board_frames[k], width=cell_size, height=cell_size, bg="#fffde0", highlightthickness=0.7, highlightbackground="black")
                    button.grid(row=i, column=j)
                    if k == 0:  # Left board
                        button.bind("<Button-1>", lambda event, x=i, y=j: self.select_stone(x, y))
                    row.append(button)
                self.buttons[k].append(row)
                

        for x, y in stone_positions:
            self.buttons[0][x-1][y-1].create_oval(5, 5, cell_size - 5, cell_size - 5, fill='saddle brown', tags="stone")
            self.buttons[1][x-1][y-1].create_oval(5, 5, cell_size - 5, cell_size - 5, fill='saddle brown', tags="stone")

        self.move_label = tk.Label(self, text=f"Moves: {self.move_count}", font=("Arial", 20), bg="white", fg="black", width="8")
        self.move_label.place(relx=0.25, rely=0.78, anchor="center")

        match_button = tk.Button(self, text="Enter", font=("Arial", 20, "bold"), bg="white", fg="black",width="8", command=self.match_stones)
        match_button.place(relx=0.5, rely=0.9, anchor="center")

        self.result_label = tk.Label(self, text="", font=("Arial", 20), bg="white", fg="black")
        self.result_label.place(relx=0.75, rely=0.78, anchor="center")

        self.selected_stone = None

    def select_stone(self, row, col):
        if self.buttons[0][row][col].find_withtag("stone") != ():
            self.selected_stone = (row, col)
            self.highlight_moves(row, col)
        else:
            self.move_stone(row, col)

    def highlight_moves(self, row, col):
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = row + dx, col + dy
            if 0 <= x < self.board_size and 0 <= y < self.board_size and self.buttons[0][x][y].find_withtag("stone") == ():
                self.buttons[0][x][y].config(bg='SpringGreen4')

    def move_stone(self, row, col):
        if hasattr(self, 'selected_stone') and self.buttons[0][row][col].config('bg')[-1] == 'SpringGreen4':
            from_row, from_col = self.selected_stone
            cell_size = self.buttons[0][row][col].winfo_reqwidth()
            self.buttons[0][row][col].create_oval(5, 5, cell_size - 5, cell_size - 5, fill='saddle brown', tags="stone")
            self.buttons[0][from_row][from_col].delete("stone")
            self.reset_button_colors()
            self.move_count += 1
            self.move_label.config(text=f"Moves: {self.move_count}")
            delattr(self, 'selected_stone')

    def reset_button_colors(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                button = self.buttons[0][row][col]
                if button.find_withtag("stone") == ():
                    button.config(bg='#fffde0')
                else:
                    button.config(bg='#fffde0')
    def clear_board(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                button = self.buttons[0][row][col]
                button.delete("stone")
                button = self.buttons[1][row][col]
                button.delete("stone")
        self.move_count = 0
        self.move_label.config(text=f"Moves: {self.move_count}")
    
    def go_win(self):
        self.destroy()
        WinPage().mainloop()
        
    def go_lose(self):
        self.destroy()
        LosePage().mainloop()
        

    def match_stones(self):
        moves_required, final_board = solve(self.board_size, list(self.stone_positions))
        if moves_required != -1:
            for row in range(self.board_size):
                for col in range(self.board_size):
                    if final_board[row][col] == '0':
                        self.buttons[1][row][col].create_oval(5, 5, self.buttons[1][row][col].winfo_reqwidth() - 5, self.buttons[1][row][col].winfo_reqheight() - 5, fill='saddle brown', tags="stone")
                    else:
                        self.buttons[1][row][col].delete("stone")
            result_text = f"Minimum moves required: {moves_required}"

            if is_wall(final_board,self.board_size)==True and self.move_count==moves_required:
                self.result(result_text)
                self.go_win()
            else:
                self.result(result_text)
                self.go_lose()

    
    def result(self, result_text):
        self.result_label.config(text=result_text)
        self.update()
        time.sleep(2)


class WinPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Win")
        
        self.attributes('-fullscreen', True)

        # Create canvas for GIF
        self.canvas = tk.Canvas(self, bg="white", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Load and animate GIF
        self.gif_file = r"c:\Users\ishan\OneDrive\Documents\python\The_Great_Wall_game\win.gif"
        self.load_gif()

        self.create_title()
        self.create_buttons()

    def load_gif(self):
        gif = Image.open(self.gif_file)
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        
        # Resize frames to fit the screen size
        self.gif_frames = [ImageTk.PhotoImage(frame.resize((self.screen_width, self.screen_height), Image.LANCZOS)) for frame in ImageSequence.Iterator(gif)]
        self.current_frame = 0
        self.animate_gif()

    def animate_gif(self):
        frame = self.gif_frames[self.current_frame]
        self.canvas.create_image(0, 0, anchor=tk.NW, image=frame)
        self.current_frame = (self.current_frame + 1) % len(self.gif_frames)
        self.after((1), self.animate_gif)

    def create_title(self):
        title = tk.Label(self.canvas, text="Do you want to play again?", font=("Arial", 30, "bold"),bg="grey1", fg="white")
        title.place(relx=0.5, rely=0.7, anchor='center')

        
    def create_buttons(self):
        Yes_button = tk.Button(self.canvas, text="Yes", font=("Arial", 30), command=self.go_to_input_page, bg='white')
        Yes_button.place(relx=0.4, rely=0.85, anchor='center')

        No_button = tk.Button(self.canvas, text="No", font=("Arial", 30), command=self.game_over, bg='white')
        No_button.place(relx=0.6, rely=0.85, anchor='center')

    def go_to_input_page(self):
        self.destroy()
        InputPage().mainloop()
        
    def game_over(self):
        self.destroy()
        Game_Over_Page().mainloop()

class LosePage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lose")
        
        self.attributes('-fullscreen', True)

        # Create canvas for GIF
        self.canvas = tk.Canvas(self, bg="white", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Load and animate GIF
        self.gif_file = r"c:\Users\ishan\OneDrive\Documents\python\The_Great_Wall_game\lostgif.gif"
        self.load_gif()

        self.create_title()
        self.create_buttons()

    def load_gif(self):
        gif = Image.open(self.gif_file)
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        
        # Resize frames to fit the screen size
        self.gif_frames = [ImageTk.PhotoImage(frame.resize((self.screen_width, self.screen_height), Image.LANCZOS)) for frame in ImageSequence.Iterator(gif)]
        self.current_frame = 0
        self.animate_gif()

    def animate_gif(self):
        frame = self.gif_frames[self.current_frame]
        self.canvas.create_image(0, 0, anchor=tk.NW, image=frame)
        self.current_frame = (self.current_frame + 1) % len(self.gif_frames)
        self.after((1), self.animate_gif)

    def create_title(self):
        title = tk.Label(self.canvas, text="Do you want to play again?", font=("Arial", 30, "bold"),bg="grey1", fg="white")
        title.place(relx=0.5, rely=0.7, anchor='center')

        
    def create_buttons(self):
        Yes_button = tk.Button(self.canvas, text="Yes", font=("Arial", 30), command=self.go_to_input_page, bg='white')
        Yes_button.place(relx=0.4, rely=0.85, anchor='center')

        No_button = tk.Button(self.canvas, text="No", font=("Arial", 30), command=self.game_over, bg='white')
        No_button.place(relx=0.6, rely=0.85, anchor='center')

    def go_to_input_page(self):
        self.destroy()
        InputPage().mainloop()
        
    def game_over(self):
        self.destroy()
        Game_Over_Page().mainloop()

class Game_Over_Page(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Over")
        self.attributes('-fullscreen', True)

        # Create canvas for GIF
        self.canvas = tk.Canvas(self, bg="white", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Load and animate GIF
        self.gif_file = r"c:\Users\ishan\OneDrive\Documents\python\The_Great_Wall_game\Game_over.gif"
        self.load_gif()
        self.frame_count = 0
        
        self.stop_music()  # Call the stop_music function

    def stop_music(self):
        pygame.mixer.music.stop()  

    def load_gif(self):
        gif = Image.open(self.gif_file)
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        
        # Resize frames to fit the screen size
        self.gif_frames = [ImageTk.PhotoImage(frame.resize((self.screen_width, self.screen_height), Image.LANCZOS)) for frame in ImageSequence.Iterator(gif)]
        self.current_frame = 0
        self.animate_gif()

    def animate_gif(self):
        frame = self.gif_frames[self.current_frame]
        self.canvas.create_image(0, 0, anchor=tk.NW, image=frame)
        self.current_frame = (self.current_frame + 1) % len(self.gif_frames)

        # Destroy the window after 18 frames
        if self.current_frame == 0:
            self.frame_count += 1
            if self.frame_count == 2:
                self.destroy()
                return

        self.after(15, self.animate_gif)

#background music
pygame.mixer.music.load(r"c:\Users\ishan\OneDrive\Documents\python\The_Great_Wall_game\background audio.mp3")
pygame.mixer.music.play(-1)  # Play indefinitely

if __name__ == "__main__":
    app = HomePage()
    app.mainloop()
