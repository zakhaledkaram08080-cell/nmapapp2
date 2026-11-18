from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class NmapApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Nmap Scanner'))
        layout.add_widget(Label(text='Enter IP:'))
        self.ip_input = TextInput(text='127.0.0.1')
        layout.add_widget(self.ip_input)
        btn = Button(text='Scan', size_hint=(1, 0.3))
        btn.bind(on_press=self.do_scan)
        layout.add_widget(btn)
        self.result = Label(text='Result will appear here')
        layout.add_widget(self.result)
        return layout

    def do_scan(self, instance):
        ip = self.ip_input.text
        self.result.text = 'Scanning ' + ip + '...'

if __name__ == '__main__':
    NmapApp().run()
