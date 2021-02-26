# /usr/bin/python3
# -*- coding:utf-8 -*-
import tkinter as tk
import tkinter.messagebox as msg
import tkinter.filedialog as fd
from tkinter import *
import json
import random
import os
import sys


def shuwei(num, character, weishu, side):
    append_text = ''
    for i in range(weishu - len(str(num))):
        append_text = append_text + character
    if side == 'front':
        return append_text + str(num)
    elif side == 'back':
        return str(num) + append_text


def get_question(qtype_chosed_list, chapter_chosed_list):
    question_chosed_list = []
    for timu in timu_list:
        if timu['q_type'] in qtype_chosed_list and timu['chapter'] in chapter_chosed_list:
            question_chosed_list.append(timu)
    return question_chosed_list


def lingqiyihang(text, num):
    sth_list = []
    while len(text) > num:
        sth = text[:num]
        text = text[num:]
        sth_list.append(sth)
    return '\n'.join(sth_list) + '\n' + text


def question_empty():
    msg.showwarning(title='提示', message='所有题目都已做完！')
    entry_in()


def choose_file():
    global timu_list, whole_chapter_list, whole_qtype_list
    file_path = 'NoFileChosed'
    while file_path[-5:] != '.json':
        if file_path == '':
            sys.exit(0)
        if file_path != 'NoFileChosed':
            msg.showwarning(title='提示', message='请选择json文件！')
        default_dir = os.path.split(os.path.realpath(__file__))[0]
        file_path = tk.filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(default_dir)))
    with open(file_path, 'r', encoding='utf-8') as f:
        timu_list = json.load(f)
    whole_chapter_list = []
    whole_qtype_list = []
    for timu in timu_list:
        if timu['chapter'] not in whole_chapter_list:
            whole_chapter_list.append(timu['chapter'])
        if timu['q_type'] not in whole_qtype_list:
            whole_qtype_list.append(timu['q_type'])


def entry_in():
    label_welcome.place(relwidth=0.5, relheight=0.1, relx=0.25, rely=0.05)
    entry_ok_button.place(relwidth=0.15, relheight=0.08, relx=0.25, rely=0.85)
    all_chapter_button.place(relwidth=0.15, relheight=0.08, relx=0.6, rely=0.85)
    for i in range(len(whole_qtype_list)):
        qtype_checkbutton_list[i].place(relwidth=0.2, relx=0.2, rely=0.2 + i * 0.05)
    for i in range(len(whole_chapter_list)):
        chapter_checkbutton_list[i].place(relwidth=0.2, relx=0.6, rely=0.2 + i * 0.05)


def entry_out():
    global chosed_timu
    for i in range(len(whole_qtype_list)):
        if qtype_var_list[i].get() == 1 and whole_qtype_list[i] not in qtype_chosed_list:
            qtype_chosed_list.append(whole_qtype_list[i])
        elif qtype_var_list[i].get() == 0 and whole_qtype_list[i] in qtype_chosed_list:
            qtype_chosed_list.remove(whole_qtype_list[i])
    for i in range(len(whole_chapter_list)):
        if chapter_var_list[i].get() == 1 and whole_chapter_list[i] not in chapter_chosed_list:
            chapter_chosed_list.append(whole_chapter_list[i])
        elif chapter_var_list[i].get() == 0 and whole_chapter_list[i] in chapter_chosed_list:
            chapter_chosed_list.remove(whole_chapter_list[i])
    if qtype_chosed_list != [] and chapter_chosed_list == []:
        msg.showwarning(title='提示', message='请选择章节！')
        return
    elif chapter_chosed_list != [] and qtype_chosed_list == []:
        msg.showwarning(title='提示', message='请选择题型！')
        return
    elif chapter_chosed_list == [] and qtype_chosed_list == []:
        msg.showwarning(title='提示', message='请选择题型和章节！')
        return
    elif get_question(qtype_chosed_list, chapter_chosed_list) == []:
        msg.showwarning(title='提示', message='此种组合无题目！')
        return
    else:
        label_welcome.place_forget()
        entry_ok_button.place_forget()
        all_chapter_button.place_forget()
        for i in range(len(whole_qtype_list)):
            qtype_checkbutton_list[i].place_forget()
        for i in range(len(whole_chapter_list)):
            chapter_checkbutton_list[i].place_forget()
        chosed_timu = get_question(qtype_chosed_list, chapter_chosed_list)
    random_timu()


