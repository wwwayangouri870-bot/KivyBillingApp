from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class BillingApp(App):
    def build(self):
        self.items = []
        self.gst = 18

        main = BoxLayout(orientation="vertical", padding=15, spacing=10)

        title = Label(text="Perfect Collection Billing App", font_size=24, bold=True)
        main.add_widget(title)

        form = GridLayout(cols=2, spacing=10, size_hint_y=None, height=180)

        form.add_widget(Label(text="Item Name"))
        self.item_name = TextInput(multiline=False)
        form.add_widget(self.item_name)

        form.add_widget(Label(text="Price"))
        self.price = TextInput(multiline=False, input_filter="float")
        form.add_widget(self.price)

        form.add_widget(Label(text="Quantity"))
        self.qty = TextInput(multiline=False, input_filter="int")
        form.add_widget(self.qty)

        main.add_widget(form)

        add_btn = Button(text="Add Item", size_hint_y=None, height=50)
        add_btn.bind(on_press=self.add_item)
        main.add_widget(add_btn)

        self.bill_label = Label(text="No items added", font_size=16)
        main.add_widget(self.bill_label)

        total_btn = Button(text="Calculate Total", size_hint_y=None, height=50)
        total_btn.bind(on_press=self.calculate_total)
        main.add_widget(total_btn)

        self.total_label = Label(text="Total: ₹0", font_size=22, bold=True)
        main.add_widget(self.total_label)

        return main

    def add_item(self, instance):
        name = self.item_name.text
        price = self.price.text
        qty = self.qty.text

        if name == "" or price == "" or qty == "":
            self.bill_label.text = "Please fill all fields"
            return

        price = float(price)
        qty = int(qty)
        amount = price * qty

        self.items.append((name, price, qty, amount))

        self.item_name.text = ""
        self.price.text = ""
        self.qty.text = ""

        bill_text = ""
        for item in self.items:
            bill_text += f"{item[0]} | ₹{item[1]} x {item[2]} = ₹{item[3]}\n"

        self.bill_label.text = bill_text

    def calculate_total(self, instance):
        subtotal = sum(item[3] for item in self.items)
        gst_amount = subtotal * self.gst / 100
        total = subtotal + gst_amount

        self.total_label.text = (
            f"Subtotal: ₹{subtotal:.2f}\n"
            f"GST 18%: ₹{gst_amount:.2f}\n"
            f"Total: ₹{total:.2f}"
        )


BillingApp().run()
