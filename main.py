import flet as ft
from db import main_db


def main(page: ft.Page):
    page.title = "Список покупок"
    page.theme_mode = ft.ThemeMode.LIGHT

    item_list = ft.Column(spacing=10)

    filter_value = "все"

    #  Загрузка товаров из базы

    def load_items():
        item_list.controls.clear()
        for item_id, name, bought in main_db.get_items():
            item_list.controls.append(
                create_item_row(item_id=item_id, item_name=name, bought=bought)
            )
        page.update()

    
    #  Создать строку товара
    def create_item_row(item_id, item_name, bought):

        checkbox = ft.Checkbox(
            label=item_name,
            value=bool(bought),
            expand=True
        )

        # обновить состояние куплено/не куплено
        def toggle_bought(e):
            main_db.set_bought(item_id, checkbox.value)
            page.update()

        checkbox.on_change = toggle_bought

        # удалить товар
        def delete_item(_):
            main_db.delete_item(item_id)
            load_items()

        delete_btn = ft.IconButton(
            icon=ft.Icons.DELETE,
            icon_color="red",
            on_click=delete_item
        )

        return ft.Row([checkbox, delete_btn], alignment="spaceBetween")

    
    #  Добавить товар
    def add_item(_):
        if item_input.value:
            name = item_input.value
            item_id = main_db.add_item(name)
            item_list.controls.append(
                create_item_row(item_id=item_id, item_name=name, bought=0)
            )
            item_input.value = ""
            page.update()

    #  Сортировка
    
    def change_filter(e):
        nonlocal filter_value
        filter_value = filter_dropdown.value
        reload_filtered_items()

    # фильтр по все/купленные/не купленные
    def reload_filtered_items():
        item_list.controls.clear()

        all_items = main_db.get_items()

        for (item_id, name, bought) in all_items:
            if filter_value == "купленные" and bought == 0:
                continue
            if filter_value == "не купленные" and bought == 1:
                continue

            item_list.controls.append(
                create_item_row(item_id=item_id, item_name=name, bought=bought)
            )

        page.update()

    
    #  UI элементы
    item_input = ft.TextField(label="Введите товар", expand=True, on_submit=add_item)
    add_button = ft.ElevatedButton( text="ADD",on_click=add_item)
    
    


    filter_dropdown = ft.Dropdown(
        width=200,
        value="все",
        on_change=change_filter,
        options=[
            ft.dropdown.Option("все"),
            ft.dropdown.Option("купленные"),
            ft.dropdown.Option("не купленные"),
        ]
    )

    page.add(
        ft.Text("Список покупок", size=25, weight=ft.FontWeight.BOLD),
        ft.Row([item_input, add_button]),
        ft.Row([ft.Text("Сортировать:"), filter_dropdown]),
        item_list
    )

    load_items()


if __name__ == "__main__":
    main_db.init_db()
    ft.app(target=main)