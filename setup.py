import os, json

def create_config():
    default_config = {
        "main_admin_id": input("Введите ID главного администратора: "),
        "info": {
            "greeting": "Привет, я бот-продавец. Чтобы узнать, что я умею, напиши /help",
        },
    }

    open("config.json", "w").write(json.dumps(default_config, indent=4, ensure_ascii=False))


if not os.path.exists("config.json"):
    create_config()
elif input("config.json уже существует. Вы уверены, что хотите перезаписать его? Все данные будут потеряны. (y/n)").lower() == "y":
    create_config()
else:
    print("Пропускаем создание config.json")

if os.path.exists("database.db") and input("Вы хотите перезаписать базу данных? Все данные будут потеряны. (y/n)").lower() == "y":
    os.remove("database.db")
    
