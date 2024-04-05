import flet as ft

def main(page):

    first_name = ft.TextField(label="Họ", autofocus=True)
    last_name = ft.TextField(label="Tên đệm")
    greetings = ft.Column()

    def btn_click(e):
        greetings.controls.append(ft.Text(f"Chào bạn, {first_name.value} {last_name.value}!"))
        first_name.value = ""
        last_name.value = ""
        page.update()
        first_name.focus()

    page.add(
        first_name,
        last_name,
        ft.ElevatedButton("Click", on_click=btn_click),
        greetings,
    )

ft.app(target=main)