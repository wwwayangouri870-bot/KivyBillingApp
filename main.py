from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.spinner import Spinner

from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


class BillingApp(App):

    def build(self):

        self.total_bill = 0

        # MAIN LAYOUT
        self.layout = BoxLayout(
            orientation='vertical',
            padding=10,
            spacing=10
        )

        # CUSTOMER NAME
        self.customer_input = TextInput(
            hint_text="Customer Name",
            multiline=False,
            size_hint=(1, 0.1)
        )

        # PAYMENT METHOD
        self.payment_spinner = Spinner(
            text='Cash',
            values=('Cash', 'UPI', 'Card'),
            size_hint=(1, 0.1)
        )

        # PRODUCT INPUT
        self.product_input = TextInput(
            hint_text="Product Name",
            multiline=False,
            size_hint=(1, 0.1)
        )

        # QUANTITY
        self.qty_input = TextInput(
            hint_text="Quantity",
            multiline=False,
            input_filter='int',
            size_hint=(1, 0.1)
        )

        # PRICE
        self.price_input = TextInput(
            hint_text="Price",
            multiline=False,
            input_filter='float',
            size_hint=(1, 0.1)
        )

        # ADD BUTTON
        add_button = Button(
            text="Add Item",
            size_hint=(1, 0.1),
            font_size=22
        )

        add_button.bind(on_press=self.add_item)

        # CLEAR BUTTON
        clear_button = Button(
            text="Clear Bill",
            size_hint=(1, 0.1),
            font_size=22
        )

        clear_button.bind(on_press=self.clear_bill)

        # SAVE PDF BUTTON
        save_button = Button(
            text="Save PDF Bill",
            size_hint=(1, 0.1),
            font_size=22
        )

        save_button.bind(on_press=self.save_bill)

        # SCROLL VIEW
        scroll = ScrollView(
            size_hint=(1, 0.45)
        )

        # BILL DISPLAY
        self.bill_label = Label(
            text="===== PERFECT COLLECTION =====",
            size_hint_y=None,
            halign="left",
            valign="top",
            font_size=20
        )

        self.bill_label.bind(
            texture_size=self.update_height
        )

        scroll.add_widget(self.bill_label)

        # TOTAL LABEL
        self.total_label = Label(
            text="Grand Total: ₹0.00",
            font_size=26,
            size_hint=(1, 0.12)
        )

        # ADD WIDGETS
        self.layout.add_widget(self.customer_input)
        self.layout.add_widget(self.payment_spinner)

        self.layout.add_widget(self.product_input)
        self.layout.add_widget(self.qty_input)
        self.layout.add_widget(self.price_input)

        self.layout.add_widget(add_button)
        self.layout.add_widget(clear_button)
        self.layout.add_widget(save_button)

        self.layout.add_widget(scroll)

        self.layout.add_widget(self.total_label)

        return self.layout

    # UPDATE LABEL HEIGHT
    def update_height(self, instance, size):

        self.bill_label.text_size = (
            self.bill_label.width,
            None
        )

        self.bill_label.height = size[1]

    # ADD ITEM
    def add_item(self, instance):

        try:

            customer = self.customer_input.text.strip()

            if customer == "":
                customer = "Walk-in Customer"

            payment = self.payment_spinner.text

            product = self.product_input.text.strip()

            qty = int(self.qty_input.text)

            price = float(self.price_input.text)

            if product == "":
                raise ValueError

            subtotal = qty * price

            gst = subtotal * 0.18

            final_total = subtotal + gst

            self.total_bill += final_total

            self.bill_label.text += (
                f"\n\nCustomer: {customer}"
                f"\nPayment: {payment}"
                f"\nProduct: {product}"
                f"\nQty: {qty}"
                f"\nPrice: ₹{price:.2f}"
                f"\nGST: ₹{gst:.2f}"
                f"\nTotal: ₹{final_total:.2f}"
            )

            self.total_label.text = (
                f"Grand Total: ₹{self.total_bill:.2f}"
            )

            # CLEAR INPUTS
            self.product_input.text = ""
            self.qty_input.text = ""
            self.price_input.text = ""

        except:

            self.bill_label.text += (
                "\n\nInvalid Input"
            )

    # SAVE PDF
    def save_bill(self, instance):

        now = datetime.now().strftime(
            "%d-%m-%Y_%H-%M-%S"
        )

        filename = f"Bill_{now}.pdf"

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        elements = []

        title = Paragraph(
            "<b>PERFECT COLLECTION</b>",
            styles['Title']
        )

        elements.append(title)

        elements.append(Spacer(1, 20))

        bill_text = self.bill_label.text.replace(
            "\n",
            "<br/>"
        )

        bill_paragraph = Paragraph(
            bill_text,
            styles['BodyText']
        )

        elements.append(bill_paragraph)

        elements.append(Spacer(1, 20))

        total_paragraph = Paragraph(
            f"<b>{self.total_label.text}</b>",
            styles['Heading2']
        )

        elements.append(total_paragraph)

        doc.build(elements)

        self.bill_label.text += (
            f"\n\nPDF Saved: {filename}"
        )

    # CLEAR BILL
    def clear_bill(self, instance):

        self.bill_label.text = (
            "===== PERFECT COLLECTION ====="
        )

        self.total_bill = 0

        self.total_label.text = (
            "Grand Total: ₹0.00"
        )


BillingApp().run()