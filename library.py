borrowuser = []
borrowbook = []
with open('borrow.txt' , 'a+') as f :
    pass
f.close()
with open('borrow.txt' , 'r') as f :
    s = f.read()
    q = s.split('\n')
    a = len(q) / 2
    i = 0
    while i < int(a) :
        borrowuser[i : i] = [q[2 * i]]
        borrowbook[i : i] = [q[2 * i + 1]]
        i = i + 1
f.close()
with open('books.txt' , 'r') as f :
    s = f.read()
    books = [i for i in s.split('\n') if i]
f.close()
with open('users.txt' , 'r') as f :
    s = f.read()
    users = [i for i in s.split('\n') if i]
f.close()
buser = {}
i = 0
while i < len(users) :
    a = []
    k = 0
    j = 0
    while j < len(borrowbook) :
        if borrowuser[j] == users[i] :
            a[k : k] = [borrowbook[j]]
            k = k + 1
        j = j + 1
    buser[users[i]] = a
    i = i + 1
bbook = {}
i = 0
while i < len(books) :
    a = []
    k = 0
    j = 0
    while j < len(borrowbook) :
        if borrowbook[j] == books[i] :
            a[k : k] = [borrowuser[j]]
            k = k + 1
        j = j + 1
    bbook[books[i]] = a
    i = i + 1
t = 1
while t == 1 :
    print('1.show list of books')
    print('2.show list of users')
    print('3.borrow a book')
    print('4.return a book')
    print('5.show borrowed books by a user')
    print('6.add a book')
    print('7.add a user')
    print('8.end')
    o = input("enter option: ")
    option = int(o)
    if option == 1 :
        print(books)
    if option == 2 :
        print(users)
    if option == 3 :
        user = input("enter user: ")
        check = 0
        i = 0
        while i < len(users) :
            if users[i] == user :
                check = 1
            i = i + 1
        if check == 0 :
            print('user not found!')
        else :
            book = input("enter book: ")
            check = 0
            i = 0
            while i < len(books) :
                if books[i] == book :
                    check = 1
                    ii = i
                i = i + 1
            if check == 0 :
                print('book not found!')
            else :
                a = len(buser[user])
                buser[user][a : a] = [book]
                a = len(bbook[book])
                bbook[book][a : a] = [user]
                a = len(borrowbook)
                borrowuser[a : a] = [user]
                borrowbook[a : a] = [book]
                del books[ii]
    if option == 4 :
        user = input("enter user: ")
        check = 0
        i = 0
        while i < len(users) :
            if users[i] == user :
                check = 1
            i = i + 1
        if check == 0 :
            print('user not found!')
        else:
            book = input("enter book: ")
            check = 0
            i = 0
            while i < len(buser[user]) :
                if buser[user][i] == book :
                    check = 1
                i = i + 1
            if check == 0 :
                print('user didnot borrow such book!')
            else :
                  a = len(books)
                  books[a : a] = [book]
    if option == 5 :
        user = input("enter user: ")
        check = 0
        i = 0
        while i < len(users) :
            if users[i] == user :
                check = 1
            i = i + 1
        if check == 0 :
            print('user not found!')
        else:
            print(buser[user])
    if option == 6 :
        book = input("enter book: ")
        check = 0
        i = 0
        while i < len(books):
            if books[i] == book:
                check = 1
            i = i + 1
        if check == 1 :
            print('this book is in library')
        else :
            a = len(books)
            books[a : a] = [book]
            bbook[book] = []
    if option == 7 :
        user = input("enter user: ")
        check = 0
        i = 0
        while i < len(users):
            if users[i] == user:
                check = 1
            i = i + 1
        if check == 1 :
            print('this user is in library!')
        else:
            a = len(users)
            users[a : a] = [user]
            buser[user] = []
    if option == 8 :
        t = 0
    with open('borrow.txt', 'w') as f :
        i = 0
        while i < len(borrowbook) :
            f.write(borrowuser[i] + '\n' + borrowbook[i] + '\n')
            i = i + 1
    f.close()
    with open('users.txt', 'w') as f :
        i = 0
        while i < len(users) :
            f.write(users[i] + '\n')
            i = i + 1
    f.close()
    with open('books.txt', 'w') as f :
        i = 0
        while i < len(books) :
            f.write(books[i] + '\n')
            i = i + 1
    f.close()
