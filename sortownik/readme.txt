How to use:
1. Download and ran browser extension for renaming downloaded files
   https://github.com/brd87/Extensions/tree/main/2M
2. Create list.json in the appdata\roaming\sortownik\
3. Inside list.json in the "size" variable, change value to any maximum file size in bytes and in the "download" to 
   directory from which you want to sort files
4. Variables inside "list" scope should be named same as their hosts which names you can find by using the extension for the downloaded files. Value shoud be
   directory where you want to move files from particular host
5. After creating list.json you can run the sortownik.pyw manualy or move it to autostart folder in appdata

list.json template:
{
    "size":200000000,
    "download":"A:\\example",
    "list":{
        "pbs.twimg.com":"A:\\test\\tw",
        "scontent-waw1-1.xx.fbcdn.net":"A:\\test\\tw"
    }
}

template tips:
- The maximum file for sorting is 200MB
- Files will be sorted only from directory A:\\example
- Only files from host pbs.twimg.com (twitter) and scontent-waw1-1.xx.fbcdn.net (facebook) will be sorted
