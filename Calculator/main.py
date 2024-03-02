from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (350, 500)

Builder.load_file('calculator.kv')

class CalcLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'
    
    def button_press(self, button):
        prior = self.ids.calc_input.text
        if "Error" in prior:
            prior = ''
        if prior == '0':
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'
     
    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}{sign}'
        
    def dot(self):
        prior = self.ids.calc_input.text
        if "." in prior:
            pass
        else:
            self.ids.calc_input.text = f'{prior}.'
    
    def remove(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = prior[:-1]
        
    def pos_neg(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text =  f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text =  f'-{prior}'   

    def equal(self):
        prior = self.ids.calc_input.text
        try:
            answer = eval(prior)
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Error"
        
class CalculatorApp(App):
    def build(self):
        return CalcLayout()
 
if __name__ == '__main__':
    CalculatorApp().run()
