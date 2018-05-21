# from tkinter.ttk import * as yyy
import tkinter.ttk as ttk
from tkinter import *
import Test_Function


#Tal Peretz- 312468929
#Tom Rozanski 204117576
class Welcome():

    def __init__(self, master):
        self.master = master
        self.master.geometry('400x200+100+200')
        self.master.title('WELCOME')
        self.master.configure(background='gray25')

        self.label1 = Label(self.master, text="the function split the matrix to hlaf upper or lower ", fg="DarkOrchid1",
                            bg="gray25").grid(row=0, column=2, sticky=W)
        self.label2 = Label(self.master, text="function two decrypt a string", fg="DarkOrchid1", bg="gray25").grid(
            row=1, column=2, sticky=W)
        self.label3 = Label(self.master, text="function three merge two sorted collection to one", fg="DarkOrchid1",
                            bg="gray25").grid(row=2, column=2, sticky=W)
        self.label4 = Label(self.master, text="print sorted countrey name acoording your sorted choise",
                            fg="DarkOrchid1", bg="gray25").grid(row=3, column=2, sticky=W)
        self.botton1 = Button(self.master, text="question 1", fg="DarkOrchid1", bg="gray25",
                              command=self.gotoWagesq1).grid(row=0)
        self.botton2 = Button(self.master, text="question 2", fg="DarkOrchid1", bg="gray25",
                              command=self.gotoWagesq2).grid(row=1)
        self.botton3 = Button(self.master, text="question 3", fg="DarkOrchid1", bg="gray25",
                              command=self.gotoWagesq3).grid(row=2)
        self.botton4 = Button(self.master, text="question 4", fg="DarkOrchid1", bg="gray25",
                              command=self.gotoWagesq4).grid(row=3)
        self.botton_quit = Button(self.master, text="quit", fg="DarkOrchid1", bg="gray25", command=self.finish).grid(
            row=4, columnspan=2)

    def gotoWagesq1(self):
        root2 = Toplevel(self.master)
        myGUI = q1Wages(root2)

    def gotoWagesq2(self):
        root2 = Toplevel(self.master)
        myGUI = q2Wages(root2)

    def gotoWagesq3(self):
        root2 = Toplevel(self.master)
        myGUI = q3Wages(root2)

    def gotoWagesq4(self):
        root2 = Toplevel(self.master)
        myGUI = q4Wages(root2)

    def finish(self):
        self.master.destroy()


class q1Wages():

    def __init__(self, master):
        self.mymatrix = StringVar()
        self.how_cut = StringVar()
        self.master = master
        self.master.geometry('700x200+500+300')
        self.master.title('question 1 ')
        self.master.configure(background='gray25')
        combo = ttk.Combobox(self.master, textvariable=self.how_cut)
        combo.grid(row=4, column=1, sticky=W)
        combo['values'] = ('upper', 'lower')
        combo.current(0)

        self.label1 = Label(self.master, text="enter to the input text a matrix and chose in the "
                                              "combobox upper or lower case.\n"
                                              "enter the matrix with space, and for new row press enter, then press"
                                              " commit button for result\n"
                                              "you have a default matrix for example ",
                            fg="DarkOrchid1", bg="gray25").grid(row=0, columnspan=3)
        self.label_input = Label(self.master, text="user input:", fg="DarkOrchid1", bg="gray25").grid(row=3, column=0)
        self.label_output = Label(self.master, text="output:", fg="DarkOrchid1", bg="gray25").grid(row=3, column=2)
        self.input_text = Text(self.master, height=5, width=10, wrap=WORD)
        self.input_text.grid(row=3, column=1, sticky=W)
        self.input_text.insert(END, '1 2 3\na 5 6\n7 c 9')
        self.button3 = Button(self.master, height=1, width=10, text="Commit", fg="DarkOrchid1", bg="gray25",
                              command=lambda: self.gui_half_q1())
        self.button3.grid(row=4)
        self.button2 = Button(self.master, text="back", fg="DarkOrchid1", bg="gray25", command=self.my_quit).grid(row=5)

    def my_quit(self):
        self.master.destroy()

    # Q1
    def gui_half_q1(self):
        value = self.input_text.get("1.0", "end-1c")
        k = self.how_cut.get()
        if k == "upper":
            k = 0
        else:
            k = 1

        value = str(value)
        matrix = [list(item for item in arr.split(' ')) for arr in value.split('\n')]
        my_result = Test_Function.half(matrix, k)
        my_result = '\n'.join([''.join(['{:1} '.format(item) for item in row]) for row in my_result])
        self.output_text = Text(self.master, height=5, width=10, wrap=WORD)
        self.output_text.grid(row=3, column=3)
        self.output_text.insert(END, my_result)


