import tkinter as tk
from tkinter import *
import webbrowser
from tkinter import ttk

#Creates class for GUI
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        # SEts title of window
        self.master.title("Web Page Generator")
        
        # Creates button to generate HTML page
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=1, padx=(10,10), pady=(10,10))

        # Creates button to submit custom text
        self.cust_btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.cust_btn.grid(row=2, column=2, padx=(10,10), pady=(10,10))
        
        # Creates entry widget for user input
        self.cust_text = Entry(self.master, width=135)
        # Postitions entry in GUI for custom text  
        self.cust_text.grid(row=1, column=0, columnspan=3, padx=(30, 10), pady=(30, 10), sticky=W)

        #creates label box above entry widget
        self.varInst = StringVar()
        self.lblvarInst = Label(self.master,text='Enter custom text or click the Default HTML page button', font=("helvetica", 14))
        self.lblvarInst.grid(row=0, column=0, padx=(30,0), pady=(30,0))

    #Creates defaultHTML window and content
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    # Creates Custom HTML window
    def customHTML(self):
        htmlCustText = self.cust_text.get()
        htmlCustFile = open("index.html", "w")
        htmlCustContent = "<html>\n<body>\n<h1>" + htmlCustText + "</h1>\n</body>\n</html>"
        htmlCustFile.write(htmlCustContent)
        htmlCustFile.close()
        webbrowser.open_new_tab("index.html")
        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
