import streamlit as st
import pandas as pd


def convert_units(value:float, from_unit:str, to_unit:str):
 if from_unit == "kilograms" and to_unit == "grams":
        return value * 1000
 elif from_unit == "grams" and to_unit == "kilograms":
        return value / 1000
 elif from_unit == "grams" and to_unit == "pounds":
        return value / 453.592
 elif from_unit == "pounds" and to_unit == "grams":
        return value * 453.592
 elif from_unit == "pounds" and to_unit == "ounces":
        return value * 16
 elif from_unit == "ounces" and to_unit == "pounds":
        return value / 16
 elif from_unit == "liters" and to_unit == "milliliters":
        return value * 1000
 elif from_unit == "milliliters" and to_unit == "liters":
        return value / 1000
 elif from_unit == "liters" and to_unit == "gallons":
        return value * 0.264172
 elif from_unit == "gallons" and to_unit == "liters":
           return value / 0.264172 
 elif from_unit =="kilometers" and to_unit=="meters":
        return value * 1000
 elif from_unit =="meters" and to_unit=="kilometers":
        return value / 1000
 elif from_unit =="meters" and to_unit=="centimeters":
        return value * 100
 elif from_unit =="centimeters" and to_unit=="meters":
        return value / 100
    #   print("value:",value)
    #   print("=from_unit:",from_unit)
    #   print("to_unit:",to_unit)

     #1 kilometer is eeual to 1000 meters
    #1 meter is equal to 100 centimeters
    # 1 centimeter is equal to 10 millimeters
    # 1 inch is equal to 2.54 centimeters
    # 1 foot is equal to 12 inches
    # 1 mile is equal to 5280 feet
    # 1 yard is equal to 3 feet
    # 1 liter is equal to 1000 milliliters
    # 1 gram is equal to 1000 milligrams
    # 1 kilogram is equal to 1000 grams
    # 1 pound is equal to 16 ounces
    # 1 ounce is equal to 28.3495 grams
    # 1 gallon is equal to 3.78541 liters
    # 1 pound is equal to 0.453592 kilograms
#      if from_unit =="kilograms" and to_unit=="grams":
#         return value*1000
def main():
    st.title("Unit Converter")
    st.write("Welcome to the Unit Converter!")
    vlue=st.number_input("Enter value:", min_value=0.0, step=0.1)
    from_unit =st.selectbox("From unit:", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches","kilograms","grams","pounds","ounces","liters","milliliters"])
    to_unit =st.selectbox("To unit:", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches","kilograms","grams","pounds","ounces","liters","milliliters"])
    if st.button("Convert"):
      result=convert_units(vlue,from_unit,to_unit)

    st.write("The vlue of convert:",result," ",to_unit) 
if __name__ == "__main__":
      main()       

  