def entry_out_all_chapter():
    global chosed_timu
    for i in range(len(whole_qtype_list)):
        if qtype_var_list[i].get() == 1 and whole_qtype_list[i] not in qtype_chosed_list:
            qtype_chosed_list.append(whole_qtype_list[i])
        elif qtype_var_list[i].get() == 0 and whole_qtype_list[i] in qtype_chosed_list:
            qtype_chosed_list.remove(whole_qtype_list[i])
    chapter_chosed_list = whole_chapter_list
    if qtype_chosed_list == []:
        msg.showwarning(title='提示', message='请选择题型！')
        return
    elif get_question(qtype_chosed_list, chapter_chosed_list) == []:
        msg.showwarning(title='提示', message='此种组合无题目！')
        return
    else:
        label_welcome.place_forget()
        entry_ok_button.place_forget()
        all_chapter_button.place_forget()
        for i in range(len(whole_qtype_list)):
            qtype_checkbutton_list[i].place_forget()
        for i in range(len(whole_chapter_list)):
            chapter_checkbutton_list[i].place_forget()
        chosed_timu = get_question(qtype_chosed_list, chapter_chosed_list)
    random_timu()


def random_timu():
    global chosed_timu, random_question
    if chosed_timu == []:
        question_empty()
        return
    random_num = random.randint(0, len(chosed_timu) - 1)
    random_question = chosed_timu.pop(random_num)
    if random_question['q_type'] == '1':
        xuanze_on()
    elif random_question['q_type'] == '2':
        tiankong_on()
    elif random_question['q_type'] == '3':
        panduan_on()


def xuanze_on():
    global label_answer, var_option, label_question, option_a, option_b, option_c, option_d
    label_question = Label(main_window, text=lingqiyihang(random_question['content']['title'], 38),
                           anchor='w', justify='left')
    var_option = StringVar()
    option_a = Radiobutton(main_window, text='A. ' + random_question['content']['opt_a'],
                           anchor='w', variable=var_option, value='a', command=xuanze_1)
    option_b = Radiobutton(main_window, text='B. ' + random_question['content']['opt_b'],
                           anchor='w', variable=var_option, value='b', command=xuanze_1)
    option_c = Radiobutton(main_window, text='C. ' + random_question['content']['opt_c'],
                           anchor='w', variable=var_option, value='c', command=xuanze_1)
    option_d = Radiobutton(main_window, text='D. ' + random_question['content']['opt_d'],
                           anchor='w', variable=var_option, value='d', command=xuanze_1)
    label_question.place(relwidth=0.8, relheight=0.3, relx=0.1, rely=0.05)
    option_a.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.35)
    option_b.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.4)
    option_c.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.45)
    option_d.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.5)


def xuanze_1():
    global next_button, label_answer, option_a_text, option_b_text, option_c_text, option_d_text
    option_a.place_forget()
    option_b.place_forget()
    option_c.place_forget()
    option_d.place_forget()
    option_a_text = Label(main_window, text='     A. ' + random_question['content']['opt_a'], anchor='w')
    option_b_text = Label(main_window, text='     B. ' + random_question['content']['opt_b'], anchor='w')
    option_c_text = Label(main_window, text='     C. ' + random_question['content']['opt_c'], anchor='w')
    option_d_text = Label(main_window, text='     D. ' + random_question['content']['opt_d'], anchor='w')
    option_a_text.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.352)
    option_b_text.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.4)
    option_c_text.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.452)
    option_d_text.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.5)
    if var_option.get() != random_question['content']['ans'].lower():
        label_answer = Label(main_window, text='答案是： ' + random_question['content']['ans'].upper(), anchor='w')
    else:
        label_answer = Label(main_window, text='答对了w', anchor='w')
    label_answer.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.65)
    next_button = Button(main_window, text='下一题', command=xuanze_off)
    next_button.place(relwidth=0.15, relheight=0.08, relx=0.425, rely=0.85)