class q2Wages():

    def __init__(self, master):
        self.my_string = StringVar()
        self.my_key = IntVar()
        self.my_key.set("3")
        self.my_string.set("solongandthanksforthefish")
        self.master = master
        self.master.geometry('500x200+500+300')
        self.master.title('question 2')
        self.master.configure(background='gray25')

        self.label1 = Label(self.master, text="enter a string an kry number press the ptrform decrypt botton ",
                            fg="DarkOrchid1", bg="gray25").grid(row=0, columnspan=2)
        self.label_input = Label(self.master, text="enter string", fg="DarkOrchid1", bg="gray25").grid(row=1, column=0)
        self.entry_string = Entry(self.master, textvariable=self.my_string).grid(row=1, column=1, sticky=W)
        self.label_output = Label(self.master, text="enter key", fg="DarkOrchid1", bg="gray25").grid(row=2)
        self.entry_key = Entry(self.master, textvariable=self.my_key).grid(row=2, column=1, sticky=W)
        self.botton3 = Button(self.master, text="preform decrypt ", fg="DarkOrchid1", bg="gray25",
                              command=self.gui_decrypt_q2).grid(row=3)
        self.botton2 = Button(self.master, text="back", fg="DarkOrchid1", bg="gray25",
                              command=self.myquit).grid(row=4)

    def myquit(self):
        self.master.destroy()

    def gui_decrypt_q2(self):
        string = self.my_string.get()
        key = self.my_key.get()
        res = Test_Function.decrypt(string, key)
        self.res_label = Label(self.master, text="the string is: " + res, bg="cyan2").grid(row=7, column=1)


class q3Wages():

    def __init__(self, master):
        self.first = StringVar()
        self.second = StringVar()
        self.first.set('0 2 4')
        self.second.set('1 3 5')

        self.master = master
        self.master.geometry('700x200+500+300')
        self.master.title('question 3')
        self.master.configure(background='gray25')

        self.label1 = Label(self.master, text="enter collection according the example and press commit",
                            fg="DarkOrchid1", bg="gray25").grid(row=0, column=2)
        self.label2 = Label(self.master, text="first collection", fg="DarkOrchid1", bg="gray25").grid(row=3, column=0)
        self.label3 = Label(self.master, text="second collection",
                            fg="DarkOrchid1", bg="gray25").grid(row=4, column=0)
        self.label4 = Label(self.master, text="result", fg="DarkOrchid1", bg="gray25").grid(row=3, column=3)

        self.my_first = Entry(self.master, textvariable=self.first).grid(row=3, column=2)
        self.mt_second = Entry(self.master, textvariable=self.second).grid(row=4, column=2)
        self.botton1 = Button(self.master, text="commit", fg="DarkOrchid1", bg="gray25", command=self.gui_merge_call_q3)
        self.botton1.grid(row=5, column=2)
        self.botton2 = Button(self.master, text="back", fg="DarkOrchid1", bg="gray25", command=self.myquit).grid(row=5,
                                                                                                                 column=3)

    def myquit(self):
        self.master.destroy()

    def gui_merge_call_q3(self):
        list1 = self.first.get()
        list2 = self.second.get()
        list1 = list1.split()
        list2 = list2.split()
        list1 = list(list1)
        list2 = list(list2)

        list_merge = []
        for i in Test_Function.merge_sorted_lists(list1, list2):
            list_merge.append(i)

        self.output_text = Text(self.master, height=5, width=10, wrap=WORD)
        self.output_text.grid(row=3, column=4)
        for x in list_merge:
            self.output_text.insert(END, x + ' ')


class q4Wages():

    def __init__(self, master):
        self.master = master
        self.master.geometry('500x200+500+300')
        self.name_file = StringVar(self.master, value='winners.txt')
        self.rate = StringVar()
        self.master.title('question 4')
        self.master.configure(background='gray25')
        combo = ttk.Combobox(self.master, textvariable=self.rate)
        combo.grid(row=2, column=1, sticky=W)
        combo['values'] = ('gold', 'total', 'weighted')
        combo.current(0)

        self.label1 = Label(self.master, text="chose in the combobox how to rank from file", fg="DarkOrchid1",
                            bg="gray25").grid(row=0, columnspan=2)
        self.label_input = Label(self.master, text="enter file name", fg="DarkOrchid1", bg="gray25").grid(row=1,
                                                                                                          sticky=W)
        self.entry_string = Entry(self.master, textvariable=self.name_file).grid(row=1, column=1, sticky=W)

        self.label_output = Label(self.master, text="enter key", fg="DarkOrchid1", bg="gray25").grid(row=2, sticky=W)

        self.botton3 = Button(self.master, text="result: ", fg="DarkOrchid1", bg="gray25",
                              command=self.gui_rank_q4).grid(row=3)
        self.botton2 = Button(self.master, text="back", fg="DarkOrchid1", bg="gray25",
                              command=self.myquit).grid(row=4)

    def myquit(self):
        self.master.destroy()

    def gui_rank_q4(self):
        file_name = self.name_file.get()
        how_to_rank = self.rate.get()
        res = Test_Function.rank(file_name, how_to_rank)
        self.res_label = Label(self.master, text=("\n".join(res)), bg="cyan2").grid(row=7, column=1)


def main():
    root = Tk()
    myGUIWelcome = Welcome(root)
    root.mainloop()


if __name__ == '__main__':
    main()
