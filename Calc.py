import sys
import sympy
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtCore import (Qt, Slot)
from PySide6.QtWidgets import (QApplication, QWidget, QLayout, QGridLayout, QPushButton, QLineEdit, QSizePolicy)


class CalculatorGUI(QWidget):
    def __init__(self):
        super().__init__()
        # ~~~~~~~~~~ BEGINNING OF CONSTRUCTOR ~~~~~~~~~~
        # --------------------
        # QWidget's properties
        self.setWindowTitle("Calculator GUI")  # setWindowTitle refers to the QWidget class
        self.setGeometry(450, 220, 330, 330)
        # --------------------
        # ********** ATTRIBUTE SECTION **********
        # --------------------------
        # CalculatorGUI's attributes
        #   Boolean attributes
        self.bool_waiting_for_operand = False

        #   Integer attributes

        #   String attributes
        self.overall_string = ""
        self.sympy_box_string = ""
        self.display_box_string = ""
        self.symbol_box_string = ""

        #   QLineEdit attributes
        self.display_box = QLineEdit("")
        self.symbol_box = QLineEdit("")
        self.symbol_box.setReadOnly(True)

        #   QFont attributes
        self.font_display_box = QFont()
        self.font_symbol_box = QFont()
        self.font_button = QFont()
        self.font_symbol = QFont()
        self.extra_font = QFont()
        #   QPushButton attributes
        #       Number buttons
        self.button_num1 = QPushButton("1")
        self.button_num2 = QPushButton("2")
        self.button_num3 = QPushButton("3")
        self.button_num4 = QPushButton("4")
        self.button_num5 = QPushButton("5")
        self.button_num6 = QPushButton("6")
        self.button_num7 = QPushButton("7")
        self.button_num8 = QPushButton("8")
        self.button_num9 = QPushButton("9")
        self.button_num0 = QPushButton("0")
        #       Operand buttons
        self.button_equal = QPushButton("=")
        self.button_plus = QPushButton("+")
        self.button_minus = QPushButton("-")
        self.button_times = QPushButton("*")
        self.button_division = QPushButton("/")
        #       Symbol buttons
        self.button_backspace = QPushButton("⌫")
        self.button_clear_all = QPushButton("CE")
        # self.button_clear = QPushButton("C")
        self.button_dot = QPushButton(".")
        self.button_left_bracket = QPushButton("(")
        self.button_right_bracket = QPushButton(")")
        # --------------------------
        # ********** ATTRIBUTE (CHANGING BEHAVIOUR) SECTION **********
        # ---------------------------------
        # Altering some of those attributes

        #   QFont attributes
        #       Regarding our self.font_display_box (QFont) attribute
        self.font_display_box.setPointSize(self.font_display_box.pointSize() + 10)
        #       Regarding our self.font_symbol_box (QFont) attribute
        self.font_symbol_box.setPointSize(self.font_symbol_box.pointSize() + 4)
        #       Regarding our self.font_button (QFont) attribute
        # self.font_button.setBold(True)
        self.font_button.setPointSize(self.font_button.pointSize() + 6)
        #       Regarding our self.font_symbol (QFont) attribute
        self.font_symbol.setPointSize(self.font_symbol.pointSize() + 6)
        self.extra_font.setPointSize(self.extra_font.pointSize() + 2)

        #   QLineEdit attributes
        #       Regarding our self.display_box (QLineEdit) attribute

        self.display_box.setAlignment(Qt.AlignRight)
        self.display_box.setMaxLength(15)
        self.display_box.setFont(self.font_display_box)
        #       Regarding our self.symbol_box (QLineEdit) attribute

        self.symbol_box.setAlignment(Qt.AlignRight)
        self.symbol_box.setMaxLength(10)
        self.symbol_box.setFont(self.font_symbol_box)

        #   QPushButton attributes
        #       Number buttons
        #           Setting the size policy
        self.button_num0.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_num1.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_num2.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_num3.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_num4.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_num5.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_num6.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_num7.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_num8.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_num9.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        #           Setting the font
        self.button_num0.setFont(self.font_button)
        self.button_num1.setFont(self.font_button)
        self.button_num2.setFont(self.font_button)
        self.button_num3.setFont(self.font_button)
        self.button_num4.setFont(self.font_button)
        self.button_num5.setFont(self.font_button)
        self.button_num6.setFont(self.font_button)
        self.button_num7.setFont(self.font_button)
        self.button_num8.setFont(self.font_button)
        self.button_num9.setFont(self.font_button)

        #       Operand buttons
        #           Setting the size policy
        self.button_equal.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_plus.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_minus.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_times.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_division.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        #           Setting the font
        self.button_equal.setFont(self.font_symbol)
        self.button_plus.setFont(self.font_symbol)
        self.button_minus.setFont(self.font_symbol)
        self.button_times.setFont(self.font_symbol)
        self.button_division.setFont(self.font_symbol)

        #       Symbol buttons
        #           Setting the size policy
        self.button_backspace.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_clear_all.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        # self.button_clear.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_dot.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_left_bracket.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        self.button_right_bracket.setSizePolicy(QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding))
        #           Setting the font
        self.button_dot.setFont(self.font_symbol)
        self.button_left_bracket.setFont(self.font_symbol)
        self.button_right_bracket.setFont(self.font_symbol)
        self.button_backspace.setFont(self.extra_font)
        self.button_clear_all.setFont(self.extra_font)
        # ---------------------------------
        # ********** LAYOUT SECTION **********
        # -----------------
        # Our class' layout
        #   QGridLayout which makes a grid of the layout
        layout = QGridLayout()
        layout.setSpacing(2)
        layout.setContentsMargins(10, 12, 10, 10)
        #       Setting the appropriate size for the QWidget and locking it in place
        # layout.setSizeConstraint(QLayout.SetFixedSize)

        #   Adding our widgets to our QGridLayout layout
        #       QLineEdit attributes
        #           Regards the first row of the grid
        layout.addWidget(self.display_box, 0, 1, 1, 3)
        layout.addWidget(self.symbol_box, 0, 4, 1, 1)

        #       QPushButton attributes
        #           Regards the second row of the grid
        layout.addWidget(self.button_clear_all, 1, 1)
        layout.addWidget(self.button_backspace, 1, 2)
        # layout.addWidget(self.button_clear, 1, 2)
        layout.addWidget(self.button_left_bracket, 1, 3)
        layout.addWidget(self.button_right_bracket, 1, 4)

        #           Regards the third row of the grid
        layout.addWidget(self.button_num7, 2, 1)
        layout.addWidget(self.button_num8, 2, 2)
        layout.addWidget(self.button_num9, 2, 3)
        layout.addWidget(self.button_division, 2, 4)

        #           Regards the fourth row of the grid
        layout.addWidget(self.button_num4, 3, 1)
        layout.addWidget(self.button_num5, 3, 2)
        layout.addWidget(self.button_num6, 3, 3)
        layout.addWidget(self.button_times, 3, 4)

        #           Regards the fifth row of the grid
        layout.addWidget(self.button_num1, 5, 1)
        layout.addWidget(self.button_num2, 5, 2)
        layout.addWidget(self.button_num3, 5, 3)
        layout.addWidget(self.button_minus, 5, 4)
        layout.addWidget(self.button_plus, 6, 4)

        #           Regards the sixth row of the grid
        layout.addWidget(self.button_dot, 6, 1)
        layout.addWidget(self.button_num0, 6, 2)
        layout.addWidget(self.button_equal, 6, 3)

        # -----------------
        # ********** ASSIGNING LAYOUT SECTION **********
        # -------------------------------------
        # Setting the layout (so it is visible)
        self.setLayout(layout)  # setLayout refers to the QWidget class
        # -------------------------------------
        # ********** SIGNALS & EVENTS SECTION **********
        # ----------------------------------
        # Connecting the signals/events to the corresponding functions
        #   Number button signals/events
        self.button_num0.clicked.connect(self.pressed_num0)
        self.button_num1.clicked.connect(self.pressed_num1)
        self.button_num2.clicked.connect(self.pressed_num2)
        self.button_num3.clicked.connect(self.pressed_num3)
        self.button_num4.clicked.connect(self.pressed_num4)
        self.button_num5.clicked.connect(self.pressed_num5)
        self.button_num6.clicked.connect(self.pressed_num6)
        self.button_num7.clicked.connect(self.pressed_num7)
        self.button_num8.clicked.connect(self.pressed_num8)
        self.button_num9.clicked.connect(self.pressed_num9)

        #   Operand button signals/events
        self.button_equal.clicked.connect(self.pressed_button_equal)
        self.button_plus.clicked.connect(self.pressed_button_plus)
        self.button_minus.clicked.connect(self.pressed_button_minus)
        self.button_times.clicked.connect(self.pressed_button_times)
        self.button_division.clicked.connect(self.pressed_button_division)

        #   Symbol button signals/events
        self.button_backspace.clicked.connect(self.pressed_button_backspace)
        self.button_clear_all.clicked.connect(self.pressed_button_clear_all)
        # self.button_clear.clicked.connect(self.pressed_button_clear)
        self.button_dot.clicked.connect(self.pressed_button_dot)
        # ----------------------------------
        # ~~~~~~~~~~ END OF CONSTRUCTOR ~~~~~~~~~~

    # Handles the events happening inside each slot function

    # The Slot decorator is responsible for the signal/event relationship/connection
    @Slot()
    # Slots & signals
    #       Number button signals
    def pressed_num0(self):
        # Displaying to the console, so we know the key has been pressed
        print("0 has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "0")

    def pressed_num1(self):
        # Displaying to the console, so we know the key has been pressed
        print("1 has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "1")

    def pressed_num2(self):
        # Displaying to the console, so we know the key has been pressed
        print("2 has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "2")

    def pressed_num3(self):
        # Displaying to the console, so we know the key has been pressed
        print("3 has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "3")

    def pressed_num4(self):
        # Displaying to the console, so we know the key has been pressed
        print("4 has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "4")

    def pressed_num5(self):
        # Displaying to the console, so we know the key has been pressed
        print("5 has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "5")

    def pressed_num6(self):
        # Displaying to the console, so we know the key has been pressed
        print("6 has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "6")

    def pressed_num7(self):
        # Displaying to the console, so we know the key has been pressed
        print("7 has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "7")

    def pressed_num8(self):
        # Displaying to the console, so we know the key has been pressed
        print("8 has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "8")

    def pressed_num9(self):
        # Displaying to the console, so we know the key has been pressed
        print("9 has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "9")

    # #       Operand buttons signals
    def pressed_button_equal(self):
        # Displaying to the console, so we know the key has been pressed
        print("= has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(str(sympy.sympify(self.display_box.text())))

    def pressed_button_plus(self):
        # Displaying to the console, so we know the key has been pressed
        print("+ has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "+")

    def pressed_button_minus(self):
        # Displaying to the console, so we know the key has been pressed
        print("- has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "-")

    def pressed_button_times(self):
        # Displaying to the console, so we know the key has been pressed
        print("* has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "*")

    def pressed_button_division(self):
        # Displaying to the console, so we know the key has been pressed
        print("/ has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + "/")

    #       Symbol buttons signals
    def pressed_button_backspace(self):
        # Displaying to the console, so we know the key has been pressed
        print("⌫ has been pressed")
        # Calling the string_manipulator to handle the input/output
        st = self.display_box.text()
        st = st[:-1]
        self.display_box.setText(st)

    def pressed_button_clear_all(self):
        # Displaying to the console, so we know the key has been pressed
        print("CE has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.clear()

    # def pressed_button_clear(self):
    #     # Displaying to the console, so we know the key has been pressed
    #     print("C has been pressed")
    #     # Calling the string_manipulator to handle the input/output
    #     self.display_box.clear()

    def pressed_button_dot(self):
        # Displaying to the console, so we know the key has been pressed
        print(". has been pressed")
        # Calling the string_manipulator to handle the input/output
        self.display_box.setText(self.display_box.text() + ".")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = CalculatorGUI()
    calc.show()
    sys.exit(app.exec_())