def xuanze_off():
    label_question.place_forget()
    option_a_text.place_forget()
    option_b_text.place_forget()
    option_c_text.place_forget()
    option_d_text.place_forget()
    label_answer.place_forget()
    next_button.place_forget()
    random_timu()


def tiankong_on():
    global label_question, answer_get, label_question, answer_sheet, answer_get_button
    label_question = Label(main_window, text=lingqiyihang(random_question['content']['title'], 38) + '\n\n请输入答案：',
                           anchor='w', justify='left')
    answer_get = StringVar()
    answer_sheet = Entry(main_window, show=None, textvariable=answer_get)
    answer_get_button = Button(main_window, text='提交', command=tiankong_1)
    label_question.place(relwidth=0.8, relheight=0.25, relx=0.1, rely=0.05)
    answer_sheet.place(relwidth=0.45, relx=0.1, rely=0.3)
    answer_get_button.place(relwidth=0.1, relheight=0.06, relx=0.6, rely=0.295)


def tiankong_1():
    global label_answer, next_button, answer_print
    answer_get_button.place_forget()
    answer_sheet.place_forget()
    if answer_get.get() == random_question['content']['ans'].lower():
        label_answer = Label(main_window, text='答对了w', anchor='w')
    else:
        label_answer = Label(main_window, text='答案是： ' + random_question['content']['ans'], anchor='w')
    answer_print = Label(main_window, text=answer_get.get(), anchor='w')
    answer_print.place(relwidth=0.45, relx=0.1, rely=0.298)
    label_answer.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.65)
    next_button = Button(main_window, text='下一题', command=tiankong_off)
    next_button.place(relwidth=0.15, relheight=0.08, relx=0.425, rely=0.85)


def tiankong_off():
    label_answer.place_forget()
    next_button.place_forget()
    label_question.place_forget()
    answer_print.place_forget()
    random_timu()


def panduan_on():
    global label_question, var_option, option_a, option_b
    label_question = Label(main_window, text=lingqiyihang(random_question['content']['title'], 38) + '\n\n请选择正误：',
                           anchor='w', justify='left')
    var_option = StringVar()
    option_a = Radiobutton(main_window, text='正确',
                           anchor='w', variable=var_option, value='a', command=panduan_1)
    option_b = Radiobutton(main_window, text='错误',
                           anchor='w', variable=var_option, value='b', command=panduan_1)
    label_question.place(relwidth=0.8, relheight=0.3, relx=0.1, rely=0.05)
    option_a.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.3)
    option_b.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.35)


