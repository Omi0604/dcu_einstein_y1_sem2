#!/usr/bin/env python3

class BankAccount():

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, add):
        self.balance = self.balance + add

    def withdraw(self, remove):
        if self.balance >= remove:
            self.balance = self.balance - remove

    def __str__(self):
        return (f"Your current balance is {self.balance:.2f} euro")
