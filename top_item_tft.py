import customtkinter as ctk
from item_automation import webscrape_items, webscrape_champion


def update_items_label():
    item_data_list = webscrape_items()
    champion_data_list = webscrape_champion()

    updated_champion_label = "\n".join(
        f"{index+1}. {champion[0]}: {champion[1]}"
        for index, champion in enumerate(champion_data_list)
    )

    updated_label = "\n".join(
        f"{index+1}. {item[0]}: {item[1]}" for index, item in enumerate(item_data_list)
    )

    champions_label.configure(text=updated_champion_label)
    items_label.configure(text=updated_label)


root = ctk.CTk()
root.geometry("400x400")
root.title("Top Items TFT Snapshot")
root.resizable(False, False)
ctk.set_appearance_mode("light")

items_champions_frame = ctk.CTkFrame(root, width=300, height=250)
items_champions_frame.propagate(False)
items_label = ctk.CTkLabel(
    items_champions_frame, text="", wraplength=250, anchor="center", justify="left"
)
champions_label = ctk.CTkLabel(
    items_champions_frame, wraplength=250, anchor="center", justify="left", text=""
)

generate_items_button = ctk.CTkButton(
    root, command=update_items_label, text="Get Top 6"
)

generate_items_button.pack(pady=20)
items_champions_frame.pack(pady=20)
items_label.pack(pady=10, padx=10)
champions_label.pack(pady=20, padx=10)
root.mainloop()