def panduan_1():
    global label_answer, next_button, answer_get, answer_sheet, answer_get_button, option_a_text, option_b_text
    option_a.place_forget()
    option_b.place_forget()
    option_a_text = Label(main_window, text='     正确', anchor='w')
    option_b_text = Label(main_window, text='     错误', anchor='w')
    option_a_text.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.3)
    option_b_text.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.352)
    if var_option.get() == 'a' and random_question['content']['ans'].lower() == 'a':
        label_answer = Label(main_window, text='答对了w', anchor='w')
        next_button = Button(main_window, text='下一题', command=panduan_off_1)
        label_answer.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.42)
        next_button.place(relwidth=0.15, relheight=0.08, relx=0.425, rely=0.85)
    elif var_option.get() == 'a' and random_question['content']['ans'].lower() == 'b':
        label_answer = Label(main_window, text='答案是：错误    请输入改正意见：', anchor='w')
        answer_get = StringVar()
        answer_sheet = Entry(main_window, show=None, textvariable=answer_get)
        answer_get_button = Button(main_window, text='提交', command=panduan_2)
        label_answer.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.42)
        answer_sheet.place(relwidth=0.45, relx=0.1, rely=0.5)
        answer_get_button.place(relwidth=0.1, relheight=0.06, relx=0.6, rely=0.495)
    elif var_option.get() == 'b' and random_question['content']['ans'].lower() == 'a':
        label_answer = Label(main_window, text='答案是：正确', anchor='w')
        next_button = Button(main_window, text='下一题', command=panduan_off_1)
        label_answer.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.42)
        next_button.place(relwidth=0.15, relheight=0.08, relx=0.425, rely=0.85)
    elif var_option.get() == 'b' and random_question['content']['ans'].lower() == 'b':
        label_answer = Label(main_window, text='答对了w    请输入改正意见：', anchor='w')
        answer_get = StringVar()
        answer_sheet = Entry(main_window, show=None, textvariable=answer_get)
        answer_get_button = Button(main_window, text='提交', command=panduan_2)
        label_answer.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.42)
        answer_sheet.place(relwidth=0.45, relx=0.1, rely=0.5)
        answer_get_button.place(relwidth=0.1, relheight=0.06, relx=0.6, rely=0.495)


def panduan_off_1():
    label_question.place_forget()
    option_a_text.place_forget()
    option_b_text.place_forget()
    label_answer.place_forget()
    next_button.place_forget()
    random_timu()


def panduan_2():
    global label_answer_2, answer_print, next_button
    answer_get_button.place_forget()
    answer_sheet.place_forget()
    answer_print = Label(main_window, text=answer_get.get(), anchor='w')
    if answer_get.get() == random_question['content']['correct'].lower():
        label_answer_2 = Label(main_window, text='答对了w', anchor='w')
    else:
        label_answer_2 = Label(main_window, text='答案是： ' + random_question['content']['correct'], anchor='w')
    next_button = Button(main_window, text='下一题', command=panduan_off_2)
    answer_print.place(relwidth=0.45, relx=0.1, rely=0.498)
    label_answer_2.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.65)
    next_button.place(relwidth=0.15, relheight=0.08, relx=0.425, rely=0.85)


def panduan_off_2():
    label_question.place_forget()
    option_a_text.place_forget()
    option_b_text.place_forget()
    label_answer.place_forget()
    next_button.place_forget()
    answer_print.place_forget()
    next_button.place_forget()
    label_answer_2.place_forget()
    random_timu()


main_window = Tk()
main_window.title('背题助手')
main_window.geometry('600x450')
qtype_meaning = ['选择', '填空', '判断']

choose_file()

label_welcome = Label(main_window, text='请选择题型与章节！', font=('宋体', 14, 'bold'), relief='solid')
qtype_checkbutton_list = []
qtype_var_list = []
qtype_chosed_list = []
chapter_checkbutton_list = []
chapter_var_list = []
chapter_chosed_list = []
entry_ok_button = Button(main_window, text='确认', command=entry_out)
all_chapter_button = Button(main_window, text='章节全选', command=entry_out_all_chapter)
for i in range(len(whole_qtype_list)):
    qtype_var_list.append(IntVar())
    qtype_checkbutton_list.append(Checkbutton(main_window, text=qtype_meaning[int(whole_qtype_list[i]) - 1],
                                              variable=qtype_var_list[i], onvalue=1, offvalue=0))
for i in range(len(whole_chapter_list)):
    chapter_var_list.append(IntVar())
    chapter_checkbutton_list.append(Checkbutton(main_window, text=shuwei(int(whole_chapter_list[i]), ' ', 2, 'back'),
                                                variable=chapter_var_list[i], onvalue=1, offvalue=0))

entry_in()
main_window.mainloop()

