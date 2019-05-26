import kivy
kivy.require("1.10.1")
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

class calculator(GridLayout):
    def __init__(self,**kwargs):
        super(calculator,self).__init__(**kwargs)
        self.cols=2
        self.total=TextInput(multiline=False,input_filter="float")
        self.add_widget(self.total)
        self.add_widget(Label(text="mL total volume"))
        self.goal=TextInput(multiline=False,input_filter="float")
        self.add_widget(self.goal)
        self.add_widget(Label(text="% dextrose"))
        
        self.ing1=TextInput(multiline=False,input_filter="float")
        self.add_widget(self.ing1)
        self.ing1desc=TextInput(text="mL additional ingredient",multiline=False)
        self.add_widget(self.ing1desc)
        self.ing2=TextInput(multiline=False,input_filter="float")
        self.add_widget(self.ing2)
        self.ing2desc=TextInput(text="mL additional ingredient",multiline=False)
        self.add_widget(self.ing2desc)
        self.ing3=TextInput(multiline=False,input_filter="float")
        self.add_widget(self.ing3)
        self.ing3desc=TextInput(text="mL additional ingredient",multiline=False)
        self.add_widget(self.ing3desc)
        self.ing4=TextInput(multiline=False,input_filter="float")
        self.add_widget(self.ing4)
        self.ing4desc=TextInput(text="mL additional ingredient",multiline=False)
        self.add_widget(self.ing4desc)

        def calc(a):
            ingreds=[]
            totalvol=float(self.total.text)
            goalpercent=float(self.goal.text)
            if self.ing1.text:
                ing=float(self.ing1.text),self.ing1desc.text
                ingreds.append(ing)
            if self.ing2.text:
                ing=float(self.ing2.text),self.ing2desc.text
                ingreds.append(ing)
            if self.ing3.text:
                ing=float(self.ing3.text),self.ing3desc.text
                ingreds.append(ing)
            if self.ing4.text:
                ing=float(self.ing4.text),self.ing4desc.text
                ingreds.append(ing)
            
        self.btn=Button(text="calculate")
        self.btn.bind(on_press=calc)
        self.add_widget(self.btn)
        
class MyApp(App):
    def build(self):
        return calculator()

if __name__=="__main__":
    MyApp().run()
