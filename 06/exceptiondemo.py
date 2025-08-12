try:
    n = int(input('Number: '))
except ValueError:
    print('Invalid Input!')
except (KeyboardInterrupt,EOFError):
    print('\nBye-bye')
    exit()
else:
    print(n)
finally:
    print('Done')
