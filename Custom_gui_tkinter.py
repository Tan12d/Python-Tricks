# from customtkinter import *
# from PIL import Image

# app = CTk()
# app.geometry("500x400")

# set_appearance_mode("dark")

# img = Image.open("message_icon.png")

# btn = CTkButton(master=app, text="Click Me", corner_radius=32, fg_color="#C850C0", hover_color="#4158D0", border_color="#FFCC70", border_width=2, image=CTkImage(dark_image=img, light_image=img))

# btn.place(relx=0.5, rely=0.5, anchor="center")

# app.mainloop()


from customtkinter import *

app = CTk()
app.geometry("500x400")


tabview = CTkTabview(master=app)
tabview.pack(padx=20, pady=20)

tabview.add("Tab 1")
tabview.add("Tab 2")
tabview.add("Tab 3")

label_1 = CTkLabel(master=tabview.tab("Tab 1"), text="This is tab 1")
label_1.pack(padx=20, pady=20)

label_2 = CTkLabel(master=tabview.tab("Tab 2"), text="This is tab 2")
label_2.pack(padx=20, pady=20)

label_3 = CTkLabel(master=tabview.tab("Tab 3"), text="This is tab 3")
label_3.pack(padx=20, pady=20)

app.mainloop()