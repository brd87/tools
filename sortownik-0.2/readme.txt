How to use:
1. Download and ran browser extension for renaming downloaded files
   https://github.com/brd87/Extensions/tree/main/2M
2. Create list.txt in same folder as sortownik.pyw
3. Inside list.txt in the first line provide maximum file size in bytes and in the second line, 
   directory from which you want to sort files
4. Every another line after that should have host name of the downloaded files (the whole part before "-") and
   directory where you want to move files from particular host
5. After creating list.txt you can run sortownik.pyw

Example list.txt:
200000000
C:\downloads
pbs.twimg.com C:\here\twitter
scontent-waw1-1.xx.fbcdn.net C:\here\facebook

- The maximum file for sorting is 200MB
- Files will be sorted only from directory C:\downloads
- Only files from host pbs.twimg.com (twitter) and scontent-waw1-1.xx.fbcdn.net (facebook) will be sorted
