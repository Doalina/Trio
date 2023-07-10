## TRIO v.1.0.1

### how to use?

0. Make sure you have python and pip installed
1. Download the repository 
2. Launch `pip install -e . ` in terminal in the repository you just downloaded 
3. Сall `trio` in terminal
4. Enjoy!

### what does it do?

The bot has 3 main functions
1. Adress Book
    - a contact consists of a name, arbitrary amount of phones, and a birthday
    - gives a list of employees who have a Birthday in a given amount of days
    - gives a number of days left to birthday for a given name
    - allows search 
    - the emplyees data is safely stored as `data.bin` in the AdressBook folder

2. Folder Sorter
    - sorts files into separate folders with respect to the extensions;
    - renames everything with respect to the convention;
    - unpacks archives;
    - deletes empty folders;
    - ignores unknown formats;
    - sorts files in the specified folder by category: images, documents, videos;

3. Note Book 
    - a note consists of a name, content and hashtags
    - allows search
    - allows sorting by hashtags
    - the data is conveniantly stored as `notes_book.csv` in the NoteBook folder

