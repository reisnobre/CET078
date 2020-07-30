from transaction import Transaction, SplitTransaction, CashTransaction

lTransaction = Transaction(600);
print(lTransaction.getTransactionTotal())
sTransaction = SplitTransaction(1, 10, 100)
print("{:.2f}".format(sTransaction.getTransactionTotal()))
cTransaction = CashTransaction(10, 600)
print(cTransaction.getTransactionTotal())

