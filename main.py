import requests
import base64
import os
import sys
import time

token = input("[ + ] Put The Bot Token Here ~> ")


def clear():
    os.system("clear")


def countdown(t, msg):
    while t:
        secs = divmod(t, 60)
        timer = f"{secs[1]}"
        print(f"{msg} {timer} Seconds", end="\r")
        time.sleep(1)
        t -= 1


def verify_token(token):
    headers = {"Authorization": f"Bot {token}"}
    url = "https://discord.com/api/v10/users/@me"
    response = requests.get(url, headers=headers)
    return response


def image_path():
    clear()
    os.system("ls")
    avatar_path = input("\n[ + ] Choose From Above or Drag The Image Here ~> ")
    try:
        with open(avatar_path, "rb") as file:
            image_content = file.read()
            base64_image = base64.b64encode(image_content).decode("utf-8")
            return base64_image
    except Exception as e:
        print(e)
        sys.exit(1)


def patch_api(choice, file_path, endpoint):
    headers = {"Authorization": f"Bot {token}"}
    data = {f"{choice}": f"data:image/gif;base64,{file_path}"}
    response = requests.patch(
        f"https://discord.com/api/v10/{endpoint}/@me", headers=headers, json=data
    )
    return response


def main():
    verify = verify_token(token)
    if verify.status_code == 200:
        while True:
            clear()
            option = input(
                "Bot Username : "
                + verify.json()["username"]
                + "#"
                + verify.json()["discriminator"]
                + "\n\n[ 1 ] Change Bot Avatar\n[ 2 ] Change Bot Banner\n[ 3 ] Change Application Icon\n[ 4 ] Exit\n[ ~ ] Enter The Number Of Desired Option Here ~> "
            )
            if option == "1":
                if patch_api("avatar", image_path(), "users").status_code == 200:
                    countdown(
                        5,
                        "[ + ] Changed Bot Avatar Successfully, Redirecting To Main Menu In",
                    )
                    clear()
                else:
                    print("[ ! ] Failed To Change Bot Avatar")
                    break
            elif option == "2":
                if patch_api("banner", image_path(), "users").status_code == 200:
                    countdown(
                        5,
                        "[ + ] Changed Bot Banner Successfully, Redirecting To Main Menu In",
                    )
                    clear()
                else:
                    print("[ ! ] Failed To Change Bot Banner")
                    break
            elif option == "3":
                if patch_api("icon", image_path(), "applications").status_code == 200:
                    countdown(
                        5,
                        "[ + ] Changed Application Icon Successfully, Redirecting To Main Menu In",
                    )
                    clear()
                else:
                    print("[ ! ] Failed To Change Application Icon")
            elif option == "4":
                print("[ ! ] Exiting...")
                break
            else:
                print("[ ! ] Invalid Input")
                time.sleep(3)
                clear()
                pass
    else:
        print("[ ! ] Invalid Token")


main()
