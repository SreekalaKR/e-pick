import customtkinter as ctk
from threading import Thread
from engine import take_command, speak
from commands1 import handle_command

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class VoiceUI:
    def __init__(self, root):
        self.root = root
        self.root.title("EPick AI Assistant")
        self.root.geometry("520x720")
        self.root.resizable(False, False)

        # ===== HEADER =====
        self.header = ctk.CTkLabel(
            root,
            text="🤖 EPick AI Assistant",
            font=("Arial", 20, "bold")
        )
        self.header.pack(pady=10)

        # ===== STATUS =====
        self.status = ctk.CTkLabel(
            root,
            text="Status: Idle",
            text_color="#22c55e",
            font=("Arial", 12)
        )
        self.status.pack()

        # ===== CHAT FRAME =====
        self.chat_frame = ctk.CTkScrollableFrame(
            root,
            width=480,
            height=520,
            corner_radius=15
        )
        self.chat_frame.pack(pady=15)

        self.running = False

        # ===== BUTTONS =====
        self.btn_frame = ctk.CTkFrame(root)
        self.btn_frame.pack(pady=10)

        self.start_btn = ctk.CTkButton(
            self.btn_frame,
            text="🎤 Start",
            fg_color="#22c55e",
            command=self.start
        )
        self.start_btn.grid(row=0, column=0, padx=10)

        self.stop_btn = ctk.CTkButton(
            self.btn_frame,
            text="🛑 Stop",
            fg_color="#ef4444",
            command=self.stop
        )
        self.stop_btn.grid(row=0, column=1, padx=10)

    # ===== CHAT BUBBLE =====
    def add_message(self, msg, sender="ai"):
        frame = ctk.CTkFrame(self.chat_frame, corner_radius=12)
        
        if sender == "user":
            frame.configure(fg_color="#1f2937")
            anchor = "e"
            text_color = "white"
        else:
            frame.configure(fg_color="#0f172a")
            anchor = "w"
            text_color = "#22c55e"

        label = ctk.CTkLabel(
            frame,
            text=msg,
            wraplength=350,
            justify="left",
            text_color=text_color,
            font=("Arial", 13)
        )
        label.pack(padx=10, pady=8)

        frame.pack(pady=5, padx=10, anchor=anchor)

    # ===== STATUS =====
    def update_status(self, text, color="#22c55e"):
        self.status.configure(text=f"Status: {text}", text_color=color)

    # ===== START =====
    def start(self):
        if self.running:
            return

        self.running = True
        self.update_status("Starting...", "#facc15")

        def run():
            speak("EPick is ready")
            self.update_status("Listening...")

            while self.running:
                query = take_command()

                if query == "none":
                    continue

                self.root.after(0, self.add_message, query, "user")
                self.update_status("Thinking...", "#38bdf8")

                response = handle_command(query)

                self.root.after(0, self.add_message, response, "ai")
                self.update_status("Listening...", "#22c55e")

        Thread(target=run, daemon=True).start()

    # ===== STOP =====
    def stop(self):
        self.running = False
        speak("Stopping assistant")
        self.update_status("Stopped", "#ef4444")


def start_ui():
    root = ctk.CTk()
    app = VoiceUI(root)
    root.mainloop()