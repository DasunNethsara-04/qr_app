# imports
import webbrowser
from kivymd.app import MDApp
from kivy.lang import Builder
from pyzbar.pyzbar import ZBarSymbol
from kivymd.uix.snackbar import Snackbar

KV = """
#:import ZBarCam kivy_garden.zbarcam.ZBarCam
#:import ZBarSymbol pyzbar.pyzbar.ZBarSymbol
MDBoxLayout:
    orientation: "vertical"
    ZBarCam:
        id:zbarcam
        code_types:ZBarSymbol.QRCODE.value,ZBarSymbol.EAN13.value
        on_symbols:app.on_symbols(*args)
"""

class MyApp(MDApp):
    def build(self) -> None:
        self.root = Builder.load_string(KV)

    def on_symbols(self, instance, symbols) -> None:
        if not symbols == "":
            for symbol in symbols:
                if(symbol.type=="QRCODE"):
                    webbrowser.open(symbol.data)
                else:
                    continue
                # print("QR: " , symbol.data.decode())
                # webbrowser.open(symbol.data.decode())

# fgmnfhmhmgh
if __name__ == "__main__":
    MyApp().run()