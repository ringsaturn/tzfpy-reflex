import reflex as rx
import tzfpy


class TZState(rx.State):
    tz: str = ""

    def get_tz(self, form_data):
        lng = float(form_data["lng"])
        lat = float(form_data["lat"])
        name = tzfpy.get_tz(lng, lat)
        self.tz = name


def index() -> rx.Component:
    return rx.container(
        rx.form(
            rx.color_mode.button(position="top-right"),
            rx.heading("Timezone Lookup", size="9"),
            rx.text("Enter a latitude and longitude to find the timezone.", size="5"),
            rx.input(
                "Longitude",
                placeholder="Enter longitude, eg. -74.0060",
                name="lng",
                type="number",
            ),
            rx.input(
                "Latitude",
                placeholder="Enter latitude, eg. 40.7128",
                name="lat",
                type="number",
            ),
            rx.text(f"Timezone: {TZState.tz}", size="5"),
            rx.button("Submit", type="submit"),
            on_submit=TZState.get_tz,
        ),
        rx.box(
            rx.el.span(
                "Powered by tzfpy.",
                class_name="px-2 py-0.5 font-small text-center text-slate-9",
            ),
            class_name="flex flex-row justify-center items-center w-full",
        ),
    )


app = rx.App()
app.add_page(index)
