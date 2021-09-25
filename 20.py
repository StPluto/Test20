#!/usr/bin/env python3
# -*- config: utf-8 -*-

# напишите программу, состоящую из двух списков Listbox . В первом будет,
# например, перечень товаров, заданный программно. Второй изначально пуст, пусть это
# будет перечень покупок. При клике на одну кнопку товар должен переходить из одного
# списка в другой. При клике на вторую кнопку – возвращаться (человек передумал покупать).
# Предусмотрите возможность множественного выбора элементов списка и их перемещения.

from tkinter import Tk, Listbox, Button

(lambda root: (lambda buy: (lambda shop, goods: (lambda button1, button2: [shop.insert('end', i) for i in
                                                                           ['apple', 'bananas', 'tomato', 'potato',
                                                                            'carrot', 'pineapple', 'bread', 'butter',
                                                                            'milk', 'meat']] + [button1.pack(),
                                                                                                button2.pack(),
                                                                                                shop.pack(side='left'),
                                                                                                goods.pack(
                                                                                                    side='right')] + [
                                                                              root.mainloop()])(
    Button(text="Преобразовать>>>Преобразовать", command=lambda i=shop, j=goods: buy(i, j)),
    Button(text="Преобразовать<<<Преобразовать", command=lambda i=goods, j=shop: buy(i, j))))(
    Listbox(selectmode='extended'), Listbox(selectmode='extended')))(
    lambda first, second: [second.insert('end', first.get(i)) for i in first.curselection()] + [first.delete(i) for i in
                                                                                                reversed(list(
                                                                                                    first.curselection()))]))(
    Tk())
