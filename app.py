import tkinter as tk
from tkinter import messagebox
import random
# دالة توليد لون فاتح
def random_light_color(base_color):
   if base_color == "pink":
       r, g, b = (255, 182 + random.randint(0, 30), 193 + random.randint(0, 30))
   elif base_color == "blue":
       r, g, b = (173 + random.randint(0, 50), 216 + random.randint(0, 39), 230 + random.randint(0, 25))
   return f'#{r:02x}{g:02x}{b:02x}'
# حركة النزول
def animate_drop(lines, color_name, symbol):
   output_canvas.delete("all")
   boxes = []
   for i, text in enumerate(lines):
       color = random_light_color(color_name)
       rect = output_canvas.create_rectangle(80, -40, 520, 0, fill=color, outline="black")
       txt = output_canvas.create_text(300, -20, text=f"{symbol} {text}",
                                       font=("Arial", 12, "bold"), fill="black")
       boxes.append((rect, txt))
   def drop_step(index=0):
       if index < len(boxes):
           rect, txt = boxes[index]
           y_target = 20 + index * 50   # 👈 رجعنا المسافة 50 بين كل بوكس
           def move():
               coords = output_canvas.coords(rect)
               if coords[1] < y_target:
                   output_canvas.move(rect, 0, 5)
                   output_canvas.move(txt, 0, 5)
                   output_canvas.after(20, move)
               else:
                   output_canvas.move(rect, 0, -3)
                   output_canvas.move(txt, 0, -3)
                   output_canvas.after(50, lambda:
                       (output_canvas.move(rect, 0, 3),
                        output_canvas.move(txt, 0, 3)))
           move()
           output_canvas.after(250, drop_step, index + 1)
   drop_step()
# معالجة الإدخال تلقائيًا
def handle_input(event=None):
   user_input = entry.get().strip()
   if not user_input:
       messagebox.showwarning("خطأ", "الرجاء إدخال نص أو قائمة")
       return
   if "," in user_input:
       items = [item.strip() for item in user_input.split(",") if item.strip()]
       animate_drop(items, "pink", "⭐")
   else:
       animate_drop(list(user_input), "blue", "🌟")
def clear_text():
   entry.delete(0, tk.END)
   output_canvas.delete("all")
# إعداد النافذة
root = tk.Tk()
root.title("تجربة الجملة التكرارية for")
root.geometry("600x500")
root.resizable(False, False)
tk.Label(root, text="أدخل النص أو القائمة (القائمة مفصولة بفواصل):",
        font=("Arial", 13)).pack(pady=5)
# فريم الإدخال + زر المسح
input_frame = tk.Frame(root)
input_frame.pack(pady=5)
entry = tk.Entry(input_frame, width=40, font=("Arial", 14))
entry.grid(row=0, column=0, padx=5)
entry.bind("<Return>", handle_input)
clear_btn = tk.Button(input_frame, text="مسح",
                     command=clear_text,
                     bg="#ADD8E6", fg="black",   # 👈 أزرق فاتح
                     width=8, height=1,
                     font=("Arial", 11, "bold"))
clear_btn.grid(row=0, column=1, padx=5)
# مساحة العرض
output_canvas = tk.Canvas(root, width=600, height=350, bg="#FFFACD")
output_canvas.pack(pady=10)
root.mainloop()